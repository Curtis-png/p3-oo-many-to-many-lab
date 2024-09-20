# lib/contract_management.py

class Book:
    all_books = []  # Class variable to keep track of all books

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)  # Add the book to the class variable

    def __repr__(self):
        return f"Book(title={self.title})"


class Author:
    all_authors = []  # Class variable to keep track of all authors

    def __init__(self, name):
        self.name = name
        self._contracts = []  # List to store contracts for this author
        Author.all_authors.append(self)  # Add the author to the class variable

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book instance.")
        if not isinstance(date, str) or not date:
            raise Exception("Invalid date.")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be a non-negative integer.")

        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)

    def __repr__(self):
        return f"Author(name={self.name})"


class Contract:
    all_contracts = []  # Class variable to keep track of all contracts

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author instance.")
        if not isinstance(book, Book):
            raise Exception("Invalid book instance.")
        if not isinstance(date, str) or not date:
            raise Exception("Invalid date.")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be a non-negative integer.")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all_contracts.append(self)  # Add contract to the class variable

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]

    def __repr__(self):
        return f"Contract(author={self.author.name}, book={self.book.title}, date={self.date}, royalties={self.royalties})"


# Example Usage
if __name__ == "__main__":
    # Create authors
    author1 = Author("George Orwell")
    author2 = Author("J.K. Rowling")

    # Create books
    book1 = Book("1984")
    book2 = Book("Animal Farm")
    book3 = Book("Harry Potter and the Philosopher's Stone")

    # Author signs contracts
    contract1 = author1.sign_contract(book1, "1949-06-08", 10)
    contract2 = author1.sign_contract(book2, "1945-08-17", 12)
    contract3 = author2.sign_contract(book3, "1997-06-26", 15)

    # Display contracts and royalties
    print("Contracts for George Orwell:", author1.contracts())
    print("Books by George Orwell:", author1.books())
    print("Total royalties for George Orwell:", author1.total_royalties())

    print("Contracts for J.K. Rowling:", author2.contracts())
    print("Books by J.K. Rowling:", author2.books())
    print("Total royalties for J.K. Rowling:", author2.total_royalties())

    # Retrieve contracts by date
    print("Contracts signed on 1949-06-08:", Contract.contracts_by_date("1949-06-08"))
