from app.main import app
from fastapi.testclient import TestClient
import psycopg2
from config.settings import settings
from config.database import connect_to_database

client = TestClient(app)

def cleanup_database():
    conn, cursor = connect_to_database()

    try:
        cursor.execute("DELETE FROM urls WHERE original_url LIKE '%example.com%'")
        conn.commit()
    except Exception as e:
        print(f"Error during cleanup: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def test_get_home():
    response = client.get('/')
    assert response.status_code == 200

def test_post_shorten():
    response = client.post('/shorten', json={
        "original_url": "https://www.example.com"
    })

    assert response.status_code == 200
    data = response.json()
    assert "shortened_url" in data
    cleanup_database()

def test_redirect_to_url():
    response = client.post('/shorten', json={
        "original_url": "https://www.example.com"
    })
    assert response.status_code == 200
    data = response.json()
    short_code = data["shortened_url"]

    response = client.get(f'/{short_code}')
    assert response.status_code == 200

    cleanup_database()