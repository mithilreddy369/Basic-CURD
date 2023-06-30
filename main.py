from connection import connect_to_database
from operations import *


def main():
    # Connect to the database
    db = connect_to_database()

    while True:
        print("1. Insert document")
        print("2. Find documents")
        print("3. Update Age")
        print("4. Delete documents")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            document = {"name": name, "age": age}
            insert_document(db, document)
        elif choice == "2":
            query = {}
            find_documents(db, query)
        elif choice == "3":
            query_name = input("Enter name to update: ")
            new_age = int(input("Enter new age: "))
            query = {"name": query_name}
            new_values = {"$set": {"age": new_age}}
            update_documents(db, query, new_values)
        elif choice == "4":
            query_name = input("Enter name to delete: ")
            query = {"name": query_name}
            delete_documents(db, query)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

    # Close the database connection
    db.client.close()


if __name__ == "__main__":
    main()
