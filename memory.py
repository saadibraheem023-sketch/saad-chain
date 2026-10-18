import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "data" / "memory.db"


def initialize_database():

    DB_PATH.parent.mkdir(exist_ok=True)

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            assistant_response TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_memory(user_message, assistant_response):

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO memories
        (user_message, assistant_response)
        VALUES (?, ?)
        """,
        (user_message, assistant_response)
    )

    connection.commit()
    connection.close()
def get_memory_text(limit=5):

    memories = get_recent_memories(limit)

    if not memories:
        return ""

    text = []

    for user_message, assistant_response in reversed(memories):

        text.append(
            f"User: {user_message}"
        )

        text.append(
            f"Assistant: {assistant_response}"
        )

    return "\n".join(text)


def get_recent_memories(limit=5):

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT user_message, assistant_response
        FROM memories
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )

    rows = cursor.fetchall()

    connection.close()

    return rows