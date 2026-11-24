PEP8_ADVICE: dict[str, dict[str, str]] = {
    "E111": {
        "why": (
            "W Pythonie wcięcia definiują bloki kodu. PEP 8 zaleca 4 spacje "
            "na poziom, żeby kod był równy i czytelny dla każdego."
        ),
        "fix": "Użyj wielokrotności 4 spacji na wcięcie (zamiast np. 2 albo 6 spacji).",
    },
    "E117": {
        "why": (
            "Linia ma większe wcięcie, niż wynika to ze struktury bloków – "
            "łatwo wtedy pomylić, do jakiego bloku należy."
        ),
        "fix": "Zmniejsz wcięcie tej linii do właściwego poziomu (zwykle wielokrotność 4 spacji).",
    },
    "E201": {
        "why": (
            "Spacja zaraz po otwierającym nawiasie '(' wygląda jak literówka "
            "i utrudnia szybkie skanowanie wzrokiem."
        ),
        "fix": "Usuń spację bezpośrednio po '(' — napisz np. funkcja(x, y).",
    },
    "E202": {
        "why": "Spacja tuż przed zamykającym nawiasem ')' zaburza przejrzystość wyrażeń i nawiasów.",
        "fix": "Usuń spację bezpośrednio przed ')' — napisz np. funkcja(x, y).",
    },
    "E225": {
        "why": (
            "Brak spacji wokół operatorów (np. '=', '+', '-', '==') sprawia, "
            "że wyrażenia zlewają się w jedną całość."
        ),
        "fix": "Dodaj po jednej spacji przed i za operatorem, np. z = x + y.",
    },
    "E231": {
        "why": (
            "Brak spacji po przecinku utrudnia szybkie odróżnienie kolejnych "
            "argumentów lub elementów listy."
        ),
        "fix": "Wstaw spację po przecinku, np. def funkcja(x, y):",
    },
    "E112": {
        "why": (
            "Po nagłówku bloku (np. 'if', 'for' lub 'def' zakończonym ':') "
            "w Pythonie musi pojawić się wcięty kod – inaczej składnia jest niepełna."
        ),
        "fix": (
            "Dodaj wcięty blok kodu (zwykle o 4 spacje) pod linią z dwukropkiem "
            "lub wpisz tymczasowo 'pass', jeśli blok ma być pusty."
        ),
    },
    "E501": {
        "why": (
            "PEP 8 zaleca maksymalnie 79 znaków w linii, aby kod był czytelny "
            "bez przewijania na boki i wygodny do porównywania zmian."
        ),
        "fix": (
            "Podziel długą linię na krótsze – np. łamiąc wyrażenie w nawiasach, "
            "łącząc dłuższe napisy lub rozbijając na zmienne pośrednie."
        ),
    },
    "W292": {
        "why": (
            "Brak znaku nowej linii na samym końcu pliku bywa kłopotliwy dla "
            "narzędzi wiersza poleceń i systemów kontroli wersji (np. Git)."
        ),
        "fix": "Wciśnij Enter na końcu ostatniej linii, aby zostawić pustą linię na końcu kodu.",
    },
    "E101": {
        "why": (
            "Mieszanie tabulatorów i spacji we wcięciach to prosta droga "
            "do 'TabError' albo rozjechania bloków kodu w innym edytorze."
        ),
        "fix": (
            "Zamień tabulatory na spacje i trzymaj się konsekwentnie 4 spacji "
            "na poziom wcięcia."
        ),
    },
    "E211": {
        "why": (
            "Spacja tuż przed nawiasem przy wywołaniu funkcji wygląda jak "
            "błąd składni albo przypadkowe kliknięcie spacji."
        ),
        "fix": "Usuń spację przed '(' — napisz np. policz(x), a nie policz (x).",
    },
    "E251": {
        "why": (
            "Przy argumentach funkcji i wartościach domyślnych PEP 8 zaleca "
            "brak spacji wokół '=' – w przeciwieństwie do zwykłego przypisania."
        ),
        "fix": "Napisz np. def funkcja(x=10): zamiast def funkcja(x = 10):.",
    },
    "E261": {
         "why": (
            "Komentarz dopisany na końcu linii z kodem wymaga co najmniej "
            "dwóch spacji odstępu, żeby wyraźnie oddzielić go od instrukcji."
        ),
        "fix": "Wstaw co najmniej dwie spacje przed '#', np. x = 1  # komentarz.",
    },
    "E262": {
        "why": (
            "Pojedyncza spacja zaraz po znaku '#' sprawia, że komentarz jest "
            "łatwiejszy do przeczytania niż zbity blok tekstu."
        ),
        "fix": "Dodaj jedną spację po '#', np. # TODO: poprawić warunek.",
    },
    "E302": {
        "why": (
            "PEP 8 wymaga dwóch pustych linii przed i po funkcjach oraz klasach "
            "najwyższego poziomu, żeby oddzielić od siebie większe bloki."
        ),
        "fix": "Dodaj puste linie tak, aby między funkcjami/klasami były dwie puste linie.",
    },
    "E303": {
        "why": (
            "Zbyt wiele pustych linii z rzędu rozciąga kod pionowo i zmniejsza "
            "jego czytelność na ekranie."
        ),
        "fix": "Usuń nadmiarowe puste linie (zwykle wystarczą 1 lub 2).",
    },
    "W191": {
        "why": (
            "Wcięcie zawiera tabulator ('\\t'), którego szerokość może różnić się "
            "między edytorami i terminalami."
        ),
        "fix": "Zamień tabulatory na spacje (4 spacje na poziom wcięcia).",
    },
    "W291": {
        "why": (
            "Zbędne spacje na końcu linii to tzw. 'trailing whitespace' – "
            "często zaśmiecają diffy w Git i łatwo je przeoczyć."
        ),
        "fix": "Usuń spacje znajdujące się na końcu tej linii.",
    },
    "W293": {
        "why": (
            "Pusta linia nie powinna zawierać niewidocznych spacji – to "
            "niepotrzebny szum w pliku źródłowym."
        ),
        "fix": "Usuń spacje z tej pustej linii, tak aby była całkiem pusta.",
    },
    "W391": {
        "why": (
            "Nadmiarowe puste linie na samym końcu pliku nie wnoszą treści, "
            "a potrafią psuć porządek przy łączeniu plików."
        ),
        "fix": "Usuń nadmiarowe puste linie na końcu kodu (zostaw najwyżej jedną).",
    },
    "W503": {
        "why": (
            "Klasyczny PEP 8 preferuje łamanie długich wyrażeń przed operatorem "
            "binarnym, żeby od razu było widać, co robi dany wiersz."
        ),
        "fix": "Przenieś operator binarny (np. '+' lub 'and') na początek kolejnej linii.",
    },
    "W504": {
        "why": (
            "Łamanie linii po operatorze binarnym jest w tym stylu uznawane za "
            "mniej czytelne niż przeniesienie operatora do nowej linii."
        ),
        "fix": "Rozważ przeniesienie operatora na początek następnej linii zamiast zostawiać go na końcu.",
    },
    "E122": {
        "why": (
            "Linia kontynuacji wyrażenia nie ma wcięcia albo jest cofnięta "
            "zbyt mocno w lewo, przez co trudno od razu zobaczyć, że należy "
            "do rozpoczętej wcześniej instrukcji."
        ),
        "fix": (
            "Dodaj odpowiednie wcięcie do linii kontynuacji (np. wcięcie "
            "wiszące o 4 spacje albo wyrównanie do otwierającego nawiasu)."
        ),
    },
    "E131": {
        "why": (
            "Przy wcięciu wiszącym (gdy po nawiasie od razu przechodzisz do "
            "nowej linii) wszystkie kolejne linie powinny mieć ten sam poziom "
            "wcięcia – nierówne linie psują przejrzystość."
        ),
        "fix": (
            "Wyrównaj wszystkie linie wcięcia wiszącego na tę samą liczbę "
            "spacji (zwykle o 4 spacje więcej niż początek instrukcji)."
        ),
    },
    "E901": {
        "why": (
            "Kod zawiera błąd składni lub wcięć (np. niedomknięty nawias, "
            "brak dwukropka albo niepoprawną konstrukcję), więc parser nie "
            "może poprawnie odczytać struktury programu."
        ),
        "fix": (
            "Najpierw popraw błąd składni wskazany w komunikacie (domknij "
            "nawiasy i cudzysłowy, sprawdź dwukropki i wcięcia), aby kod "
            "poprawnie się parsował, a potem dopieść styl PEP 8."
        ),
    },
    "E203": {
        "why": (
            "Spacja przed dwukropkiem, średnikiem lub przecinkiem wygląda jak "
            "przypadkowe kliknięcie i rozbija czytelny zapis."
        ),
        "fix": "Usuń spację przed ':', ';' lub ',', np. lista[1:3] albo funkcja(a, b).",
    },
    "E221": {
        "why": (
            "Wielokrotne spacje przed operatorem zwykle nie poprawiają "
            "czytelności i tworzą nierówny odstęp w linii."
        ),
        "fix": "Zostaw dokładnie jedną spację przed operatorem, np. x = 1 + 2.",
    },
    "E222": {
        "why": (
            "Wielokrotne spacje po operatorem zaburzają spójność formatowania "
            "w całym pliku."
        ),
        "fix": "Zostaw dokładnie jedną spację za operatorem, np. x = 1 + 2.",
    },
    "E226": {
        "why": (
            "Przy operatorach arytmetycznych (np. '+', '-', '*', '/') brak "
            "spacji sprawia, że wyrażenie wygląda na zbite i mniej czytelne."
        ),
        "fix": "Dodaj po jednej spacji wokół operatora arytmetycznego, np. a * b + c.",
    },
    "E227": {
        "why": (
            "Operatory bitowe (np. '&', '|', '^', '<<', '>>') w wyrażeniach "
            "łatwiej odczytać, gdy są oddzielone spacjami."
        ),
        "fix": "Dodaj spacje wokół operatora bitowego, np. maska = flagi | 0x01.",
    },
    "E228": {
        "why": (
            "W starszym formatowaniu przez '%' brak spacji wokół operatora "
            "zmniejsza przejrzystość napisu."
        ),
        "fix": "Wstaw spację przed i po '%', np. 'wartość: %s' % wynik.",
    },
    "E241": {
        "why": (
            "Zbyt wiele spacji po przecinku wygląda na ręczne wyrównywanie "
            "kolumn, które w PEP 8 jest odradzane."
        ),
        "fix": "Zostaw pojedynczą spację po przecinku, np. [1, 2, 3].",
    },
    "E271": {
        "why": (
            "Nadmiarowe spacje po słowie kluczowym (np. 'if', 'return', 'in') "
            "są zbędnym szumem w kodzie."
        ),
        "fix": "Usuń dodatkowe spacje po słowie kluczowym, zostawiając jedną.",
    },
    "E272": {
        "why": (
            "Nadmiarowe spacje przed słowem kluczowym rozjeżdżają rytm czytania "
            "linii."
        ),
        "fix": "Usuń dodatkowe spacje przed słowem kluczowym.",
    },
    "E301": {
        "why": (
            "Metody wewnątrz klasy warto oddzielać pojedynczą pustą linią, "
            "żeby nie zlewały się ze sobą."
        ),
        "fix": "Dodaj jedną pustą linię między metodami w klasie.",
    },
    "E401": {
        "why": (
            "Kilka różnych modułów zaimportowanych w jednej linii po przecinku "
            "jest mniej czytelne niż osobne linie importu."
        ),
        "fix": "Rozbij importy na osobne linie, np. 'import os' oraz 'import sys'.",
    },
    "E402": {
        "why": (
            "Import umieszczony niżej w pliku (po innym kodzie) utrudnia "
            "szybkie zorientowanie się, od czego zależy moduł."
        ),
        "fix": (
            "Przenieś import na górę pliku – tuż po komentarzach nagłówkowych "
            "i docstringu modułu (chyba że wymagany jest inny układ)."
        ),
    },
    "E701": {
        "why": (
            "Wrzucanie całego bloku kodu w tej samej linii po dwukropku "
            "(np. 'if x: y = 1') pogarsza czytelność."
        ),
        "fix": "Przenieś instrukcję do nowej linii z wcięciem 4 spacji pod ':'.",
    },
    "E702": {
        "why": (
            "Łączenie kilku instrukcji w jednej linii średnikiem ';' to styl "
            "niezalecany w Pythonie i utrudnia przeglądanie zmian."
        ),
        "fix": "Rozdziel instrukcje na osobne linie zamiast używać średnika.",
    },
    "E711": {
        "why": (
            "Porównywanie do 'None' przez '==' lub '!=' jest mniej bezpieczne "
            "i mniej idiomatyczne niż użycie 'is' albo 'is not'."
        ),
        "fix": "Zamień '== None' na 'is None', a '!= None' na 'is not None'.",
    },
    "E712": {
        "why": (
            "Porównywanie wartości logicznej przez '== True' lub '== False' "
            "jest rozwlekłe i mniej czytelne niż bezpośredni warunek."
        ),
        "fix": "Użyj 'if warunek:' zamiast 'if warunek == True:' lub 'if not warunek:'.",
    },
    "E713": {
        "why": (
            "Zapis 'not x in y' jest mniej naturalny w języku angielskim/Pythonie "
            "niż 'x not in y'."
        ),
        "fix": "Zmień kolejność na 'x not in y'.",
    },
    "E714": {
        "why": (
            "Zapis 'not x is y' jest trudniejszy w odbiorze niż 'x is not y'."
        ),
        "fix": "Zmień kolejność na 'x is not y'.",
    },
    "E721": {
        "why": (
            "Sprawdzanie typu przez 'type(x) == ...' bywa zawodne przy "
            "dziedziczeniu – lepiej użyć 'isinstance()'."
        ),
        "fix": "Zamiast 'type(x) == Klasa' użyj 'isinstance(x, Klasa)'.",
    },
    "E722": {
        "why": (
            "Gołe 'except:' łapie absolutnie wszystko – w tym przerwanie "
            "programu przez użytkownika (Ctrl+C) czy błędy systemowe."
        ),
        "fix": (
            "Wskaż konkretny typ wyjątku, np. 'except ValueError:' lub "
            "'except Exception:'."
        ),
    },
}

DEFAULT_ADVICE = {
    "why": "Ta reguła pomaga utrzymać jednolity styl kodu w całym projekcie zgodnie z PEP 8.",
    "fix": "Sprawdź komunikat błędu i dopasuj formatowanie linii do wytycznych PEP 8.",
}
