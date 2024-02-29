#!/usr/bin/python3
"""Unittest for the City class"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    This class contains unit tests for the City class.
    """

    def setUp(self):
        """
        Set up the test fixture. This method is called before each test method.
        """
        self.city = City()

    def test_state_id(self):
        """
        Test the state_id attribute of the City class.
        """
        self.assertEqual(self.city.state_id, "")

    def test_name(self):
        """
        Test the name attribute of the City class.
        """
        self.assertEqual(self.city.name, "")

    def test_attributes(self):
        """
        Test the existence of certain attributes in the City class.
        """
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_inheritance(self):
        """
        Test if the City class inherits from the BaseModel class.
        """
        self.assertIsInstance(self.city, BaseModel)

    def test_str_representation(self):
        """
        Test the string representation of the City class.
        """
        expected = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected)

if __name__ == '__main__':
    unittest.main()
