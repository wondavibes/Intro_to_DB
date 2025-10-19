import mysql.connector


def create_database():
    try:
        # Establish a connection to the MySQL server
        db = mysql.connector.connect(host="localhost", user="root", password="12345")

        # Create a cursor object
        cursor = db.cursor()

        # Create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        # Commit the changes
        db.commit()

        # Close the cursor and connection
        cursor.close()
        db.close()

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as error:
        print(f"Failed to create database: {error}")


if __name__ == "__main__":
    create_database()
