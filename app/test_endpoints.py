from app.main import app
from fastapi.testclient import TestClient
import psycopg2
from config.settings import settings
from config.database import connect_to_database

client = TestClient(app)

def cleanup_database():
    """
    Cleans up test data from the database.

    Deletes any rows from the `urls` table where the original URL contains 'example.com'.
    Used to ensure a clean slate after running tests that insert test URLs.

    Handles exceptions gracefully and ensures the connection is properly closed.
    """

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
    """
    Tests the root ("/") endpoint of the FastAPI application.

    Sends a GET request and asserts that the response status code is 200,
    indicating that the server is running and returning the welcome message.
    """

    response = client.get('/')
    assert response.status_code == 200

def test_post_shorten():
    """
    Tests the '/shorten' POST endpoint.

    Sends a sample URL in the request body to be shortened.
    Verifies that the response contains a 'shortened_url' and has a status code of 200.

    Performs cleanup by deleting the inserted test URL after the test.
    """

    response = client.post('/shorten', json={
        "original_url": "https://www.example.com"
    })

    assert response.status_code == 200
    data = response.json()
    assert "shortened_url" in data
    cleanup_database()

def test_redirect_to_url():
    """
    Tests the redirection logic of the application.

    Steps:
    1. Sends a POST request to '/shorten' to generate a short code.
    2. Sends a GET request using the short code to test redirection.

    Asserts:
        - The initial POST returns a 200 status and a short code.
        - The GET request with the short code also returns 200.

    Cleans up the test entry from the database afterward.
    """

    response = client.post('/shorten', json={
        "original_url": "https://www.example.com"
    })
    assert response.status_code == 200
    data = response.json()
    short_code = data["shortened_url"]

    response = client.get(f'/{short_code}')
    assert response.status_code == 200

    cleanup_database()