# -*- coding: utf-8 -*-

import re
import unittest
from unittest.mock import patch
import class_exercises


#27

class TestBankAccount(unittest.TestCase):
    """
    Checks Bank Account class
    """
    def setUp(self):
        self.account = class_exercises.BankAccount(317, 2500)

    def test_check_bank_account(self):
        """
        checks if the bank account is working
        """

        self.assertEqual(self.account.account_number, 317)
        self.assertEqual(self.account.balance, 2500)

    @patch("builtins.print")
    def test_view_account(self, mock_print):
        """
        Checks function to see bank account details
        """
        self.account.view_account()

        mock_print.assert_called_with(
            f"The account {self.account.account_number} has a balance of {self.account.balance}"
        )

class TestBankingSystem(unittest.TestCase):
    """
    Checks the banking system class
    """
    user = "user123"
    password = "pass123"


    def setUp(self):
        self.bank_sys = class_exercises.BankingSystem()

    def test_banking_system_start(self):
        """
        Checks that banking system can start correctly
        """

        self.assertEqual(self.bank_sys.users, {f"{self.user}": f"{self.password}"})
        self.assertEqual(self.bank_sys.logged_in_users, set())

    @patch("builtins.print")
    def test_authenticate_success(self, mock_print):
        """
        Checks that the user authentication function works
        """
        authenticated = self.bank_sys.authenticate(self.user, self.password)
        self.assertTrue(authenticated)
        self.assertIn(self.user, self.bank_sys.logged_in_users)
        mock_print.assert_called_with(f"User {self.user} authenticated successfully.")

    @patch("builtins.print")
    def test_authenticate_already(self, mock_print):
        """
        Checks that the banking systems can detect that the user is already authenticated
        """
        self.bank_sys.logged_in_users.add(self.user)
        authenticated = self.bank_sys.authenticate(self.user, self.password)
        self.assertFalse(authenticated)
        mock_print.assert_called_with("User already logged in.")

    @patch("builtins.print")
    def test_authenticate_fail(self, mock_print):
        """
        Checks that the authentification function fails
        """
        authenticated = self.bank_sys.authenticate(self.user,"lepassword")
        self.assertFalse(authenticated)
        self.assertNotIn(self.user, self.bank_sys.logged_in_users)
        mock_print("Authentication failed.")

    @patch("builtins.print")
    def test_transfer_money_user_not_authenticated(self, mock_print):
        """
        Checks that a user not authenticated can't transfer money
        """
        receiver = "user321"
        amount = 350
        transaction_type = "express"
        result = self.bank_sys.transfer_money(
            self.user, receiver, amount, transaction_type
        )
        mock_print.assert_called_with("Sender not authenticated.")
        self.assertFalse(result)

    @patch("builtins.print")
    def test_transfer_money_regular(self, mock_print):
        """
        Checks that the Banking System can transfer money in regular type
        """
        receiver = "user321"
        amount = 500
        transaction_type = "regular"
        self.bank_sys.logged_in_users.add(self.user)
        result = self.bank_sys.transfer_money(self.user, receiver, amount, transaction_type)
        mock_print.assert_called_with(
            f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {self.user} to {receiver} processed successfully."
        )
        self.assertTrue(result)

    @patch("builtins.print")
    def test_transfer_money_express(self, mock_print):
        """
        Checks that the Banking System can transfer money in express type
        """
        receiver = "user321"
        amount = 450
        transaction_type = "express"
        self.bank_sys.logged_in_users.add(self.user)
        result = self.bank_sys.transfer_money(self.user, receiver, amount, transaction_type)
        mock_print.assert_called_with(
            f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {self.user} to {receiver} processed successfully."
        )
        self.assertTrue(result)


    @patch("builtins.print")
    def test_transfer_money_scheduled(self, mock_print):
        """
        Checks that the Banking System can transfer money in scheduled type
        """
        receiver = "user321"
        amount = 300
        transaction_type = "scheduled"
        self.bank_sys.logged_in_users.add(self.user)
        result = self.bank_sys.transfer_money(self.user, receiver, amount, transaction_type)
        mock_print.assert_called_with(
            f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {self.user} to {receiver} processed successfully."
        )
        self.assertTrue(result)

    @patch("builtins.print")
    def test_transfer_money_invalid_transactio_type(self, mock_print):
        """
        Checks that the Banking System can detect an invalid transaction type
        """
        receiver = "user321"
        amount = 250
        transaction_type = "instant"
        self.bank_sys.logged_in_users.add(self.user)
        result = self.bank_sys.transfer_money(self.user, receiver, amount, transaction_type)
        mock_print.assert_called_with("Invalid transaction type.")
        self.assertFalse(result)

    @patch("builtins.print")
    def test_transfer_money_insufficient_funds(self, mock_print):
        """
        Checks that the Banking System can detect that there are insufficient funds.
        """
        receiver = "user321"
        amount = 1000
        transaction_type = "regular"
        self.bank_sys.logged_in_users.add(self.user)
        result = self.bank_sys.transfer_money(self.user, receiver, amount, transaction_type)
        mock_print.assert_called_with("Insufficient funds.")
        self.assertFalse(result)

