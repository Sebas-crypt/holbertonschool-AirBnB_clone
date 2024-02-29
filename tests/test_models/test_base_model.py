#!/usr/bin/python3
"""unittest for the class BaseModel"""
import unittest
import os
from models.base_model import BaseModel
import uuid
from datetime import datetime


class TestModel(unittest.TestCase):
    """This class contains unit tests for the BaseModel class."""

    def test_Class(self):
        """Test the initialization of the BaseModel class."""
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))
        self.assertEqual(model.created_at, model.updated_at)

    def test_diferent_id(self):
        """Test that different instances of BaseModel have different ids."""
        model_1 = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model_1.id, model_2.id)

    def test_init_with_kwargs(self):
        """Test initialization with keyword arguments."""
        kwargs = {
            "id": "123",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }

        model = BaseModel(**kwargs)
        for key, value in kwargs.items():
            if key in ["created_at", "updated_at"]:
                self.assertEqual(getattr(model, key).isoformat(), value)
            else:
                self.assertEqual(getattr(model, key), value)

    def test_str(self):
        """Test the __str__ method of BaseModel."""
        model = BaseModel()
        The_str = f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}"
        self.assertEqual(model.__str__(), The_str)

    def test_double_check_update_not_save(self):
        """Test that the updated not change if is call more than twice."""
        model = BaseModel()
        time_1 = model.updated_at
        time_2 = model.updated_at
        self.assertEqual(time_1, time_2)

    def test_save(self):
        """Test the save method of BaseModel."""
        model = BaseModel()
        time_1 = model.updated_at
        model.my_number = 89
        model.save()
        time_2 = model.updated_at
        self.assertNotEqual(time_1, time_2)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertTrue(isinstance(model_dict, dict))
        self.assertTrue(isinstance(model, BaseModel))

    def test_init_with_args(self):
        """Test initialization with positional arguments."""
        args = ["123", datetime.now().isoformat(), datetime.now().isoformat()]

        model = BaseModel(*args)
        self.assertEqual(model.id, args[0])
        self.assertEqual(model.created_at.isoformat(), args[1])
        self.assertEqual(model.updated_at.isoformat(), args[2])

    @classmethod
    def tearDownClass(cls):
        """Clean up files (if any) created during the tests."""
        try:
            os.remove("file.json")  # Adjust filename as necessary
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
