#!/usr/bin/python3

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []
        self._checked_out = []

    def add_book(self, book: Book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                idx = self._books.index(book)
                self._checked_out.append(book)
                self._books.pop(idx)
                break
        else:
            print(f"{title} is not available")

    # return_book(self):
        pass

    def return_book(self, title):
        for book in self._checked_out:
            if book.title == title:
                idx = self._checked_out.index(book)
                self._books.append(book)
                self._checked_out.pop(idx)
                break
        return True


    def list_available_books(self):
        for book in self._books:
            print(book)
