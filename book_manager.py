from book import Book
from storage import CSVStorage

class BookManager:
    
    def __init__(self):
        """
        Initialize BookManager object.
        """
        self.books = []
        self.storage = CSVStorage("books.csv")

    def add_book(self, book):
        """
        Add a book to the book list and save it to storage.

        Args:
            book (Book): The book object to be added.
        """
        # Check if book is an instance of the Book class
        if isinstance(book, Book):  
            self.books.append(book)
            self.save_books_to_storage()
        else:
            print("Invalid book object. Please provide an instance of the Book class.")

    def update_book(self, book_id, new_book_info):
        """
        Update book information and save to storage.

        Args:
            book_id (str): The ISBN of the book to be updated.
            new_book_info (dict): Dictionary containing new book information.

        Returns:
            bool: True if book is updated successfully, False otherwise.
        """
        for book in self.books:
            if book.isbn == book_id:
                book.title = new_book_info.get('title', book.title)
                book.author = new_book_info.get('author', book.author)
                self.save_books_to_storage()
                return True
        return False

    def delete_book(self, book_id):
        """
        Delete a book from the book list and save to storage.

        Args:
            book_id (str): The ISBN of the book to be deleted.

        Returns:
            bool: True if book is deleted successfully, False otherwise.
        """
        for book in self.books:
            if book.isbn == book_id:
                self.books.remove(book)
                self.save_books_to_storage()
                return True
        return False

    def list_books(self):
        """
        Print the list of books.
        """
        if not self.books:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("No books available.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!")
            return
        for book in self.books:
            print("*************************************************************************************************")
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Availability: {book.availability}")
            print("**************************************************************************************************")

    def search_books(self, keyword):
        """
        Search for books based on a keyword.

        Args:
            keyword (str): The keyword to search for in book titles or authors.

        Returns:
            list: A list of books matching the keyword.
        """
        results = []
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                results.append(book)
        return results

    def load_books_from_storage(self):
        """
        Load books from storage.
        """
        data = self.storage.load()
        for item in data:
            try:
                title = item['Title']
                author = item['Author']
                isbn = item['ISBN']
                availability = item.get('Availability', False)  
                book = Book(title, author, isbn, availability)
                self.books.append(book)
            except KeyError as e:
                print(f"Error loading book: {e}. Skipping...")

    def save_books_to_storage(self):
        """
        Save books to storage.
        """
        data = []
        for book in self.books:
            book_data = {
                'Title': book.title,
                'Author': book.author,
                'ISBN': book.isbn,
                'Availability': book.availability
            }
            data.append(book_data)
        self.storage.save(data)

    def checkout_book(self, book_id, user_id, user_manager):
        """
        Checkout a book.

        Args:
            book_id (str): The ISBN of the book to be checked out.
            user_id (int): The ID of the user checking out the book.
            user_manager (UserManager): The user manager object.

        Returns:
            bool: True if book is successfully checked out, False otherwise.
        """
        for book in self.books:
            if book.isbn == book_id:
                boole = book.availability
                if boole == "False":
                    # Book already checked out
                    print("Book is already taken. Please try again after a few days...")
                    return False
                else:
                    user = user_manager.get_user_by_id(user_id)
                    if user:
                        user_manager.add_checked_out_book(book_id, user_id)
                        self.save_books_to_storage()
                        user_manager.save_users_to_storage()
                        book.availability = False
                        return True
                    else:
                        print("User not found.")
                        return False
        # Book not found
        print("Invalid Book Info.")
        return False

    def checkin_book(self, book_id, user_id, user_manager):
        """
        Check in a book.

        Args:
            book_id (str): The ISBN of the book to be checked in.
            user_id (int): The ID of the user checking in the book.
            user_manager (UserManager): The user manager object.

        Returns:
            bool: True if book is successfully checked in, False otherwise.
        """
        for book in self.books:
            if book.isbn == book_id:
                user = user_manager.get_user_by_id(user_id)
                if user and book_id in user.using_books:
                    user_manager.remove_checked_out_book(book_id, user_id)
                    self.save_books_to_storage()
                    user_manager.save_users_to_storage()
                    book.availability = True
                    return True
                else:
                    print("Book is not checked out by this user.")
                    return False
        # Book not found
        print("Invalid Book Info.")
        return False