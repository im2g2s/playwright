import os

BrowserName = os.environ.get('BROWSER', 'Chrome')  # Chrome, Firefox, Edge
RunID = os.environ.get('RUN_ID', '24341')
ENV = os.environ.get('ENV', 'sandbox1')  # Change this to ENTAPPSB or ENTAPP2SB as needed

testrail_url = os.environ.get('TESTRAIL_URL', f'https://hhax.testrail.net/index.php?/api/v2/add_results_for_cases/{RunID}')
BASE_URL = os.environ.get('BASE_URL', 'https://the-internet.herokuapp.com/login')
USERNAME = os.environ.get('USERNAME', 'tomsmith')
PASSWORD = os.environ.get('PASSWORD', 'SuperSecretPassword!')
headless = os.environ.get('HEADLESS', 'False').lower() in ('1', 'true', 'yes')
video = os.environ.get('VIDEO', 'True').lower() in ('1', 'true', 'yes')
Authorization = os.environ.get('AUTHORIZATION', 'Basic YXV0b21hdGlvbnFhQGhoYWV4Y2hhbmdlLmNvbTpBdXRvbWF0aW9uQDEy')

