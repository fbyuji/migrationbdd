import mariadb
import pandas as pd
import pytest


DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "istore_db",
    "port": 3307  
}


def connect_db():
    return mariadb.connect(**DB_CONFIG)

# Récupérer les data
def fetch_data(query):
    conn = connect_db()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# TEST 1 : Vérifier le nombre d'articles
def test_articles_count():
    query = "SELECT COUNT(*) as count FROM articles;"
    result = fetch_data(query)
    assert result["count"][0] > 0, "Erreur : Aucun article trouvé !"

# TEST 2 : Vérifier l'intégrité des données avec NAME
def test_articles_data():
    query = "SELECT id, NAME, price FROM articles ORDER BY id;"
    data = fetch_data(query)
    assert not data.isnull().values.any(), "Données corrompues (valeurs NULL détectées) !"

# TEST 3 : Vérifier la correspondance entre articles et inventories
def test_articles_inventory_relation():
    query = """
        SELECT a.id FROM articles a
        LEFT JOIN inventories i ON a.inventory_id = i.id
        WHERE a.inventory_id IS NOT NULL AND i.id IS NULL;
    """
    result = fetch_data(query)
    assert result.empty, "Erreur : Articles avec inventory_id inexistant dans inventories !"

if __name__ == "__main__":
    pytest.main()
