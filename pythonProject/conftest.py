import os
import shutil
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright

VIDEO_DIR = "videos"
RunID = '24341'

@pytest.fixture(scope="session")
def browser():
    os.makedirs(VIDEO_DIR, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


# SELENIUM_GRID_URL = "http://44.198.185.90:4444"

# @pytest.fixture(scope="session")
# def browser():
#     os.makedirs(VIDEO_DIR, exist_ok=True)
#     options = webdriver.ChromeOptions()
#     # Add any options you need
#     driver = webdriver.Remote(
#         command_executor=SELENIUM_GRID_URL,
#         desired_capabilities=DesiredCapabilities.CHROME,
#         options=options
#     )
#     yield driver
#     driver.quit()

@pytest.fixture
def page(browser, request):
    test_name = request.node.name
    context = browser.new_context(
        record_video_dir=VIDEO_DIR,
        record_video_size={"width": 1280, "height": 720}
    )
    page = context.new_page()
    yield page

    video_path = page.video.path()
    context.close()

    if request.node.rep_call.failed:
        new_video_path = os.path.join(VIDEO_DIR, f"{test_name}.webm")

        # Remove existing video with the same name
        if os.path.exists(new_video_path):
            os.remove(new_video_path)

        shutil.move(video_path, new_video_path)
        print(f"Test failed. Video saved as: {new_video_path}")
    else:
        os.remove(video_path)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
