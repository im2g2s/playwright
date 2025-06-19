import requests

from conftest import RunID


def update_testrail(case_id, status_id, comment="NA"):
    if status_id == 'PASS':
        add_results_for_cases(case_id, 1, comment)
    else:
        add_results_for_cases(case_id, 5, comment)


def add_results_for_cases(testcase_id, testcase_status, comment='NA'):
    testrail_url = 'https://hhax.testrail.net/index.php?/api/v2/add_results_for_cases/' + RunID
    new_headers = {'Content-type': 'application/json',
                   'Authorization': 'Basic YXV0b21hdGlvbnFhQGhoYWV4Y2hhbmdlLmNvbTpBdXRvbWF0aW9uQDEy'}

    body = {
        "results": [
            {
                "case_id": testcase_id,
                "status_id": testcase_status,
                "comment": comment,
            }]
    }
    response = requests.post(url=testrail_url,
                             json=body,
                             headers=new_headers)