#28

class TestShopping(unittest.TestCase):
    """
    Checks the product and shopping cart classes
    """

    def setUp(self):
        self.shopping_cart = class_exercises.ShoppingCart()
        self.cereal = class_exercises.Product("Cereal", 50)
        self.milk = class_exercises.Product("Milk", 35)

    @patch("builtins.print")
    def test_view_product(self, mock_print):
        """
        Checks the function that display the product details
        """
        self.cereal.view_product()
        mock_print.assert_called_with(f"The product {self.cereal.name} has a price of {self.cereal.price}")


    def test_add_product_already_existing_product(self):
        """
        Checks if the add product function can add an already existing product in the cart
        """

        product = self.cereal.name
        quantity = 2

        self.shopping_cart.items.append({"product": product, "quantity": quantity})
        self.shopping_cart.add_product(product)
        self.assertEqual(self.shopping_cart.items, [{"product": product, "quantity": (quantity + 1)}])

    def test_add_product_new(self):
        """
        Checks if the "add product" function can add a new product in the cart
        """
        product = self.milk.name
        quantity = 1
        self.shopping_cart.add_product(product, quantity)
        self.assertEqual(self.shopping_cart.items, [{"product": product, "quantity": quantity}])

    def test_remove_product_not_completely(self):
        """
        Checks if the function can remove an existing product in the cart but not completely
        """
        product = self.cereal.name
        quantity = 2
        self.shopping_cart.items.append({"product": product, "quantity": quantity})
        self.shopping_cart.remove_product(product)
        self.assertEqual(self.shopping_cart.items, [{"product": product, "quantity": (quantity-1)}])

    def test_remove_product_completely(self):
        """
        Checks if the function can remove an existing product in the cart
        """
        product = self.milk.name
        quantity = 2
        self.shopping_cart.items.append({"product": product, "quantity": quantity})
        self.shopping_cart.remove_product(product, quantity)
        self.assertEqual(self.shopping_cart.items, [])

    def test_remove_product_not_in_cart(self):
        """
        Checks if the function can break trying to remove a non-existent product
        """
        product = self.cereal.name
        self.shopping_cart.remove_product(product)
        self.assertEqual(self.shopping_cart.items, [])

    @patch("builtins.print")
    def test_view_cart(self, mock_print):
        """
        Checks the function to view the shopping cart
        """
        product = self.cereal
        quantity = 3
        self.shopping_cart.add_product(product,quantity)
        self.cart = self.shopping_cart.items[0]
        mock_print(
                f"{self.cart['quantity']} x {self.cart['product'].name}"
                f" - ${self.cart['product'].price * self.cart['quantity']}"
            )

    @patch("builtins.print")
    def test_checkout(self, mock_print):
        """
        Checks the checkout function
        """
        self.shopping_cart.add_product(self.cereal, 5)
        self.shopping_cart.add_product(self.milk, 2)
        self.shopping_cart.checkout()
        total = sum(item["product"].price * item["quantity"] for item in self.shopping_cart.items)
        mock_print.assert_any_call(f"Total: ${total}")
        mock_print.assert_called_with("Checkout completed. Thank you for shopping!")
