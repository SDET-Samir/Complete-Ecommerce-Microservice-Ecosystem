import os
import sqlite3
import logging
import pytest

# Configure structured, enterprise-ready console logging output layouts
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s'
)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session", autouse=True)
def manage_database():
    """
    Manages the runtime testing database environment infrastructure.

    SETUP: Initializes a local SQLite architecture for host machine execution loops.
    TEARDOWN: Safely destroys local host state database files while respecting containerized sandboxes.
    """
    db_file = "ecommerce.db"

    is_containerized = os.path.exists("/.dockerenv")

    if not is_containerized:
        logger.info(
            "DevOps Environment: Host machine detected. Initializing SQL sandbox tables...")
        try:
            connection = sqlite3.connect(db_file)
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            """)
            cursor.execute(
                "INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)",
                ("samir", "secure123")
            )
            connection.commit()
        except sqlite3.Error as error:
            logger.error(f"Database setup failure occurred: {error}")
            raise
        finally:
            connection.close()
    else:
        logger.info(
            "DevOps Environment: Containerized sandbox detected. Delegating database state to service layers.")

    yield

    if not is_containerized:
        logger.info(
            "CI/CD Pipeline: Testing complete. Cleaning up host sandbox database file...")
        if os.path.exists(db_file):
            try:
                os.remove(db_file)
            except OSError as error:
                logger.warning(
                    f"Could not remove temporary database file: {error}")
    else:
        logger.info(
            "CI/CD Pipeline: Container testing complete. Retaining containerized database integrity bounds.")
