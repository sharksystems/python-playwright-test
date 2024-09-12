import allure
import pytest

from playwright.sync_api import Playwright

disable_loggers = []


@pytest.fixture(scope='function')
def new_page(playwright: Playwright, request):
    browser_name = request.config.getoption('--browser_name')
    headless = False if request.config.getoption("--headed") else True
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=headless)
    if browser_name == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    if browser_name == "webkit":
        browser = playwright.webkit.launch(headless=headless)
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto(f'https://www.automationexercise.com/')
    yield page
    context.tracing.stop(path="trace.zip")
    browser.close()

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chromium')