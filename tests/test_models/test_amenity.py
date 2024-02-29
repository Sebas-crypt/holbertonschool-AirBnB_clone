#!/usr/bin/python3
"""Unittest for the Amenity Class """
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def test_init(self):
        """
        Test the initialization of an Amenity instance.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "")

    def test_attributes(self):
        """
        Test the attributes of an Amenity instance.
        """
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_to_dict(self):
        """
        Test the to_dict method of an Amenity instance.
        """
        amenity = Amenity()
        amenity.name = "Gym"
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict["name"], "Gym")
        self.assertEqual(amenity_dict["__class__"], "Amenity")

    def test_from_dict(self):
        """
        Test the from_dict method of the Amenity class.
        """
        amenity_dict = {
            "name": "Sauna",
            "__class__": "Amenity",
            "id": "123",
            "created_at": "2022-01-01T00:00:00.000000",
            "updated_at": "2022-01-01T00:00:00.000000"
        }
        amenity = Amenity(**amenity_dict)
        self.assertEqual(amenity.name, "Sauna")
        self.assertEqual(amenity.id, "123")
        self.assertEqual(amenity.created_at.isoformat(), "2022-01-01T00:00:00.000000")
        self.assertEqual(amenity.updated_at.isoformat(), "2022-01-01T00:00:00.000000")

if __name__ == '__main__':
    unittest.main()
