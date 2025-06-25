from App.db.database import get_connection

def authenticate_user(user_id: str, password: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT * FROM logindetails
    WHERE userId = %s
    """
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result
