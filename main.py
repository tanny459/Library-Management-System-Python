from book import Book
from user import User
from book_manager import BookManager
from user_manager import UserManager

def main():
    # Initialize BookManager and UserManager objects
    book_manager = BookManager()
    user_manager = UserManager()

    # Load data from storage
    book_manager.load_books_from_storage()
    user_manager.load_users_from_storage()

    # Main loop for user interaction
    while True:
        
        # Display Menu option
        print("╔══════════════════════════════════════╗")
        print("║            Library Management        ║")
        print("║                System                ║")
        print("╠══════════════════════════════════════╣")
        print("║ 1.  Add Book                         ║")
        print("║ 2.  Add User                         ║")
        print("║ 3.  Update Book                      ║")
        print("║ 4.  Update User                      ║")
        print("║ 5.  Delete Book                      ║")
        print("║ 6.  Delete User                      ║")
        print("║ 7.  Check-out Book                   ║")
        print("║ 8.  Check-in Book                    ║")
        print("║ 9.  List Books                       ║")
        print("║ 10. List Users                       ║")
        print("║ 11. Search Books                     ║")
        print("║ 12. Search Users                     ║")
        print("║ 13. Exit                             ║")
        print("╚══════════════════════════════════════╝")

        # Get user choice
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a new book
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book_manager.add_book(Book(title, author, isbn))
            print("*****************************************************")
            print("New book added successfully.")
            print("*****************************************************")
            
        elif choice == "2":
            # Add a new user
            name = input("Enter user's name: ")
            user_id = input("Enter user ID: ")
            using_books = input("Enter if user is using some book")
            user_manager.add_user(User(name, user_id, using_books))
            print("*****************************************************")
            print("New user added successfully.")
            print("*****************************************************")

        elif choice == "3":
            # Update book information
            isbn = input("Enter ISBN of the book to update: ")
            title = input("Enter new title (leave empty to keep existing): ")
            author = input("Enter new author (leave empty to keep existing): ")
            new_book_info = {'title': title, 'author': author}
            if book_manager.update_book(isbn, new_book_info):
                print("*****************************************************")
                print("Book updated successfully.")
                print("*****************************************************")
            else:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("Failed to update the book(Wrong ISBN number)s.")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                
        elif choice == "4":
            # Update user information
            user_id = input("Enter user ID to update: ")
            name = input("Enter new name (leave empty to keep existing): ")
            new_user_info = {'name': name}
            if user_manager.update_user(user_id, new_user_info):
                print("*****************************************************")
                print("User updated successfully.")
                print("*****************************************************")
            else:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("Failed to update the user.")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                
        elif choice == "5":
            # Delete a book
            isbn = input("Enter ISBN of the book to delete: ")
            if book_manager.delete_book(isbn):
                print("*****************************************************")
                print("Book deleted successfully.")
                print("*****************************************************")
            else:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("Failed to delete the book.")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                
        elif choice == "6":
            # Delete a user
            user_id = input("Enter user ID to delete: ")
            if user_manager.delete_user(user_id):
                print("*****************************************************")
                print("User deleted successfully.")
                print("*****************************************************")
            else:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("Failed to delete the user.")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                
        elif choice == "7":
            # Check out a book
            isbn = input("Enter ISBN of the book to check out: ")
            user_id = input("Enter user ID: ")  
            if book_manager.checkout_book(isbn, user_id, user_manager):  
                print("*****************************************************")
                print("Book checked out successfully.")
                print("*****************************************************")
            else:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("Failed to check out the book.")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                
        elif choice == "8":
            # Check in a book
            isbn = input("Enter ISBN of the book to check in: ")
            user_id = input("Enter user ID: ")
            if book_manager.checkin_book(isbn, user_id, user_manager):
                print("*****************************************************")
                print("Book checked in successfully.")
                print("*****************************************************")
            else:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("Failed to check in the book.")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                
        elif choice == "9":
            # List all books
            book_manager.list_books()

        elif choice == "10":
            # List all users
            user_manager.list_users()
                
        elif choice == "11":
            # Search for books
            keyword = input("Please provide Title or Author Infromation to search books: ")
            books = book_manager.search_books(keyword)
            if books:
                for book in books:
                    print("*****************************************************")
                    print(book)
                    print("*****************************************************")
            else:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("No matching books found.")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                
        elif choice == "12":
            # Search for users
            keyword = input("Please provide Name of the user to search: ")
            users = user_manager.search_users(keyword)
            if users:
                for user in users:
                    print("*****************************************************")
                    print(user)
                    print("*****************************************************")
            else:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("No matching users found.")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                
        elif choice == "13":
            # Save data and exit
            book_manager.save_books_to_storage()
            user_manager.save_users_to_storage()
            print("*****************************************************")
            print("Thanks for using Library Manager:):):)...")
            print("Do visit us agin happy User:):):)...")
            print("*****************************************************")
            break
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Invalid choice. Please try again.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


if __name__ == "__main__":
    main()
