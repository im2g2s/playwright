import os
import shutil
import pytest
from playwright.sync_api import sync_playwright
from utils.config import ENV, BrowserName, headless, video

VIDEO_DIR = "videos"

# 🌐 Browser Fixture
@pytest.fixture(scope="session")
def browser():
    os.makedirs(VIDEO_DIR, exist_ok=True)
    with sync_playwright() as p:
        if BrowserName == 'Chrome':
            browser = p.chromium.launch(headless=headless, slow_mo=500)
        else:
            browser = p.firefox.launch(headless=headless, slow_mo=500)

        yield browser
        browser.close()

# 📄 Page Fixture
@pytest.fixture
def page(browser, request):
    test_name = request.node.name

    context_args = {}
    if video:
        context_args["record_video_dir"] = VIDEO_DIR
        context_args["record_video_size"] = {"width": 1280, "height": 720}

    context = browser.new_context(**context_args)
    page = context.new_page()
    yield page

    if video:
        video_path = page.video.path()
        context.close()

        if request.node.rep_call.failed:
            new_video_path = os.path.join(VIDEO_DIR, f"{test_name}.webm")
            if os.path.exists(new_video_path):
                os.remove(new_video_path)
            shutil.move(video_path, new_video_path)
            print(f"Test failed. Video saved as: {new_video_path}")
        else:
            os.remove(video_path)
    else:
        context.close()

# 🧪 Hook for test result tracking
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
