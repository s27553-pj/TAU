import logging

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_github_search_selenium_repository(driver):
    log = logging.getLogger()
    log.info("Wyszukiwanie Selenium na Github")

    driver.get("https://github.com/search?q=selenium&type=repositories")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.TAG_NAME, "body"))
    )
    log.info("Strona wyszukiwania Github załadowana")
    repo_locator = (By.PARTIAL_LINK_TEXT, "SeleniumHQ/selenium")
    WebDriverWait(driver, 15).until(
       EC.element_to_be_clickable(repo_locator))

    assert "SeleniumHQ/selenium" in driver.page_source
    driver.find_element(*repo_locator).click()

    WebDriverWait(driver, 15).until(
        EC.url_contains("/SeleniumHQ/selenium"))
    title = driver.title.lower()
    assert "seleniumhq/selenium" in title
    log.info("Otwarto stronę repozytorium Selenium")

def test_github_open_about_page(driver):
    log = logging.getLogger()
    log.info("Sprawdzenie strony 'About' na GitHub")

    driver.get("https://github.com")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.TAG_NAME, "body"))
    )
    log.info("GitHub załadowany")

    clicked = False
    for locator in [
        (By.LINK_TEXT, "About"),
        (By.PARTIAL_LINK_TEXT, "About"),
        (By.CSS_SELECTOR, 'a[href="/about"]'),
    ]:
        try:
            link = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(locator)
            )
            link.click()
            clicked = True
            log.info("Kliknięto link 'About'")
            break
        except TimeoutException:
            continue

    if not clicked:
        log.warning("Nie znaleziono linku 'About', przejście bezpośrednio na /about")
        driver.get("https://github.com/about")

    WebDriverWait(driver, 10).until(EC.url_contains("/about"))
    title = driver.title.lower()
    assert "about" in title or "github" in title
    log.info("[ASSERT] Strona 'About' otwarta poprawnie – OK")

