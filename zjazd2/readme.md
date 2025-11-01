Scenariusze testowe

Scenariusz 1. Wikipedia- wyszukiwanie 

| Krok | Opis działania                               | Oczekiwany rezultat                         |
|------|----------------------------------------------|---------------------------------------------|
| 1    | Wejdź na stronę `https://www.wikipedia.org/` | Strona główna Wikipedii jest widoczna       |
| 2    | Wpisz w wyszukiwarkę frazę „Ragdoll”         | Pole przyjmuje tekst                        |
| 3    | Wciśnij Enter                                | Następuje przejście do strony artykułu      |
| 4    | Sprawdź tytuł strony                         | Nagłówek artykułu = „Ragdoll”               |
| 5    | Sprawdź treść artykułu                       | Widoczna sekcja tekstowa z treścią artykułu |

Scenarriusz 2. Wikipedia - zmiana języka artykułu

| Krok | Opis działania                                                   | Oczekiwany rezultat                                |
|------|------------------------------------------------------------------|----------------------------------------------------|
| 1    | Wejdź na stronę artykułu `https://en.wikipedia.org/wiki/Ragdoll` | Artykuł w języku angielskim jest widoczny          |
| 2    | Kliknij link „Polski” w panelu języków                           | Następuje przejście na polską wersję strony        |
| 3    | Sprawdź adres URL                                                | Adres zawiera `pl.wikipedia.org`                   |
| 4    | Sprawdź nagłówek artykułu                                        | Nagłówek zawiera słowo „Selenium” w języku polskim |

Scenariusz 3. GitHub - wyszukiwanie repozytorium selenium

| Krok | Opis działania                                                           | Oczekiwany rezultat                                                             |
| ---- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| 1    | Wejdź na stronę `https://github.com/search?q=selenium&type=repositories` | Strona wyników wyszukiwania GitHuba zostaje załadowana                          |
| 2    | Poczekaj, aż pojawią się wyniki wyszukiwania                             | Widoczna lista repozytoriów                                                     |
| 3    | Sprawdź, czy na liście znajduje się „SeleniumHQ/selenium”                | Repozytorium „SeleniumHQ/selenium” jest obecne na liście wyników                |
| 4    | Kliknij link do repozytorium „SeleniumHQ/selenium”                       | Następuje przejście do strony repozytorium                                      |
| 5    | Sprawdź adres URL oraz tytuł strony                                      | Adres zawiera `/SeleniumHQ/selenium`, a tytuł strony zawiera nazwę repozytorium |

Scenariusz 4. GitHub - wejście na stronę 'About'

| Krok | Opis działania                                            | Oczekiwany rezultat                                   |
| ---- | --------------------------------------------------------- | ----------------------------------------------------- |
| 1    | Otwórz stronę główną `https://github.com`                 | Widoczna strona główna GitHuba                        |
| 2    | Znajdź link „About” w nagłówku lub stopce                 | Link „About” jest widoczny lub dostępny do kliknięcia |
| 3    | Kliknij link „About” lub przejdź bezpośrednio na `/about` | Następuje przejście na stronę informacyjną GitHuba    |
| 4    | Sprawdź adres URL                                         | Adres zawiera `/about`                                |
| 5    | Sprawdź tytuł strony                                      | Tytuł zawiera słowo „About” lub „GitHub”              |

