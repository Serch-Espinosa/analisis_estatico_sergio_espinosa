# -*- coding: utf-8 -*-
import re
import unittest
import class_exercises


class TestMethods(unittest.TestCase):
    """
    White_box unittest class.
    """

    #1

    def test_check_number_status_positive(self):
        """
        Checks if the number given is positive
        """
        self.assertEqual(class_exercises.check_number_status(5), "Positive")

    def test_check_number_status_negative(self):
        """
        Checks if the number given is negative
        """
        self.assertEqual(class_exercises.check_number_status(-3), "Negative")

    def test_check_number_status_zero(self):
        """
        Checks if the number given is zero
        """
        self.assertEqual(class_exercises.check_number_status(0), "Zero")

    #2

    def test_validate_password_lenght_yes(self):
        """
        Checks if lenght of password is equal or more than 8
        """
        self.assertTrue(class_exercises.validate_password("Hola123!"))

    def test_validate_password_lenght_no(self):
        """
        Checks if lenght of password is less than 8
        """
        self.assertFalse(class_exercises.validate_password("Hola12!"))

    def test_validate_password_uppercase_yes(self):
        """
        Checks if the password has at least 1 uppercase letter
        """
        self.assertTrue(class_exercises.validate_password("Hola12345$"))

    def test_validate_password_uppercase_no(self):
        """
        Checks if the password hasn't a uppercase letter
        """
        self.assertFalse(class_exercises.validate_password("hola12345$"))

    def test_validate_password_lowercase_yes(self):
        """
        Checks if the password has at least 1 lowercase letter
        """
        self.assertTrue(class_exercises.validate_password("HOLa12345%"))

    def test_validate_password_lowercase_no(self):
        """
        Checks if the password hasn't at least 1 lowercase letter
        """
        self.assertFalse(class_exercises.validate_password("HOLA12345%"))

    def test_validate_password_digit_yes(self):
        """
        Checks if the password has at least 1 digit
        """
        self.assertTrue(class_exercises.validate_password("HolaMundo1&"))

    def test_validate_password_digit_no(self):
        """
        Checks if the password hasn't at least 1 digit
        """
        self.assertFalse(class_exercises.validate_password("HolaMundo&"))

    def test_validate_password_special_yes(self):
        """
        Checks if the password has at least 1 special character
        """
        self.assertTrue(class_exercises.validate_password("Sergio12345@"))

    def test_validate_password_(self):
        """
        Checks if the password hasn't at least 1 special character
        """
        self.assertFalse(class_exercises.validate_password("Sergio12345"))

    #3

    def test_calculate_total_discount_no_discount(self):
        """
        Calculates the discount of a customer's purchase that is less than 100
        """
        self.assertEqual(class_exercises.calculate_total_discount(99),0)

    def test_calculate_total_discount_ten_percent1(self):
        """
        Calculates the discount of a customer's purchase that is
        equal or more than 100 and equal or less than 500
        """
        self.assertEqual(class_exercises.calculate_total_discount(100),(100*0.1))

    def test_calculate_total_discount_ten_percent2(self):
        """
        Calculates the discount of a customer's purchase that is
        equal or more than 100 and equal or less than 500
        """
        self.assertEqual(class_exercises.calculate_total_discount(500),(500*0.1))

    def test_calculate_total_discount_twenty_percent(self):
        """
        Calculates the discount of a customer's purchase that is more than 500
        """
        self.assertEqual(class_exercises.calculate_total_discount(501),(501*0.2))

    #4

    def test_calculate_order_total_between_1_and_5_first(self):
        """
        Calculates the total price of an order between 1 and 5 items of each type
        """
        items = [{"quantity": 1, "price": 15}]
        self.assertEqual(class_exercises.calculate_order_total(items),15)

    def test_calculate_order_total_between_1_and_5_second(self):
        """
        Calculates the total price of an order between 1 and 5 items of each type
        """
        items = [{"quantity": 5, "price": 15}]
        self.assertEqual(class_exercises.calculate_order_total(items),(15*5))

    def test_calculate_order_total_between_6_and_10_first(self):
        """
        Calculates the total price of an order between 6 and 10 items of each type
        """
        items = [{"quantity": 6, "price": 10}]
        self.assertAlmostEqual(class_exercises.calculate_order_total(items),(10*6*0.95))

    def test_calculate_order_total_between_6_and_10_second(self):
        """
        Calculates the total price of an order between 6 and 10 items of each type
        """
        items = [{"quantity": 10, "price": 20}]
        self.assertAlmostEqual(class_exercises.calculate_order_total(items),(10*20*0.95))

    def test_calculate_order_total_more_than_10(self):
        """
        Calculates the total price of an order with more than 10 items each one
        """
        items = [{"quantity": 11, "price": 150}]
        self.assertAlmostEqual(class_exercises.calculate_order_total(items),(11*150*0.90))

    def test_calculate_order_total_multiple_items(self):
        """
        Calculates the total price of an order with multiple items
        """
        items = [
            {"quantity": 3, "price": 10},
            {"quantity": 8, "price": 15},
            {"quantity": 12, "price": 17}
        ]
        self.assertAlmostEqual(class_exercises.calculate_order_total(items),(3*10)+(8*15*0.95)+(12*17*0.9))

    #5

    def test_calculate_items_shipping_cost_standard_case_1(self):
        """
        Calculates shipping cost of standard shipping that weights equal or less than 5
        """
        items = [{"weight": 5}]
        self.assertEqual(class_exercises.calculate_items_shipping_cost(items, "standard"),10)

    def test_calculate_items_shipping_cost_standard_case_2(self):
        """
        Calculates shipping cost of standard shipping that weights more than 5, but less or equal to 10
        """
        items = [{"weight": 6}]
        self.assertEqual(class_exercises.calculate_items_shipping_cost(items, "standard"),15)

    def test_calculate_items_shipping_cost_standard_case_3(self):
        """
        Calculates shipping cost of standard shipping that weights more than 5, but less or equal to 10
        """
        items = [{"weight": 10}]
        self.assertEqual(class_exercises.calculate_items_shipping_cost(items, "standard"),15)

    def test_calculate_items_shipping_cost_standard_case_4(self):
        """
        Calculates shipping cost of standard shipping that weights more than 10
        """
        items = [{"weight": 11}]
        self.assertEqual(class_exercises.calculate_items_shipping_cost(items, "standard"), 20)

    def test_calculate_items_shipping_cost_express_case_1(self):
        """
        Calculates shipping cost of express shipping that weights equal or less than 5
        """
        items = [{"weight": 5}]
        self.assertEqual(class_exercises.calculate_items_shipping_cost(items, "express"),20)

    def test_calculate_items_shipping_cost_express_case_2(self):
        """
        Calculates shipping cost of express shipping that weights more than 5, but less or equal to 10
        """
        items = [{"weight": 6}]
        self.assertEqual(class_exercises.calculate_items_shipping_cost(items, "express"),30)

    def test_calculate_items_shipping_cost_express_case_3(self):
        """
        Calculates shipping cost of express shipping that weights more than 5, but less or equal to 10
        """
        items = [{"weight": 10}]
        self.assertEqual(class_exercises.calculate_items_shipping_cost(items, "express"),30)

    def test_calculate_items_shipping_cost_express_case_4(self):
        """
        Calculates shipping cost of express shipping that weights more than 10
        """
        items = [{"weight": 11}]
        self.assertEqual(class_exercises.calculate_items_shipping_cost(items, "express"),40)

    def test_calculate_items_shipping_cost_invalid_shipping_method(self):
        """
        Checks if shipping type is invalid
        """
        items = [{"weight": 15}]
        with self.assertRaises(ValueError) as context:
            class_exercises.calculate_items_shipping_cost(items, "premium")

    def test_calculate_items_shipping_cost_express_multiple_items(self):
        """
        Calculates shipping cost of express shipping with multiple items
        """
        items = [{"weight": 1},
                 {"weight": 3},
                 {"weight": 6}

        ]
        self.assertEqual(class_exercises.calculate_items_shipping_cost(items, "express"),30)

    #6

    def test_validate_login_username_case_1(self):
        """
        Validates username login credential
        """
        self.assertEqual(class_exercises.validate_login("Henry","1234s6789o"), "Login Successful")

    def test_validate_login_username_case_2(self):
        """
        Validates username login credential
        """
        self.assertEqual(class_exercises.validate_login("Henry123456789012345","1234s6789o"), "Login Successful")

    def test_validate_login_invalid_username_case_1(self):
        """
        Validates username login credential
        """
        self.assertEqual(class_exercises.validate_login("Henr","1234s6789o"), "Login Failed")

    def test_validate_login_invalid_username_case_2(self):
        """
        Validates username login credential
        """
        self.assertEqual(class_exercises.validate_login("Henry1234567890123456","1234s6789o"), "Login Failed")

    def test_validate_login_password_case_1(self):
        """
        Validates password login credential
        """
        self.assertEqual(class_exercises.validate_login("Sergio123!","1.e456g8"), "Login Successful")

    def test_validate_login_password_case_2(self):
        """
        Validates password login credential
        """
        self.assertEqual(class_exercises.validate_login("Sergio123!","1.e456g890123a5"), "Login Successful")

    def test_validate_login_invalid_password_case_1(self):
        """
        Validates password login credential
        """
        self.assertEqual(class_exercises.validate_login("Sergio123!","1.e456g"), "Login Failed")

    def test_validate_login_invalid_password_case_2(self):
        """
        Validates password login credential
        """
        self.assertEqual(class_exercises.validate_login("Sergio123!","1.e456g890123a56"), "Login Failed")

    #7

    def test_verify_age_case_1(self):
        """
        Determines whether a person is eligible for a certain service based on their age.
        Between 18 and 65
        """
        self.assertEqual(class_exercises.verify_age(18), "Eligible")

    def test_verify_age_case_2(self):
        """
        Determines whether a person is eligible for a certain service based on their age.
        Between 18 and 65
        """
        self.assertEqual(class_exercises.verify_age(65), "Eligible")

    def test_verify_age_invalid_case_1(self):
        """
        Determines whether a person is eligible for a certain service based on their age.
        Between 18 and 65
        """
        self.assertEqual(class_exercises.verify_age(17), "Not Eligible")

    def test_verify_age_invalid_case_2(self):
        """
        Determines whether a person is eligible for a certain service based on their age.
        Between 18 and 65
        """
        self.assertEqual(class_exercises.verify_age(66), "Not Eligible")

    #8

    def test_categorize_product_category_a_case_1(self):
        """
        Determines the price category of a product based on its price.
        Category A (Between 10 and 50)
        """
        self.assertEqual(class_exercises.categorize_product(10),"Category A")

    def test_categorize_product_category_a_case_2(self):
        """
        Determines the price category of a product based on its price.
        Category A (Between 10 and 50)
        """
        self.assertEqual(class_exercises.categorize_product(50),"Category A")

    def test_categorize_product_category_b_case_1(self):
        """
        Determines the price category of a product based on its price.
        Category A (Between 51 and 100)
        """
        self.assertEqual(class_exercises.categorize_product(51),"Category B")

    def test_categorize_product_category_b_case_2(self):
        """
        Determines the price category of a product based on its price.
        Category A (Between 51 and 100)
        """
        self.assertEqual(class_exercises.categorize_product(100),"Category B")

    def test_categorize_product_category_c_case_1(self):
        """
        Determines the price category of a product based on its price.
        Category A (Between 101 and 200)
        """
        self.assertEqual(class_exercises.categorize_product(101),"Category C")

    def test_categorize_product_category_c_case_2(self):
        """
        Determines the price category of a product based on its price.
        Category A (Between 101 and 200)
        """
        self.assertEqual(class_exercises.categorize_product(200),"Category C")

    def test_categorize_product_category_d_case_1(self):
        """
        Determines the price category of a product based on its price.
        Category A (less than 10 and more than 200)
        """
        self.assertEqual(class_exercises.categorize_product(9),"Category D")

    def test_categorize_product_category_d_case_2(self):
        """
        Determines the price category of a product based on its price.
        Category A (less than 10 and more than 200)
        """
        self.assertEqual(class_exercises.categorize_product(201),"Category D")

    #9

    def test_validate_email_len_case_1(self):
        """
        Validates lenght email addresses.
        Between 5 and 50
        """
        self.assertEqual(class_exercises.validate_email("I2@a."), "Valid Email")

    def test_validate_email_len_case_2(self):
        """
        Validates lenght email addresses.
        Between 5 and 50
        """
        self.assertEqual(class_exercises.validate_email("I2@a56789O123456789012345678901234567890123456789."), "Valid Email")

    def test_validate_email_invalid_len_case_1(self):
        """
        Validates lenght email addresses.
        Between 5 and 50
        """
        self.assertEqual(class_exercises.validate_email("I@e."), "Invalid Email")

    def test_validate_email_invalid_len_case_2(self):
        """
        Validates lenght email addresses.
        Between 5 and 50
        """
        self.assertEqual(class_exercises.validate_email("12@a56789O1234567890123456789012345678901234567890."), "Invalid Email")

    def test_validate_email_invalid_case_1(self):
        """
        Validates lenght email addresses.
        Between 5 and 50
        """
        self.assertEqual(class_exercises.validate_email("Hola@Itesomx"), "Invalid Email")

    def test_validate_email_invalid_case_2(self):
        """
        Validates lenght email addresses.
        Between 5 and 50
        """
        self.assertEqual(class_exercises.validate_email("HolaIteso.mx"), "Invalid Email")

    #10

    def test_celsius_to_fahrenheit_case_1(self):
        """
        Converts temperatures from Celsius to Fahrenheit.
        Between -100 and 100
        """
        self.assertAlmostEqual(class_exercises.celsius_to_fahrenheit(-100), (-100*9/5)+32)

    def test_celsius_to_fahrenheit_case_2(self):
        """
        Converts temperatures from Celsius to Fahrenheit.
        Between -100 and 100
        """
        self.assertAlmostEqual(class_exercises.celsius_to_fahrenheit(100), (100*9/5)+32)

    def test_celsius_to_fahrenheit_invalid_case_1(self):
        """
        Converts temperatures from Celsius to Fahrenheit.
        Between -100 and 100
        """
        self.assertAlmostEqual(class_exercises.celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_celsius_to_fahrenheit_invalid_case_2(self):
        """
        Converts temperatures from Celsius to Fahrenheit.
        Between -100 and 100
        """
        self.assertAlmostEqual(class_exercises.celsius_to_fahrenheit(101), "Invalid Temperature")

    #11

    def test_validate_credit_card_case_1(self):
        """
        Validates credit card numbers between 13 and 16 numbers
        """
        self.assertEqual(class_exercises.validate_credit_card("1234567890123"), "Valid Card")

    def test_validate_credit_card_case_2(self):
        """
        Validates credit card numbers between 13 and 16 numbers
        """
        self.assertEqual(class_exercises.validate_credit_card("1234567890123456"), "Valid Card")

    def test_validate_credit_card_invalid_len_case_1(self):
        """
        Validates credit card numbers between 13 and 16 numbers
        """
        self.assertEqual(class_exercises.validate_credit_card("123456789012"), "Invalid Card")

    def test_validate_credit_card_invalid_len_case_2(self):
        """
        Validates credit card numbers between 13 and 16 numbers
        """
        self.assertEqual(class_exercises.validate_credit_card("12345678901234567"), "Invalid Card")

    def test_validate_credit_card_invalid(self):
        """
        Validates credit card numbers between 13 and 16 numbers (Only digits)
        """
        self.assertEqual(class_exercises.validate_credit_card("1234567890123A"), "Invalid Card")

    #12

    def test_validate_date_year_case_1(self):
        """
        Validates dates.
        Between 1900 and 2100 in year
        """
        self.assertEqual(class_exercises.validate_date(1900,3,5), "Valid Date")

    def test_validate_date_year_case_2(self):
        """
        Validates dates.
        Between 1900 and 2100 in year
        """
        self.assertEqual(class_exercises.validate_date(2100,3,5), "Valid Date")

    def test_validate_date_invalid_year_case_1(self):
        """
        Validates dates.
        Between 1900 and 2100 in year
        """
        self.assertEqual(class_exercises.validate_date(1899,3,5), "Invalid Date")

    def test_validate_date_invalid_year_case_2(self):
        """
        Validates dates.
        Between 1900 and 2100 in year
        """
        self.assertEqual(class_exercises.validate_date(2101,3,5), "Invalid Date")

    def test_validate_date_month_case_1(self):
        """
        Validates dates.
        Between 1 and 12 in month
        """
        self.assertEqual(class_exercises.validate_date(2026,1,20), "Valid Date")

    def test_validate_date_month_case_2(self):
        """
        Validates dates.
        Between 1 and 12 in month
        """
        self.assertEqual(class_exercises.validate_date(2026,12,20), "Valid Date")

    def test_validate_date_invalid_month_case_1(self):
        """
        Validates dates.
        Between 1 and 12 in month
        """
        self.assertEqual(class_exercises.validate_date(2026,0,20), "Invalid Date")

    def test_validate_date_invalid_month_case_2(self):
        """
        Validates dates.
        Between 1 and 12 in month
        """
        self.assertEqual(class_exercises.validate_date(2026,13,20), "Invalid Date")

    def test_validate_date_day_case_1(self):
        """
        Validates dates.
        Between 1 and 31 in day
        """
        self.assertEqual(class_exercises.validate_date(2026,3,1), "Valid Date")

    def test_validate_date_day_case_2(self):
        """
        Validates dates.
        Between 1 and 31 in day
        """
        self.assertEqual(class_exercises.validate_date(2026,3,31), "Valid Date")

    def test_validate_date_invalid_day_case_1(self):
        """
        Validates dates.
        Between 1 and 31 in day
        """
        self.assertEqual(class_exercises.validate_date(2026,3,0), "Invalid Date")

    def test_validate_date_invalid_day_case_2(self):
        """
        Validates dates.
        Between 1 and 31 in day
        """
        self.assertEqual(class_exercises.validate_date(2026,3,32), "Invalid Date")

    def test_validate_date_impossible_date(self):
        """
        Validates dates.
        This is an impossible date, is valid in the code but in reality it doesn't exist
        """
        self.assertEqual(class_exercises.validate_date(2026,2,31), "Valid Date")

    #13

    def test_check_flight_eligibility_frecuent_case_1(self):
        """
        Checks the eligibility of a passenger to book a flight.
        Between 18 and 65 of age
        """
        self.assertEqual(class_exercises.check_flight_eligibility(18,"Frecuent"), "Eligible to Book")

    def test_check_flight_eligibility_frecuent_case_2(self):
        """
        Checks the eligibility of a passenger to book a flight.
        Between 18 and 65 of age or frecuent flyer
        """
        self.assertEqual(class_exercises.check_flight_eligibility(65,"Frecuent"), "Eligible to Book")

    def test_check_flight_eligibility_frecuent_invalid_age_case_1(self):
        """
        Checks the eligibility of a passenger to book a flight.
        Between 18 and 65 of age or frequent flyer
        """
        self.assertEqual(class_exercises.check_flight_eligibility(17,"Frecuent"), "Eligible to Book")

    def test_check_flight_eligibility_frecuent_invalid_age_case_2(self):
        """
        Checks the eligibility of a passenger to book a flight.
        Between 18 and 65 of age or frequent flyer
        """
        self.assertEqual(class_exercises.check_flight_eligibility(66,"Frecuent"), "Eligible to Book")

    def test_check_flight_eligibility_not_frecuent_case_1(self):
        """
        Checks the eligibility of a passenger to book a flight.
        Between 18 and 65 of age or frecuent flyer
        """
        self.assertEqual(class_exercises.check_flight_eligibility(18,""), "Eligible to Book")

    def test_check_flight_eligibility_not_frecuent_case_2(self):
        """
        Checks the eligibility of a passenger to book a flight.
        Between 18 and 65 of age or frecuent flyer
        """
        self.assertEqual(class_exercises.check_flight_eligibility(65,""), "Eligible to Book")

    def test_check_flight_eligibility_not_frecuent_invalid_age_case_1(self):
        """
        Checks the eligibility of a passenger to book a flight.
        Between 18 and 65 of age or frecuent flyer
        """
        self.assertEqual(class_exercises.check_flight_eligibility(17,""), "Not Eligible to Book")

    def test_check_flight_eligibility_not_frecuent_invalid_age_case_2(self):
        """
        Checks the eligibility of a passenger to book a flight.
        Between 18 and 65 of age or frecuent flyer
        """
        self.assertEqual(class_exercises.check_flight_eligibility(66,""), "Not Eligible to Book")

    #14

    def test_validate_url_len_https(self):
        """
        Validates URLs with lenght less or equal to 255
        """
        self.assertEqual(class_exercises.validate_url("https://www.ejemplo.com/02498014980192074520498207498074204729895204278047980782407982748974189dsadfsgre82fd28s82fds8298fed982829fes8282fes882fe9s89fes8282fes89fe8s28fes28fes822fe98s5fd52s25fd52s952fd259s95229fe82s89fe8s98q82f82ew8282fe82w82few8998few82fe"), "Valid URL")

    def test_validate_url__invalid_len_https(self):
        """
        Validates URLs with lenght less or equal to 255
        """
        self.assertEqual(class_exercises.validate_url("https://www.ejemplo.com/0249804014980192074520498207498074204729895204278047980782407982748974189dsadfsgre82fd28s82fds8298fed982829fes8282fes882fe9s89fes8282fes89fe8s28fes28fes822fe98s5fd52s25fd52s952fd259s95229fe82s89fe8s98q82f82ew8282fe82w82few8998dw82fe"), "Valid URL")

    def test_validate_url_len_http(self):
        """
        Validates URLs with lenght less or equal to 255
        """
        self.assertEqual(class_exercises.validate_url("http://www.ejemplo.com/024958014980192074520498207498074204729895204278047980782407982748974189dsadfsgre82fd28s82fds8298fed982829fes8282fes882fe9s89fes8282fes89fe8s28fes28fes822fe98s5fd52s25fd52s952fd259s95229fe82s89fe8s98q82f82ew8282fe82w82few8998few82fe"), "Valid URL")

    def test_validate_url_invalid_len_http(self):
        """
        Validates URLs with lenght less or equal to 255
        """
        self.assertEqual(class_exercises.validate_url("http://www.ejemplo.com/0249845014980192074520498207498074204729895204278047980782407982748974189dsadfsgre82fd28s82fds8298fed982829fes8282fes882fe9s89fes8282fes89fe8s28fes28fes822fe98s5fd52s25fd52s952fd259s95229fe82s89fe8s98q82f82ew8282fe82w82few8998few82fe"), "Invalid URL")

    def test_validate_url_invalid_start(self):
        """
        Validates URLs with lenght less or equal to 255
        """
        self.assertEqual(class_exercises.validate_url("htt://www.ejemplo.com"), "Invalid URL")

    #15

    def test_calculate_quantity_discount_0_case_1(self):
        """
        Calculates discounts based on the quantity of a product.
        Between 1 and 5
        """
        self.assertEqual(class_exercises.calculate_quantity_discount(1), "No Discount")

    def test_calculate_quantity_discount_0_case_2(self):
        """
        Calculates discounts based on the quantity of a product.
        Between 1 and 5
        """
        self.assertEqual(class_exercises.calculate_quantity_discount(5), "No Discount")

    def test_calculate_quantity_discount_5_case_1(self):
        """
        Calculates discounts based on the quantity of a product.
        Between 6 and 10
        """
        self.assertEqual(class_exercises.calculate_quantity_discount(6), "5% Discount")

    def test_calculate_quantity_discount_5_case_2(self):
        """
        Calculates discounts based on the quantity of a product.
        Between 6 and 10
        """
        self.assertEqual(class_exercises.calculate_quantity_discount(10), "5% Discount")

    def test_calculate_quantity_discount_10(self):
        """
        Calculates discounts based on the quantity of a product.
        More than 10
        """
        self.assertEqual(class_exercises.calculate_quantity_discount(11), "10% Discount")

    def test_calculate_quantity_discount_10_invalid_case(self):
        """
        Calculates discounts based on the quantity of a product.
        More than 10
        """
        self.assertEqual(class_exercises.calculate_quantity_discount(0), "10% Discount")

    #16

    def test_check_file_size_case_1(self):
        """
        Checks if the size is valid for a file.
        Between 0 and 1048576 bytes (1 MB)
        """
        self.assertEqual(class_exercises.check_file_size(0), "Valid File Size")

    def test_check_file_size_case_2(self):
        """
        Checks if the size is valid for a file.
        Between 0 and 1048576 bytes (1 MB)
        """
        self.assertEqual(class_exercises.check_file_size(1048576), "Valid File Size")

    def test_check_file_size_ivalid(self):
        """
        Checks if the size is valid for a file.
        Between 0 and 1048576 bytes (1 MB)
        """
        self.assertEqual(class_exercises.check_file_size(1048577), "Invalid File Size")

    #17

    def test_check_loan_eligibility_case_1(self):
        """
        Checks if and which loan can be granted based on the income and credit score.
        """
        self.assertEqual(class_exercises.check_loan_eligibility(30000,700),"Secured Loan")

    def test_check_loan_eligibility_case_2(self):
        """
        Checks if and which loan can be granted based on the income and credit score.
        """
        self.assertEqual(class_exercises.check_loan_eligibility(30000,701),"Standard Loan")

    def test_check_loan_eligibility_case_3(self):
        """
        Checks if and which loan can be granted based on the income and credit score.
        """
        self.assertEqual(class_exercises.check_loan_eligibility(60000,701),"Standard Loan")

    def test_check_loan_eligibility_case_4(self):
        """
        Checks if and which loan can be granted based on the income and credit score.
        """
        self.assertEqual(class_exercises.check_loan_eligibility(60000,700),"Secured Loan")

    def test_check_loan_eligibility_case_5(self):
        """
        Checks if and which loan can be granted based on the income and credit score.
        """
        self.assertEqual(class_exercises.check_loan_eligibility(60001,750),"Standard Loan")

    def test_check_loan_eligibility_case_6(self):
        """
        Checks if and which loan can be granted based on the income and credit score.
        """
        self.assertEqual(class_exercises.check_loan_eligibility(60001,751),"Premium Loan")

    def test_check_loan_eligibility_case_7(self):
        """
        Checks if and which loan can be granted based on the income and credit score.
        """
        self.assertEqual(class_exercises.check_loan_eligibility(60000,751),"Standard Loan")

    def test_check_loan_eligibility_case_8(self):
        """
        Checks if and which loan can be granted based on the income and credit score.
        """
        self.assertEqual(class_exercises.check_loan_eligibility(29999,800),"Not Eligible")

    #18

    def test_calculate_shipping_cost_case_1(self):
        """
        Calculates the shipping cost based on the package weight and dimensions.
        """
        self.assertEqual(class_exercises.calculate_shipping_cost(1,10,10,10), 5)

    def test_calculate_shipping_cost_case_2(self):
        """
        Calculates the shipping cost based on the package weight and dimensions.
        """
        self.assertEqual(class_exercises.calculate_shipping_cost(2,10,10,10), 20)

    def test_calculate_shipping_cost_case_3(self):
        """
        Calculates the shipping cost based on the package weight and dimensions.
        """
        self.assertEqual(class_exercises.calculate_shipping_cost(5,10,10,10), 20)

    def test_calculate_shipping_cost_case_4(self):
        """
        Calculates the shipping cost based on the package weight and dimensions.
        """
        self.assertEqual(class_exercises.calculate_shipping_cost(5,11,11,11), 10)

    def test_calculate_shipping_cost_case_5(self):
        """
        Calculates the shipping cost based on the package weight and dimensions.
        """
        self.assertEqual(class_exercises.calculate_shipping_cost(5,30,30,30), 10)

    def test_calculate_shipping_cost_case_6(self):
        """
        Calculates the shipping cost based on the package weight and dimensions.
        """
        self.assertEqual(class_exercises.calculate_shipping_cost(5,31,31,31), 20)

    def test_calculate_shipping_cost_case_7(self):
        """
        Calculates the shipping cost based on the package weight and dimensions.
        """
        self.assertEqual(class_exercises.calculate_shipping_cost(6,30,30,30), 20)

    #19

    def test_grade_quiz_case_1(self):
        """
        Grades online quizzes based on the number of correct and incorrect answers.
        """
        self.assertEqual(class_exercises.grade_quiz(7,2), "Pass")

    def test_grade_quiz_case_2(self):
        """
        Grades online quizzes based on the number of correct and incorrect answers.
        """
        self.assertEqual(class_exercises.grade_quiz(6,2), "Conditional Pass")

    def test_grade_quiz_case_3(self):
        """
        Grades online quizzes based on the number of correct and incorrect answers.
        """
        self.assertEqual(class_exercises.grade_quiz(5,2), "Conditional Pass")

    def test_grade_quiz_case_4(self):
        """
        Grades online quizzes based on the number of correct and incorrect answers.
        """
        self.assertEqual(class_exercises.grade_quiz(5,3), "Conditional Pass")

    def test_grade_quiz_case_5(self):
        """
        Grades online quizzes based on the number of correct and incorrect answers.
        """
        self.assertEqual(class_exercises.grade_quiz(4,3), "Fail")

    def test_grade_quiz_case_6(self):
        """
        Grades online quizzes based on the number of correct and incorrect answers.
        """
        self.assertEqual(class_exercises.grade_quiz(5,4), "Fail")

    #20

    def test_authenticate_user_case_1(self):
        """
        Authenticates users based on their username and password.
        """
        self.assertEqual(class_exercises.authenticate_user("admin","admin123"), "Admin")

    def test_authenticate_user_case_2(self):
        """
        Authenticates users based on their username and password.
        """
        self.assertEqual(class_exercises.authenticate_user("Admin","admin123"), "User")

    def test_authenticate_user_case_3(self):
        """
        Authenticates users based on their username and password.
        """
        self.assertEqual(class_exercises.authenticate_user("admin","Admin123"), "User")

    def test_authenticate_user_case_4(self):
        """
        Authenticates users based on their username and password.
        """
        self.assertEqual(class_exercises.authenticate_user("Henry","12345678"), "User")

    def test_authenticate_user_case_5(self):
        """
        Authenticates users based on their username and password.
        """
        self.assertEqual(class_exercises.authenticate_user("Henr","12345678"), "Invalid")

    def test_authenticate_user_case_6(self):
        """
        Authenticates users based on their username and password.
        """
        self.assertEqual(class_exercises.authenticate_user("Henry","1234567"), "Invalid")

    #21

    def test_get_weather_advisory_case_1(self):
        """
        Provides weather advisories based on temperature and humidity.
        """
        self.assertEqual(class_exercises.get_weather_advisory(31,71), "High Temperature and Humidity. Stay Hydrated.")

    def test_get_weather_advisory_case_2(self):
        """
        Provides weather advisories based on temperature and humidity.
        """
        self.assertEqual(class_exercises.get_weather_advisory(30,71), "No Specific Advisory")

    def test_get_weather_advisory_case_3(self):
        """
        Provides weather advisories based on temperature and humidity.
        """
        self.assertEqual(class_exercises.get_weather_advisory(31,70), "No Specific Advisory")

    def test_get_weather_advisory_case_4(self):
        """
        Provides weather advisories based on temperature and humidity.
        """
        self.assertEqual(class_exercises.get_weather_advisory(0,70), "No Specific Advisory")

    def test_get_weather_advisory_case_5(self):
        """
        Provides weather advisories based on temperature and humidity.
        """
        self.assertEqual(class_exercises.get_weather_advisory(-1,70), "Low Temperature. Bundle Up!")




if __name__ == '__main__':
    unittest.main()
