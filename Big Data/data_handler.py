import requests
import pandas as pd
from pymongo import MongoClient

def fetch_data(indicator='NY.GDP.PCAP.CD', date_range='2010:2020'):
    """Pobiera dane z API Banku Światowego."""
    url = f"https://api.worldbank.org/v2/country/all/indicator/{indicator}?date={date_range}&format=json&per_page=10000"
    response = requests.get(url)
    data = response.json()
    return data

def save_to_csv(data, filename='gdp_per_capita.csv'):
    """Zapisuje dane do pliku CSV."""
    records = []
    for item in data[1]:
        if item["value"] is not None:
            records.append({
                "country": item["country"]["value"],
                "year": int(item["date"]),
                "gdp_per_capita": float(item["value"])
            })
    df = pd.DataFrame(records)
    df.to_csv(filename, index=False)

def save_to_mongodb(data, db_name='world_bank_data', collection_name='gdp_per_capita'):
    """Zapisuje dane do bazy MongoDB."""
    client = MongoClient('localhost', 27017)
    db = client[db_name]
    collection = db[collection_name]
    collection.delete_many({})  # Wyczyść istniejące dane
    for item in data[1]:
        if item["value"] is not None:
            doc = {
                "country": item["country"]["value"],
                "year": int(item["date"]),
                "gdp_per_capita": float(item["value"])
            }
            collection.insert_one(doc)

def load_from_csv(filename='gdp_per_capita.csv'):
    """Ładuje dane z pliku CSV do Pandas DataFrame."""
    return pd.read_csv(filename)

def load_from_mongodb(db_name='world_bank_data', collection_name='gdp_per_capita'):
    """Ładuje dane z MongoDB do Pandas DataFrame."""
    client = MongoClient('localhost', 27017)
    db = client[db_name]
    collection = db[collection_name]
    data = list(collection.find())
    df = pd.DataFrame(data)
    df = df.drop('_id', axis=1)
    return df