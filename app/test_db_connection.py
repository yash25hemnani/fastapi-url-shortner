from config.database import connect_to_database
import pytest

def test_connection():
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
