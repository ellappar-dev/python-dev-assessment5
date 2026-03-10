# Task 2.2: Object-Oriented Programming (OOP) Fundamentals

class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        """Return the age of the book based on the year 2026."""
        current_year = 2026
        return current_year - self.publication_year

    def get_summary(self):
        """Return a summary string of the book."""
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"


# Example usage
if __name__ == "__main__":
    book1 = Book("Python Basics", "Alice Smith", "1234567890", 2018)
    book2 = Book("Advanced Python", "Bob Johnson", "0987654321", 2020)

    print(book1.get_summary())
    print(f"Book age: {book1.get_age()} years\n")

    print(book2.get_summary())
    print(f"Book age: {book2.get_age()} years")