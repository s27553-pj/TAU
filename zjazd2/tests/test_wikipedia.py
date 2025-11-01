import logging

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_wikipedia_search_article(driver):
    log = logging.getLogger()
    log.info("Wyszukiwanie artykułu 'Ragdoll'")

    driver.get("https://en.wikipedia.org/")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "searchInput"))
    )

    log.info("Strona główna wikipedii załadowana")

    search = driver.find_element(By.ID, "searchInput")
    search.clear()
    search.send_keys("Ragdoll")
    search.send_keys(Keys.ENTER)
    log.info("Wysłano zapytanie wyszukiwania")

    heading =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "firstHeading"))
    )
    assert "Ragdoll" in heading.text

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "mw-content-text"))
    )
    log.info("Artykuł i treść widoczne")

    def test_wikipedoa_switch_language(driver):
        log = logging.getLogger()
        log.info("zmiana języka artykułu na polski")

        driver.get("https://en.wikipedia.org/wiki/Ragdoll")

        heading_en = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "firstHeading"))
        )
        assert "Ragdoll" in heading_en.text
        log.info("Artykuł po angielsku otarty")

        polish_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[lang="pl"]'))
        )

        polish_link.click()
        log.info("Kliknięto link języka Polskiego")
        WebDriverWait(driver, 10).until(EC.url_contains("pl.wikipedia.org"))
        heading_pl = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "firstHeading"))
        )
        assert "Selenium" in heading_pl.text
        log.info("[ASSERT] Jesteśmy na pl.wikipedia.org, nagłówek OK, lang=pl")

