class User:
    def __init__(self, name, user_id, using_books):
        """
        Initialize a User object.

        Args:
            name (str): The name of the user.
            user_id (int): The ID of the user.
            using_books: The List to store ISBN number of book used by user.
        """
        self.name = name
        self.user_id = user_id
        self.using_books = using_books

    def __str__(self):
        """
        Return a string representation of the User object.

        Returns:
            str: A string containing user information.
        """
        return f"User: {self.name} (ID: {self.user_id}) is using {self.using_books}"
