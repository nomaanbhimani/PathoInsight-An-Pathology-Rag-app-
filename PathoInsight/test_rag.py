from query_data import query_rag
from langchain_community.llms.ollama import Ollama
EVAL_PROMPT="""
Expected Response: {expected_response}
Actual Response: {actual_response}
(Answer in true or false )does the actual response match the expected response?"""

def test_data():
    assert query_and_validate(
        question="Normal Adult Bone Marrow Counts (Myelogram)"
        , expected_response="Fat/cell ratio : 50:50Myeloid/erythroid (M/E) ratio : 2-4:1 (mean 3:1)Myeloid series: 30-45% (37.5%)• Myeloblasts : 0.1-3.5%• Promyelocytes: 0.5-5%Erythroid series: 10-15% (mean 12.5%)Megakaryocytes: 0.5%Lymphocytes: 5-20%Plasma cells: < 3%Reticulum cells: 0.1-2%"
    )
def query_and_validate(question: str, expected_response: str):

   
    response=query_rag(question)
    prompt=EVAL_PROMPT.format(
        expected_response=expected_response,
        actual_response=response
    )
    model=Ollama(model="mistral")
    evaluation_result=model.invoke(prompt)
    evaluation_results_str_cleaned = evaluation_result.strip().lower()
    print (prompt)
    if evaluation_results_str_cleaned in ["true", "yes"]:
        print("\033[91m" + f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
        return True
    else:
        print("\033[91m" + f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
        return False