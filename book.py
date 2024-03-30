class Book:
    def __init__(self, title, author, isbn, availability=True):
        """
        Initialize a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN (International Standard Book Number) of the book.
            availability (bool, optional): The availability status of the book. Defaults to True.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability

    def __str__(self):
        """
        String representation of the Book object.

        Returns:
            str: A string containing book details.
        """
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"