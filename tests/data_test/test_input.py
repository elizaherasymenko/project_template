import unittest
from unittest.mock import mock_open, patch
import pandas as pd
from app.io.input import read_file_builtin, read_file_with_pandas

class TestFileReadingOperations(unittest.TestCase):

    # Tests for the function read_file_builtin
    @patch("builtins.open", mock_open(read_data="Hello, world!"))
    def test_read_file_builtin_successfully(self):
        """Test the correct reading of data from a file"""
        result = read_file_builtin("data/test_file.txt")
        self.assertEqual(result, "Hello, world!")

    @patch("builtins.open", mock_open(read_data=""))
    def test_read_file_builtin_empty_file(self):
        """Test when reading from an empty file"""
        result = read_file_builtin("data/empty_file.txt")
        self.assertEqual(result, "")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_file_builtin_not_found(self, mock_file):
        """Test when attempting to read a file that does not exist"""
        with self.assertRaises(FileNotFoundError):
            read_file_builtin("data/non_existent_file.txt")

    # Tests for the function read_file_with_pandas
    @patch("pandas.read_csv", return_value=pd.DataFrame({"Animal": ["Dog", "Cat", "Parrot", "Crocodile"], "Name": ["Baron", "Pushok", "Kesha", "Sanya"]}))
    def test_read_file_with_pandas_successfully(self, mock_read_csv):
        """Test successful reading of CSV data using pandas"""
        result = read_file_with_pandas("data/test_data.csv")
        expected_result = pd.DataFrame({"Animal": ["Dog", "Cat", "Parrot", "Crocodile"], "Name": ["Baron", "Pushok", "Kesha", "Sanya"]})
        pd.testing.assert_frame_equal(result, expected_result)

    @patch("pandas.read_csv", return_value=pd.DataFrame())
    def test_read_file_with_pandas_empty_csv(self, mock_read_csv):
        """Test for reading an empty CSV file with pandas"""
        result = read_file_with_pandas("data/empty_data.csv")
        expected_result = pd.DataFrame()
        pd.testing.assert_frame_equal(result, expected_result)

    @patch("pandas.read_csv", side_effect=FileNotFoundError)
    def test_read_file_with_pandas_file_not_found(self, mock_file):
        """Test for handling the case when trying to read a non-existent CSV file"""
        with self.assertRaises(FileNotFoundError):
            read_file_with_pandas("data/non_existent_data.csv")


if __name__ == "__main__":
    unittest.main()