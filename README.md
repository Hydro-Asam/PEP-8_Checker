# PEP-8_Checker
Apka sprawdza kod Pythona pod kątem PEP 8 w przeglądarce, dzieli uwagi na błędy i ostrzeżenia, podpowiada przyczynę i poprawkę.

Funkcje: Edytor z numerowaniem linii, liczniki błędów/ostrzeżeń i znaków, limit długości kodu, przycisk czyszczenia oraz linki do opisów reguł.

Uruchomienie lokalnie(terminal linux):

Utwórz środowisko poleceniem python3 -m venv .venv 

Włącz środowisko source .venv/bin/activate 

Przy aktywnym (.venv) wpisz pip install -r requirements.txt 

Wpisz python app.py (lub python3 app.py, jeśli skrót python nie jest podpięty) 

wejdź na http://127.0.0.1:5000

(zatrzymanie serwera Ctrl + C)

app.py odpala serwer w trybie debug=True (dobre do lokalnego programowania i podglądu błędów, ale nie do wystawiania na otwartą produkcję)

