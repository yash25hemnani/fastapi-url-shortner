from fastapi import (FastAPI, HTTPException, Body)
from fastapi.responses import RedirectResponse
from config.database import connect_to_database
from config.generate_short_code import generate_short_code
from pydantic import BaseModel

class Url(BaseModel):
    original_url: str

app = FastAPI()

@app.get('/')
def home_view():
    """
    Home route for the URL Shortener API.

    Returns:
        str: A welcome message to confirm that the API is running.
    """

    return "Welcome to URL Shortner!"

@app.post("/shorten")
def shorten_url(url: Url):
    """
    Shortens a given original URL by generating a unique short code and storing it in the database.

    Args:
        url (Url): A Pydantic model containing the original URL to be shortened.

    Returns:
        dict: A dictionary with the generated short URL code.

    Raises:
        HTTPException: If an error occurs during database insertion, returns a 500 status code.
    """

    conn, cursor = connect_to_database()

    insert_query = """
        INSERT INTO urls (original_url, short_url)
        VALUES (%s, %s);
    """

    short_code = generate_short_code()

    data = (url.original_url, short_code)

    try:
        cursor.execute(insert_query, data)
        conn.commit()
        return {"shortened_url": short_code}


    except Exception as e:
        print(f"Error occurred: {e}")
        conn.rollback()
        raise HTTPException(status_code=500, detail="Error occurred while inserting data.")

    finally:
        cursor.close()
        conn.close()


@app.get("/{short_url}")
def redirect_to_url(short_url: str):
    """
    Redirects to the original URL based on the given short URL code.

    Args:
        short_url (str): The shortened URL code to be resolved.

    Returns:
        RedirectResponse: A redirect response to the original URL.

    Raises:
        HTTPException:
            - 404 if the short code is not found.
            - 500 if a database error occurs.
    """

    conn, cursor = connect_to_database()

    select_query = "SELECT original_url FROM urls WHERE short_url = %s"

    try:
        cursor.execute(select_query, (short_url,))
        result = cursor.fetchone()

        if result is None:
            raise HTTPException(status_code=404, detail="Short code not found.")

        original_url = result[0]
        return RedirectResponse(url=original_url)

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error occurred while redirecting to original URL.")

    finally:
        cursor.close()
        conn.close()