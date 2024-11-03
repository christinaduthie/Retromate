from utils.iris_connection import get_iris_connection

def get_chat_history():
    connection = get_iris_connection()
    if connection is None:
        print("Failed to connect to IRIS")
        return []

    chat_history = []

    try:
        print("Connected to IRIS in get_chat_history")

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # SQL query to fetch chat history
        query = "SELECT UserQuery, GeneratedText FROM SQLUser.TherapistData ORDER BY ID ASC"
        print("Executing query:", query)  # Debugging line

        # Execute the query
        cursor.execute(query)

        # Fetch all rows and process them
        rows = cursor.fetchall()
        for row in rows:
            print(f"Row fetched: UserQuery={row[0]}, GeneratedText={row[1]}")
            chat_history.append({"sender": "user", "text": row[0]})
            chat_history.append({"sender": "bot", "text": row[1]})

        print("Complete chat history:", chat_history)
        return chat_history

    except Exception as e:
        print("Error retrieving chat history:", e)
        return []

    finally:
        cursor.close()
        connection.close()


# Run the test
if __name__ == "__main__":
    chat_history = get_chat_history()
    print("Final chat history:", chat_history)
