import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    # Application
    BASE_URL: str = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com")

    # Credentials
    ADMIN_USERNAME: str = os.getenv("ADMIN_USERNAME", "Admin")
    ADMIN_PASSWORD: str = os.getenv("ADMIN_PASSWORD", "admin123")
    EMPLOYEE_USERNAME: str = os.getenv("EMPLOYEE_USERNAME", "")
    EMPLOYEE_PASSWORD: str = os.getenv("EMPLOYEE_PASSWORD", "")

    # Browser
    BROWSER: str = os.getenv("BROWSER", "chromium")          # chromium | firefox | webkit
    HEADLESS: bool = os.getenv("HEADLESS", "true").lower() == "true"

    # Timeouts (ms)
    DEFAULT_TIMEOUT: int = int(os.getenv("DEFAULT_TIMEOUT", "10000"))
    NAVIGATION_TIMEOUT: int = int(os.getenv("NAVIGATION_TIMEOUT", "30000"))

    # Artifacts
    SCREENSHOT_ON_FAILURE: bool = os.getenv("SCREENSHOT_ON_FAILURE", "true").lower() == "true"
    VIDEO_ON_FAILURE: bool = os.getenv("VIDEO_ON_FAILURE", "true").lower() == "true"

# Singleton instance
settings = Settings()