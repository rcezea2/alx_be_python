#!/usr/bin/python3

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.__books = []
        self.__checked_out = []

    def add_book(self, book: Book):
        self.__books.append(book)

    def check_out_book(self, title):
        for book in self.__books:
            if book.title == title:
                idx = self.__books.index(book)
                self.__checked_out.append(book)
                self.__books.pop(idx)
                break
        else:
            print(f"{title} is not available")

    # return_book(self):
        pass

    def return_book(self, title):
        for book in self.__checked_out:
            if book.title == title:
                idx = self.__checked_out.index(book)
                self.__books.append(book)
                self.__checked_out.pop(idx)
                break
        return True


    def list_available_books(self):
        for book in self.__books:
            print(book)
