import mysql.connector

def create_database():
    try:
        # Connect to the MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host="localhost",  # Replace with your MySQL host
            user="root",       # Replace with your MySQL username
            password="PapaBabe56."  # Replace with your MySQL password
        )

        if connection.is_connected():
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # SQL query to create the database if it doesn't exist
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

            # Execute the query
            cursor.execute(create_db_query)

            # Print success message
            print("Database 'alx_book_store' created successfully!")

    except Exception as e:
        # Print error message if connection or query fails
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

# Run the function to create the database
create_database()