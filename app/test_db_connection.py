from config.database import connect_to_database
import pytest

def test_connection():
    """
    Test the database connection to PostgreSQL.

    Assertions:
        - Ensures that a version is returned from the database.
        - Confirms that the version string contains the word "PostgreSQL".

    Raises:
        pytest.fail: If any exception occurs during the database operation, the test fails.
    """

    conn, cursor = connect_to_database()

    query_sql = 'SELECT VERSION()'
    try:
        cursor.execute(query_sql)

        version = cursor.fetchone()[0]

        print("PostgreSQL Version:", version)

        assert version is not None, "No version info returned from PostgreSQL"
        assert "PostgreSQL" in version, f"Unexpected version format: {version}"

    except Exception as e:
        pytest.fail(f"Error while connecting to PostgreSQL: {e}")
