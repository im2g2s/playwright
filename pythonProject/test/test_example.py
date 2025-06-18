import pytest
from Pages.example_page import ExamplePage

@pytest.fixture(scope="session")
def browser_instance(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

def test_example(browser_instance):
    page = browser_instance.new_page()
    example_page = ExamplePage(page)
    example_page.navigate()
    assert example_page.is_title_correct()
