import os
from datetime import datetime
from playwright.sync_api import Page

def take_screenshot(page: Page, name: str = "screenshot") -> str:
    """
    Take a full-page screenshot and return the saved path.
    Files are stored in the screenshots/ folder with a timestamp.
    """
    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = name.replace(" ", "_").replace("/", "_")
    path = os.path.join("screenshots", f"{safe_name}_{timestamp}.png")
    page.screenshot(path=path, full_page=True)
    return path