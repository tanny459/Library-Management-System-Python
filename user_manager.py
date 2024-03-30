from user import User
from storage import CSVStorage

class UserManager:
    
    def __init__(self):
        """
        Initialize UserManager object.
        """
        self.users = []
        self.storage = CSVStorage("users.csv")

    def add_user(self, user):
        """
        Add a user to the user list and save it to storage.

        Args:
            user (User): The user object to be added.
        """
        self.users.append(user)
        self.save_users_to_storage()

    def update_user(self, user_id, new_user_info):
        """
        Update user information and save to storage.

        Args:
            user_id (int): The ID of the user to be updated.
            new_user_info (dict): Dictionary containing new user information.

        Returns:
            bool: True if user is updated successfully, False otherwise.
        """
        for user in self.users:
            if user.user_id == user_id:
                user.name = new_user_info.get('name', user.name)
                self.save_users_to_storage()
                return True
        return False

    def delete_user(self, user_id):
        """
        Delete a user from the user list and save to storage.

        Args:
            user_id (int): The ID of the user to be deleted.

        Returns:
            bool: True if user is deleted successfully, False otherwise.
        """
        for user in self.users:
            if user.user_id == user_id:
                if user.using_books:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Cannot delete user because books are issued under this ID.")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    return False
                else:
                    self.users.remove(user)
                    self.save_users_to_storage()
                    return True
        return False
    
    def list_users(self):
        """
        Print the list of users.
        """
        if not self.users:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("No Users available.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return
        for user in self.users:
            print("*************************************************************")
            print(f"Name: {user.name}, User ID: {user.user_id}, Using Book: {user.using_books}")
            print("*************************************************************")

    def search_users(self, keyword):
        """
        Search for users based on a keyword.

        Args:
            keyword (str): The keyword to search for in user names.

        Returns:
            list: A list of users matching the keyword.
        """
        results = []
        for user in self.users:
            if keyword.lower() in user.name.lower():
                results.append(user)
        return results

    def load_users_from_storage(self):
        """
        Load users from storage.
        """
        data = self.storage.load()
        for item in data:
            try:
                name = item['Name']
                user_id = item['User_ID']
                if item['Using_Book'] == "":
                    using_books = list(item['Using_Book'])
                else:
                    using_books = eval(item['Using_Book'])
                user = User(name, user_id, using_books)
                self.users.append(user)
            except KeyError as e:
                print(f"Error loading user: {e}. Skipping...")
                
    def get_user_by_id(self, user_id):
        """
        Get a user by ID.

        Args:
            user_id (int): The ID of the user to get.

        Returns:
            User: The user object if found, None otherwise.
        """
        for user in self.users:
            if user.user_id == user_id:
                print("User present")
                return user
        return None
    
    def add_checked_out_book(self, book_id, user_id):
        """
        Add a checked-out book to a user's list of books.

        Args:
            book_id (int): The ID of the book to be added.
            user_id (int): The ID of the user.
        """
        user = self.get_user_by_id(user_id)
        if user:
            user.using_books.append(book_id)
            
    def remove_checked_out_book(self, book_id, user_id):
        """
        Remove a checked-out book from a user's list of books.

        Args:
            book_id (int): The ID of the book to be removed.
            user_id (int): The ID of the user.
        """
        user = self.get_user_by_id(user_id)
        if user and book_id in user.using_books:
            user.using_books.remove(book_id)

    def save_users_to_storage(self):
        """
        Save users to storage.
        """
        data = []
        for user in self.users:
            user_data = {
                'Name': user.name,
                'User_ID': user.user_id,
                'Using_Book': user.using_books
            }
            data.append(user_data)
        self.storage.save(data)
