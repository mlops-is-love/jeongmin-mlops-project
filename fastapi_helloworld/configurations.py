import os

class DBConfigurations:
    postgres_username = os.getenv("POSTGRES_USER", "super_user")
    postgres_password = os.getenv("POSTGRES_PASSWORD", "su_password")
    postgres_port = int(os.getenv("POSTGRES_PORT", 2345))
    postgres_db = os.getenv("POSTGRES_DB", "test-db")
    postgres_server = os.getenv("POSTGRES_SERVER", "localhost")
    sql_alchemy_database_url = (
        f"postgresql://{postgres_username}:{postgres_password}@{postgres_server}:{postgres_port}/{postgres_db}"
    )

class APIConfigurations:
    title = os.getenv("API_TITLE", "Test DB")
    description = os.getenv("API_DESCRIPTION", "mlops study - fastapi hello world")
    version = os.getenv("API_VERSION", "0.1")
    header = "mlops-study"