import os
import shutil
import pytest
from playwright.sync_api import sync_playwright, Browser, Page
from utils.config import ENV, BrowserName as ConfigBrowserName, headless as ConfigHeadless, video as ConfigVideo
from utils.logger import log_message
from typing import Generator

VIDEO_DIR = "videos"
SCREENSHOT_DIR = "screenshots"

def get_browser_type() -> str:
    return os.environ.get("BROWSER", ConfigBrowserName).lower()

def get_headless() -> bool:
    env_val = os.environ.get("HEADLESS")
    if env_val is not None:
        return env_val.lower() in ("1", "true", "yes")
    return ConfigHeadless

def get_video() -> bool:
    env_val = os.environ.get("VIDEO")
    if env_val is not None:
        return env_val.lower() in ("1", "true", "yes")
    return ConfigVideo

@pytest.fixture(scope="session")
def browser() -> Generator[Browser, None, None]:
    """Session-scoped browser fixture with robust cleanup and logging."""
    os.makedirs(VIDEO_DIR, exist_ok=True)
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    with sync_playwright() as p:
        browser_type = get_browser_type()
        headless = get_headless()
        log_message(f"Launching browser: {browser_type}, headless={headless}")
        if browser_type == 'chrome':
            browser = p.chromium.launch(headless=headless, slow_mo=500)
        elif browser_type == 'firefox':
            browser = p.firefox.launch(headless=headless, slow_mo=500)
        else:
            browser = p.webkit.launch(headless=headless, slow_mo=500)
        try:
            yield browser
        finally:
            browser.close()
            log_message("Browser closed.")

@pytest.fixture
def page(browser: Browser, request) -> Generator[Page, None, None]:
    """Test-scoped page fixture with video/screenshot capture and robust cleanup."""
    test_name = request.node.name
    context_args = {}
    if get_video():
        context_args["record_video_dir"] = VIDEO_DIR
        context_args["record_video_size"] = {"width": 1280, "height": 720}
    context = browser.new_context(**context_args)
    page = context.new_page()
    try:
        yield page
    except Exception as e:
        screenshot_path = os.path.join(SCREENSHOT_DIR, f"FAIL_{test_name}.png")
        page.screenshot(path=screenshot_path)
        log_message(f"Test failed. Screenshot saved as: {screenshot_path}")
        raise
    finally:
        if get_video():
            try:
                if page.video is not None:
                    video_path = page.video.path()
                    context.close()
                    if hasattr(request.node, "rep_call") and getattr(request.node.rep_call, "failed", False):
                        new_video_path = os.path.join(VIDEO_DIR, f"{test_name}.webm")
                        if os.path.exists(new_video_path):
                            os.remove(new_video_path)
                        shutil.move(video_path, new_video_path)
                        log_message(f"Test failed. Video saved as: {new_video_path}")
                    else:
                        os.remove(video_path)
                else:
                    context.close()
            except Exception as e:
                log_message(f"Error handling video: {e}")
        else:
            context.close()
        log_message(f"Context closed for test: {test_name}")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to attach test result to the request.node for use in fixtures."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
