-----------------czytajka: know-how:
-data_handler.py: Zawiera funkcje do pobierania danych z API, zapisu do  CSV lub MongoDB oraz ładowania danych.
-analysis.py: Zawiera funkcje do analizy danych, np. obliczanie średniej GDP per capita czy znajdowanie maksymalnych wartości.
-visualization.py: Zawiera funkcje do tworzenia wizualizacji, np. wykresów liniowych i słupkowych.
-main.py: Skrypt główny, który łączy wszystkie etapy: pobieranie, zapis, analizę i wizualizację.
-requirements.txt: lista zależności, takich jak requests, pymongo, pandas, matplotlib (potrzebne do zainstalowania)
------------------
Projekt wymaga doinstalowania:
requests
pymongo
pandas
matplotlib

które zostały określone w pliku requirements.txt . Możliwość szybkiej instalacji za pomocą komendy pip install -r requirements.txt
-------------------
Projekt jest uruchamiany za pomocą skryptu main.py, z opcją wyboru metody zapisu: CSV/MongoDB(w przypadku konfiguracji na porcie 27017)

W pliku data_handler.py wykorzystywane jest api: https://api.worldbank.org/v2/country/all/indicator/NY.GDP.PCAP.CD?date=2010:2020&format=json&per_page=10000 zawierające GDP per capita

aby uruchomić project:

w przypadaku CSV:
python main.py --storage csv
-pobierze csv z https://api.worldbank.org/v2/country/all/indicator/NY.GDP.PCAP.CD?date=2010:2020&format=json&per_page=10000 i zaloguje plik csv w folderze projektu
-następnie wyświetli 2 wykresy:
*nr 1 : wykres przedstawiający się zmieniające się PKB Stanów Zjednoczonych w latach 2010-2020
*nr 2 : wykres porównujący PKB Chin, Niemiec, Japonii i Stanów zjednoczonych w 2020 r.

W przypadku skonfigurowanego mongoDB 
Komenda:
python main.py --storage mongodb
-analogicznie projekt wyświetli 2 wykresy, lecz dane pierw zgromadzi w lokalnym mongoDB

---------
Wykresy (dowód :D) są zawarte w osobnych plikach PNG znajdujących się w projekcie:
1. Wykres nr1
2. Wykres nr2
3. Command line
