import logging
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session", autouse=True)
def _configure_logging():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler(),
                  logging.FileHandler("logs/test_run.log", mode="w", encoding="utf-8")]
    )

@pytest.fixture(params=["chrome", "safari"])
def driver(request):
    browser = request.param
    logging.info(f"[SETUP] Start: {browser}")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        # Jeśli chcesz testować bez otwierania okna przeglądarki, dodaj:
        # options.add_argument("--headless=new")
        options.add_argument("--window-size=1280,800")
        drv = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                               options=options)

    elif browser == "safari":
        # Safari nie wymaga instalacji sterownika – działa natywnie na macOS
        try:
            drv = webdriver.Safari()
            drv.set_window_size(1280, 800)
        except Exception as e:
            pytest.skip(f"Nie można uruchomić SafariDriver: {e}")

    drv.implicitly_wait(3)
    yield drv
    logging.info(f"[TEARDOWN] Quit: {browser}")
    drv.quit()
