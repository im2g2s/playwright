import requests
from utils.config import Authorization, testrail_url


def update_testrail(case_id, status_id, comment="NA"):
    if status_id == 'PASS':
        add_results_for_cases(case_id, 1, comment)
        assert True
    else:
        add_results_for_cases(case_id, 5, comment)
        assert False


def add_results_for_cases(testcase_id, testcase_status, comment='NA'):
    new_headers = {'Content-type': 'application/json',
                   'Authorization': Authorization}
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
