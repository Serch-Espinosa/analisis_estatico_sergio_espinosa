# -*- coding: utf-8 -*-

import unittest
import re
from unittest.mock import patch
import book_store

class TestBookStore(unittest.TestCase):
    """
    Checks the classes and functions of the book store
    """

    def setUp(self):
        self.mundo = book_store.Book("Mundo", "Pedro", 150, 5)
        self.carros = book_store.Book("Carros", "Walter", 200, 15)
        self.store= book_store.BookStore()

    @patch("builtins.print")
    def test_display(self, mock_print):
        """
        Checks the display function
        """

        self.mundo.display()
        mock_print.assert_any_call(f"Title: {self.mundo.title}")
        mock_print.assert_any_call(f"Author: {self.mundo.author}")
        mock_print.assert_any_call(f"Price: ${self.mundo.price}")
        mock_print.assert_any_call(f"Quantity: {self.mundo.quantity}")

    @patch("builtins.print")
    def test_add_books(self, mock_print):
        """
        Checks the function to add books
        """

        self.store.add_book(self.carros)
        mock_print.assert_called_with(f"Book '{self.carros.title}' added to the store.")

    @patch("builtins.print")
    def test_display_books_no_books(self, mock_print):
        """
        Checks the function to display if there's not a book
        """
        self.store.display_books()
        mock_print.assert_called_with("No books in the store.")

    @patch("builtins.print")
    def test_display_books_success(self, mock_print):
        """
        Checks the function to display books on the book store
        """
        self.store.add_book(self.mundo)
        self.store.add_book(self.carros)
        self.store.display_books()
        mock_print.assert_any_call("Books available in the store:")
        mock_print.assert_any_call(f"Title: {self.mundo.title}")
        mock_print.assert_any_call(f"Author: {self.mundo.author}")
        mock_print.assert_any_call(f"Price: ${self.mundo.price}")
        mock_print.assert_any_call(f"Quantity: {self.mundo.quantity}")
        mock_print.assert_any_call(f"Title: {self.carros.title}")
        mock_print.assert_any_call(f"Author: {self.carros.author}")
        mock_print.assert_any_call(f"Price: ${self.carros.price}")
        mock_print.assert_any_call(f"Quantity: {self.carros.quantity}")

    @patch("builtins.print")
    def test_search_books_failure(self, mock_print):
        """
        Checks when looking for a non existent book
        """
        title = "Platillos"

        self.store.search_book(title)
        mock_print.assert_called_with(f"No book found with title '{title}'.")

    @patch("builtins.print")
    def test_search_books_success(self, mock_print):
        """
        Checks when looking for an existent book
        """
        self.store.add_book(self.mundo)
        self.store.add_book(self.carros)

        title = self.carros.title

        self.store.search_book(title)
        mock_print.assert_any_call(f"Found {1} book(s) with title '{title}':")


    @patch("builtins.input")
    @patch("builtins.print")
    def test_display_all_books_main(self, mock_print, mock_input):
        """
        Checks main if can display books
        """


        mock_input.side_effect = [
            "3", "Mundo", "Pedro", "100", "5",
            "1",
            "4"
        ]

        book_store.main()

        mock_print.assert_any_call("Books available in the store:")
        mock_print.assert_any_call(f"Title: Mundo")
        mock_print.assert_any_call("Exiting...")


    @patch("builtins.print")
    @patch("builtins.input")
    def test_search_books_main(self, mock_input, mock_print):
        """
        Checks in main if can search for a book
        """

        mock_input.side_effect = ["3", "Carros", "Walter", "200", "15", "2", "CARROS", "4"]

        book_store.main()


        mock_print.assert_any_call("Found 1 book(s) with title 'CARROS':")
        mock_print.assert_any_call("Title: Carros")
        mock_print.assert_any_call("Exiting...")
