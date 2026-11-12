from playwright.sync_api import Page, expect
from config.settings import settings
from utils.logger import get_logger
from utils.screenshot import take_screenshot

logger = get_logger(__name__)

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.page.set_default_timeout(settings.DEFAULT_TIMEOUT)

    def navigate(self, url: str | None = None) -> None:
        """Navigate to a URL (defaults to base URL)."""
        target = url or settings.BASE_URL
        logger.info(f"Navigating to: {target}")
        self.page.goto(target, timeout=settings.NAVIGATION_TIMEOUT)

    def click(self, locator: str) -> None:
        """Click an element."""
        logger.debug(f"Clicking: {locator}")
        self.page.locator(locator).click()

    def fill(self, locator: str, value: str) -> None:
        """Fill an input field."""
        logger.debug(f"Filling '{locator}' with '{value}'")
        self.page.locator(locator).fill(value)

    def get_text(self, locator: str) -> str:
        """Get text content of an element."""
        text = self.page.locator(locator).inner_text()
        logger.debug(f"Text from '{locator}': {text}")
        return text

    def wait_for(self, locator: str, state: str = "visible", timeout: int | None = None) -> None:
        """Wait for an element to reach a certain state."""
        timeout = timeout or settings.DEFAULT_TIMEOUT
        logger.debug(f"Waiting for '{locator}' to be {state}")
        self.page.locator(locator).wait_for(state=state, timeout=timeout)

    def is_visible(self, locator: str) -> bool:
        """Check if an element is visible."""
        return self.page.locator(locator).is_visible()

    def take_screenshot(self, name: str = "screenshot") -> str:
        """Take a screenshot and return the file path."""
        path = take_screenshot(self.page, name)
        logger.info(f"Screenshot saved: {path}")
        return path

    def get_title(self) -> str:
        """Return the current page title."""
        return self.page.title()

    def expect_visible(self, locator: str) -> None:
        """Assert that an element is visible."""
        expect(self.page.locator(locator)).to_be_visible()