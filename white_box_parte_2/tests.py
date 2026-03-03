# -*- coding: utf-8 -*-

import re
import unittest
import class_exercise

#22

class TestVendingMachine(unittest.TestCase):
    """
    Vending Machine Unit Test.
    """
    def setUp(self):
        self.vending_machine = class_exercise.VendingMachine()
        self.assertEqual(self.vending_machine.state, "Ready")

    def test_insert_coin_fail(self):
        """
        Checks if the vending machine works when you insert a coin.
        """

        self.vending_machine.state = "Dispensing"
        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Invalid operation in current state.")

    def test_insert_coin_success(self):
        """
        Checks if the vending machine works when you insert a coin.
        """

        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Coin Inserted. Select your drink.")

    def test_select_drink_success(self):
        """
        Checks if the vending machine can dispense a drink
        """
        self.vending_machine.state = "Dispensing"
        output = self.vending_machine.select_drink()

        self.assertEqual(self.vending_machine.state, "Ready")
        self.assertEqual(output, "Drink Dispensed. Thank you!")

    def test_select_drink_fail(self):
        """
        Checks if the vending machine can dispense a drink
        """

        output = self.vending_machine.select_drink()

        self.assertEqual(self.vending_machine.state, "Ready")
        self.assertEqual(output, "Invalid operation in current state.")

#23

class TestTrafficLight(unittest.TestCase):
    """
    A traffic light system with three states: "Green," "Yellow," and "Red."
    """
    def setUp(self):
        self.traffic_light = class_exercise.TrafficLight()
        self.assertEqual(self.traffic_light.state, "Red")

    def test_change_state_red_to_green_success(self):
        """
        Checks if traffic light can change from red to green
        """

        current_state= self.traffic_light.get_current_state()

        self.assertEqual(current_state, "Red")

        self.traffic_light.change_state()

        self.assertEqual(self.traffic_light.state, "Green")

    def test_change_state_green_to_yellow(self):
        """
        Checks if traffic light can change from green to yellow
        """

        self.traffic_light.change_state()

        current_state= self.traffic_light.get_current_state()

        self.assertEqual(current_state, "Green")

        self.traffic_light.change_state()

        self.assertEqual(self.traffic_light.state, "Yellow")

    def test_change_state_yellow_to_red(self):
        """
        Checks if traffic light can change from yellow to red
        """

        self.traffic_light.change_state()
        self.traffic_light.change_state()

        current_state= self.traffic_light.get_current_state()

        self.assertEqual(current_state, "Yellow")

        self.traffic_light.change_state()

        self.assertEqual(self.traffic_light.state, "Red")

#24

class TestUserAuthentication(unittest.TestCase):
    """
    A user authentication system with states "Logged Out" and "Logged In."
    """
    def setUp(self):
        self.user = class_exercise.UserAuthentication()
        self.assertEqual(self.user.state, "Logged Out")

    def test_login_fail(self):
        """
        Checks the function to log in
        """

        self.user.state = "Logged In"
        output = self.user.login()

        self.assertEqual(self.user.state, "Logged In")
        self.assertEqual(output, "Invalid operation in current state")

    def test_login_success(self):
        """
        Checks the function to log in
        """


        output = self.user.login()

        self.assertEqual(self.user.state, "Logged In")
        self.assertEqual(output, "Login successful")

    def test_logout_fail(self):
        """
        Checks the function to log out
        """


        output = self.user.logout()

        self.assertEqual(self.user.state, "Logged Out")
        self.assertEqual(output, "Invalid operation in current state")

    def test_logout_success(self):
        """
        Checks the function to log out
        """

        self.user.state = "Logged In"
        output = self.user.logout()

        self.assertEqual(self.user.state, "Logged Out")
        self.assertEqual(output, "Logout successful")

#25

class TestDocumentEditingSystem(unittest.TestCase):
    """
    A document editing system with states "Editing" and "Saved."
    """

    def setUp(self):
        self.document_editing_system = class_exercise.DocumentEditingSystem()
        self.assertEqual(self.document_editing_system.state, "Editing")

    def test_save_document_fail(self):
        """
        Checks the function to save a document.
        """

        self.document_editing_system.state = "Saved"
        output = self.document_editing_system.save_document()

        self.assertEqual(self.document_editing_system.state, "Saved")
        self.assertEqual(output, "Invalid operation in current state")

    def test_save_document_success(self):
        """
        Checks the function to save a document.
        """

        output = self.document_editing_system.save_document()

        self.assertEqual(self.document_editing_system.state, "Saved")
        self.assertEqual(output, "Document saved successfully")

    def test_edit_document_fail(self):
        """
        Checks the function to edit a document.
        """

        output = self.document_editing_system.edit_document()

        self.assertEqual(self.document_editing_system.state, "Editing")
        self.assertEqual(output, "Invalid operation in current state")

    def test_edit_document_success(self):
        """
        Checks the function to edit a document.
        """
        self.document_editing_system.state = "Saved"
        output = self.document_editing_system.edit_document()

        self.assertEqual(self.document_editing_system.state, "Editing")
        self.assertEqual(output, "Editing resumed")

#26

class TestElevatorSystem(unittest.TestCase):
    """
    An elevator system with states "Idle," "Moving Up," and "Moving Down."
    """
    def setUp(self):
        self.elevator_system = class_exercise.ElevatorSystem()
        self.assertEqual(self.elevator_system.state, "Idle")

    def test_move_up_fail(self):
        """
        Checks the function to move an elevator.
        """

        self.elevator_system.state = "Moving Up"
        output = self.elevator_system.move_up()

        self.assertEqual(self.elevator_system.state, "Moving Up")
        self.assertEqual(output, "Invalid operation in current state")

    def test_move_up_success(self):
        """
        Checks the function to move up an elevator.
        """

        output = self.elevator_system.move_up()

        self.assertEqual(self.elevator_system.state, "Moving Up")
        self.assertEqual(output, "Elevator moving up")

    def test_move_down_fail(self):
        """
        Checks the function to move down an elevator.
        """

        self.elevator_system.state = "Moving Down"
        output = self.elevator_system.move_down()

        self.assertEqual(self.elevator_system.state, "Moving Down")
        self.assertEqual(output, "Invalid operation in current state")

    def test_move_down_success(self):
        """
        Checks the function to move down an elevator.
        """

        output = self.elevator_system.move_down()

        self.assertEqual(self.elevator_system.state, "Moving Down")
        self.assertEqual(output, "Elevator moving down")

    def test_stop_fail(self):
        """
        Checks the function to stop an elevator.
        """

        output = self.elevator_system.stop()

        self.assertEqual(self.elevator_system.state, "Idle")
        self.assertEqual(output, "Invalid operation in current state")

    def test_stop_move_up(self):
        """
        Checks the function to stop an elevator moving up.
        """
        self.elevator_system.state = "Moving Up"
        output = self.elevator_system.stop()

        self.assertEqual(self.elevator_system.state, "Idle")
        self.assertEqual(output, "Elevator stopped")

    def test_stop_move_down(self):
        """
        Checks the function to stop an elevator moving down.
        """
        self.elevator_system.state = "Moving Down"
        output = self.elevator_system.stop()

        self.assertEqual(self.elevator_system.state, "Idle")
        self.assertEqual(output, "Elevator stopped")
