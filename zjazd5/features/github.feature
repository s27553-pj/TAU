Feature: GitHub

  Scenario: Wyszukiwanie repozytorium Selenium
    Given Otwieram stronę "https://github.com/search?q=selenium&type=repositories"
    Then Widzę na stronie tekst "SeleniumHQ/selenium"
    When Klikam link "SeleniumHQ/selenium"
    Then Adres URL zawiera "/SeleniumHQ/selenium"

  Scenario: Otwarcie strony About GitHub
    Given Otwieram stronę "https://github.com"
    When Przechodzę na stronę "/about"
    Then Adres URL zawiera "/about"
