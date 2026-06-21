"""
Database module for Career Bridge AI.

Handles SQLite database operations including connection management,
table creation, and CRUD operations.
"""

import sqlite3
import os
from pathlib import Path
from typing import Any, Optional
import logging

from config import DB_PATH, DB_TIMEOUT

logger = logging.getLogger(__name__)


class DatabaseManager:
    """
    Manages SQLite database connections and operations.

    Provides connection pooling, table creation, and CRUD operations
    for Career Bridge AI.
    """

    def __init__(self, db_path: Path = DB_PATH) -> None:
        """
        Initialize database manager.

        Args:
            db_path: Path to SQLite database file.

        TODO: Implement database initialization.
        """
        database_url = os.getenv("DATABASE_URL", "").strip()
        if database_url.startswith("sqlite:///"):
            self.db_path = Path(database_url.replace("sqlite:///", "", 1))
        elif database_url:
            logger.warning("DATABASE_URL is set but this lightweight deployment build supports SQLite only. Using local SQLite fallback.")
            self.db_path = db_path
        else:
            self.db_path = db_path

        self.available = False
        try:
            self.db_path.parent.mkdir(parents=True, exist_ok=True)
            self.create_tables()
            self.available = True
        except Exception as exc:
            logger.error("Database initialization failed; continuing without persistent storage: %s", exc)

    def get_connection(self) -> sqlite3.Connection:
        """
        Get a database connection.

        Returns:
            sqlite3.Connection: Database connection object.

        TODO: Implement connection retrieval with timeout.
        """
        try:
            conn = sqlite3.connect(str(self.db_path), timeout=DB_TIMEOUT)
            conn.row_factory = sqlite3.Row
            return conn
        except sqlite3.Error as e:
            logger.error(f"Database connection error: {e}")
            raise

    def close_connection(self, connection: sqlite3.Connection) -> None:
        """
        Close a database connection.

        Args:
            connection: Connection to close.

        TODO: Implement connection closing.
        """
        try:
            if connection:
                connection.close()
        except sqlite3.Error as e:
            logger.error(f"Error closing connection: {e}")

    def create_tables(self) -> None:
        """
        Create all required database tables.

        TODO: Implement table creation for:
            - users
            - resumes
            - career_recommendations
            - scholarship_recommendations
            - government_schemes
            - opportunities
            - learning_roadmaps
        """
        tables_sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            education_level TEXT,
            experience_years INTEGER,
            state TEXT,
            annual_income REAL,
            category TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        
        CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            filename TEXT NOT NULL,
            filepath TEXT NOT NULL,
            extracted_text TEXT,
            ats_score REAL,
            skills TEXT,
            education TEXT,
            experience TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        
        CREATE TABLE IF NOT EXISTS career_recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            career_name TEXT NOT NULL,
            match_score REAL,
            salary_range TEXT,
            growth_potential TEXT,
            skills_needed TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        
        CREATE TABLE IF NOT EXISTS scholarship_recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            scholarship_name TEXT NOT NULL,
            award_amount REAL,
            eligibility_status TEXT,
            application_deadline TEXT,
            match_score REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        
        CREATE TABLE IF NOT EXISTS government_schemes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            scheme_name TEXT NOT NULL,
            scheme_type TEXT,
            benefit TEXT,
            eligibility_status TEXT,
            application_deadline TEXT,
            match_score REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        
        CREATE TABLE IF NOT EXISTS opportunities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            opportunity_name TEXT NOT NULL,
            opportunity_type TEXT,
            stipend REAL,
            skills_required TEXT,
            match_score REAL,
            deadline TEXT,
            application_link TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        
        CREATE TABLE IF NOT EXISTS learning_roadmaps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            target_career TEXT NOT NULL,
            duration_months INTEGER,
            skills_to_develop TEXT,
            monthly_goals TEXT,
            resources TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        """

        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.executescript(tables_sql)
            conn.commit()
            logger.info("Database tables created successfully")
        except sqlite3.Error as e:
            logger.error(f"Error creating tables: {e}")
        finally:
            conn.close()

    def execute_query(self, query: str, params: tuple = (), fetch: bool = False) -> Optional[list[tuple]]:
        """
        Execute a database query.

        Args:
            query: SQL query string.
            params: Query parameters for parameterized queries.
            fetch: Whether to fetch and return results.

        Returns:
            List of tuples if fetch=True, None otherwise.

        TODO: Implement query execution with error handling.
        """
        if not self.available:
            logger.warning("Database unavailable. Query skipped.")
            return [] if fetch else None

        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, params)

            if fetch:
                results = cursor.fetchall()
                conn.close()
                return results
            else:
                conn.commit()
                conn.close()
                return None
        except sqlite3.Error as e:
            logger.error(f"Query execution error: {e}")
            conn.close()
            raise

    def insert(self, table: str, data: dict[str, Any]) -> int:
        """
        Insert a record into a table.

        Args:
            table: Table name.
            data: Dictionary of column names and values.

        Returns:
            ID of inserted record.

        TODO: Implement insert operation.
        """
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

        if not self.available:
            logger.warning("Database unavailable. Insert skipped for table %s.", table)
            return -1

        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, tuple(data.values()))
            conn.commit()
            last_id = cursor.lastrowid
            return last_id
        except sqlite3.Error as e:
            logger.error(f"Insert error: {e}")
            conn.rollback()
            raise
        finally:
            conn.close()

    def update(self, table: str, data: dict[str, Any], condition: str) -> int:
        """
        Update records in a table.

        Args:
            table: Table name.
            data: Dictionary of columns and new values.
            condition: WHERE clause condition.

        Returns:
            Number of rows updated.

        TODO: Implement update operation.
        """
        set_clause = ", ".join([f"{k} = ?" for k in data.keys()])
        query = f"UPDATE {table} SET {set_clause} WHERE {condition}"

        if not self.available:
            logger.warning("Database unavailable. Update skipped for table %s.", table)
            return 0

        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, tuple(data.values()))
            conn.commit()
            return cursor.rowcount
        except sqlite3.Error as e:
            logger.error(f"Update error: {e}")
            conn.rollback()
            raise
        finally:
            conn.close()

    def delete(self, table: str, condition: str) -> int:
        """
        Delete records from a table.

        Args:
            table: Table name.
            condition: WHERE clause condition.

        Returns:
            Number of rows deleted.

        TODO: Implement delete operation.
        """
        query = f"DELETE FROM {table} WHERE {condition}"

        if not self.available:
            logger.warning("Database unavailable. Delete skipped for table %s.", table)
            return 0

        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            return cursor.rowcount
        except sqlite3.Error as e:
            logger.error(f"Delete error: {e}")
            conn.rollback()
            raise
        finally:
            conn.close()

    def select(self, table: str, condition: Optional[str] = None) -> list[tuple]:
        """
        Select records from a table.

        Args:
            table: Table name.
            condition: Optional WHERE clause condition.

        Returns:
            List of records.

        TODO: Implement select operation.
        """
        query = f"SELECT * FROM {table}"
        if condition:
            query += f" WHERE {condition}"

        results = self.execute_query(query, fetch=True)
        return results if results else []


# Global database manager instance
_db_manager: Optional[DatabaseManager] = None


def get_db_manager() -> DatabaseManager:
    """
    Get or create global database manager instance.

    Returns:
        DatabaseManager: Global database manager.

    TODO: Implement singleton pattern.
    """
    global _db_manager
    if _db_manager is None:
        try:
            _db_manager = DatabaseManager()
        except Exception as exc:
            logger.error("Could not create database manager; using non-persistent fallback: %s", exc)
            _db_manager = DatabaseManager.__new__(DatabaseManager)
            _db_manager.db_path = DB_PATH
            _db_manager.available = False
    return _db_manager
