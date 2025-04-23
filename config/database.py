import psycopg2
from config.settings import settings

def connect_to_database():
    """
    Connects to the PostgreSQL database and returns the connection and cursor.

    Returns:
        tuple: (conn, cursor) - Database connection and cursor objects.
    """

    conn = psycopg2.connect(
        host=settings.database_host,
        port=settings.database_port,
        user=settings.database_user,
        password=settings.database_password,
        dbname=settings.database_name,
        sslmode=settings.database_sslmode
    )

    cursor = conn.cursor()

    return conn, cursor


