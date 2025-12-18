Feature: Wikipedia

  Scenario: Wyszukiwanie artykułu Ragdoll
    Given Otwieram stronę "https://www.wikipedia.org/"
    When Wyszukuję frazę "Ragdoll"
    Then Widzę nagłówek artykułu "Ragdoll"

  Scenario: Zmiana języka artykułu na polski
    Given Otwieram stronę "https://en.wikipedia.org/wiki/Ragdoll"
    When Zmieniam język na "Polski"
    Then Adres URL zawiera "pl.wikipedia.org"
