import psycopg2


DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "saad_ai",
    "user": "postgres",
    "password": "YOUR_PASSWORD"
}


def get_connection():

    return psycopg2.connect(
        **DB_CONFIG
    )


def get_vehicle_count():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM vehicles"
    )

    result = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return str(result)