#!/usr/bin/python3
"""unittest of the Place Class"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    This class contains unit tests for the Place class.
    """

    def test_init(self):
        """
        Test the initialization of a Place instance with custom attributes.
        """
        place = Place(city_id="123", user_id="456", name="Test Place")
        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "Test Place")

    def test_attribute_types(self):
        """
        Test the types of attributes in a Place instance.
        """
        place = Place()
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_inheritance(self):
        """
        Test that Place is a subclass of BaseModel.
        """
        place = Place()
        self.assertTrue(issubclass(type(place), BaseModel))

    def test_str_representation(self):
        """
        Test the __str__ method of the Place class.
        """
        place = Place(name="Test Place")
        expected_str = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(str(place), expected_str)

    def test_to_dict_method(self):
        """
        Test the to_dict method of the Place class.
        """
        place = Place(name="Test Place")
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict["name"], "Test Place")
        self.assertEqual(place_dict["__class__"], "Place")

    def test_from_dict_method(self):
        """
        Test the from_dict method of the Place class.
        """
        place_dict = {
            "id": "123",
            "name": "Test Place",
            "__class__": "Place"
        }
        place = Place.from_dict(place_dict)
        self.assertIsInstance(place, Place)
        self.assertEqual(place.id, "123")
        self.assertEqual(place.name, "Test Place")

if __name__ == '__main__':
    unittest.main()
