import logging

def take_screenshot(page, path):
    page.screenshot(path=path)

def log_message(message):
    logging.basicConfig(level=logging.INFO)
    logging.info(message)


