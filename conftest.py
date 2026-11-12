import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page
from config.settings import settings
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.fixture(scope="session")
def playwright():
    """Start Playwright once per test session."""
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright) -> Browser:
    """Launch the browser once per session."""
    browser_type = getattr(playwright, settings.BROWSER)
    browser = browser_type.launch(headless=settings.HEADLESS)
    logger.info(f"Launched {settings.BROWSER} browser (headless={settings.HEADLESS})")
    yield browser
    browser.close()
    logger.info("Browser closed")

@pytest.fixture(scope="function")
def context(browser) -> BrowserContext:
    """Create a fresh context for each test (supports video/trace)."""
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        record_video_dir="videos/" if settings.VIDEO_ON_FAILURE else None,
        record_video_size={"width": 1280, "height": 720},
    )
    # Start tracing if enabled
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context, request) -> Page:
    """Provide a fresh page for each test and handle failure artifacts."""
    page = context.new_page()
    page.set_default_timeout(settings.DEFAULT_TIMEOUT)
    page.set_default_navigation_timeout(settings.NAVIGATION_TIMEOUT)

    yield page

    # On failure: screenshot + stop tracing + save video
    if request.node.rep_call.failed:
        logger.error(f"Test failed: {request.node.name}")

        # Screenshot
        if settings.SCREENSHOT_ON_FAILURE:
            page.screenshot(path=f"screenshots/{request.node.name}.png", full_page=True)
            logger.info(f"Screenshot saved for failed test: {request.node.name}")

        # Trace
        context.tracing.stop(path=f"traces/{request.node.name}.zip")
        logger.info(f"Trace saved: traces/{request.node.name}.zip")
    else:
        # Stop tracing without saving if test passed
        context.tracing.stop()

    page.close()

# Hook to make the test result available in the fixture
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)