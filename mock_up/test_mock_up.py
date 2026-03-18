# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch, MagicMock
import io
import mockup_exercises
import subprocess

class TestFetchDataFromAPI(unittest.TestCase):
    """
    Class to test the function to fetch data from API
    """

    @patch("mockup_exercises.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """
        Checks that the function can success in the process
        """

        mock_get.return_value.json.return_value = {"key":"value"}

        result = mockup_exercises.fetch_data_from_api("https://api.example.com/data")

        self.assertEqual(result, {"key": "value"})

        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)

class TestReadDataFromFile(unittest.TestCase):
    """
    Class to test the function to read data from a file
    """

    @patch('builtins.open', create=True)
    def test_read_data_from_file_success(self, mock_open):
        """
        Checks if the function can read a file
        """
        fake_file = io.StringIO("data")
        mock_open.return_value = fake_file
        result = mockup_exercises.read_data_from_file("Data Base")
        self.assertEqual(result, "data")

    @patch('builtins.open', create=False)
    def test_read_data_from_file_fail(self, mock_open):
        """
        Checks the function if there's not a file
        """

        result = mockup_exercises.read_data_from_file("Data Base")
        self.assertRaises(FileNotFoundError)

class TestExecuteCommand(unittest.TestCase):
    """
    Class that checks the function for execute a command in a subprocess
    """
    @patch("mockup_exercises.subprocess.run")
    def test_execute_command_success(self, mock_run):
        """
        Checks the function to execute a command
        """
        mock_result = MagicMock()
        mock_result.stdout = "Success"
        mock_run.return_value = mock_result

        result = mockup_exercises.execute_command("fastfetch")
        self.assertEqual(result, "Success")
        mock_run.assert_called_once_with("fastfetch", capture_output=True, check=False, text=True)

    @patch("mockup_exercises.subprocess.run")
    def test_execute_command_fail(self, mock_run):

        result = mockup_exercises.execute_command("fastfetch")
        self.assertRaises(subprocess.CalledProcessError)

class TestPerformActionBasedOnTime(unittest.TestCase):
    """
    Class that checks the function to perform an action based on time
    """

    @patch("mockup_exercises.time.time")
    def test_perform_action_based_on_time_action_a(self, mock_time):
        """
        Checks the function performing the action A
        """
        mock_time.return_value = 3
        result = mockup_exercises.perform_action_based_on_time()
        self.assertEqual(result, "Action A")

    @patch("mockup_exercises.time.time")
    def test_perform_action_based_on_time_action_b(self, mock_time):
        """
        Checks the function performing the action A
        """
        mock_time.return_value = 12
        result = mockup_exercises.perform_action_based_on_time()
        self.assertEqual(result, "Action B")
