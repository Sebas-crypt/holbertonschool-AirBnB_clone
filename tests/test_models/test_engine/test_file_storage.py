#!/usr/bin/python3
import unittest
from json import dumps
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestAll(unittest.TestCase):
    """test the method all"""
    def test_no_arguments(self):
        """test without args"""
        test_instance = FileStorage()
        self.assertEqual(test_instance.all(), FileStorage._FileStorage__objects)

    def test_objects_type(self):
        """test the type of the obj"""
        test_instance = FileStorage()

        for obj in test_instance.all().values():
            self.assertIsInstance(obj, dict)

    def test_arguments(self):
        """test with args"""
        test_instance = FileStorage()
        with self.assertRaises(TypeError):
            test_instance.all("never gonna give you up")


class TestNew(unittest.TestCase):
    """test the method New"""
    def test_no_arguments(self):
        """test without args"""
        test_instance = FileStorage()
        with self.assertRaises(TypeError):
            test_instance.new()

    def test_more_arguments(self):
        """test with args"""
        test_instance = FileStorage()
        with self.assertRaises(TypeError):
            test_instance.new("I don't know", complex(float(), int()))


class TestSave(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()

    def test_file_path(self):
        """Test __file_path attribute"""
        self.assertTrue(hasattr(self.storage, "_FileStorage__file_path"))
        self.assertIsInstance(self.storage._FileStorage__file_path, str)

    """test the method save"""
    def test_no_arguments(self):
        """test without args"""
        test_instance = FileStorage()
        test_instance.save()

        with open(FileStorage._FileStorage__file_path, "r") as file:
            expected_output = dumps(test_instance.all())
            self.assertEqual(file.read(), expected_output)

    def test_arguments(self):
        """test with args"""
        test_instance = FileStorage()
        with self.assertRaises(TypeError):
            test_instance.save("hi")

class testReload(unittest.TestCase):
    """test the method reload"""
    def test_reload_correcly(self):
        """test if the  reload convert to __obj"""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, storage.all())

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()

    def test_file_path(self):
        """Test __file_path attribute"""
        storage = FileStorage()
        self.assertTrue(hasattr(storage, "_FileStorage__file_path"))
        self.assertIsInstance(storage._FileStorage__file_path, str)
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_initial_objects(self):
        """Test initial value of __objects"""
        self.assertEqual(self.storage._FileStorage__objects, {})

    def test_add_object(self):
        """Test adding object to __objects"""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(f"BaseModel.{obj.id}", self.storage._FileStorage__objects)

    def test_remove_object(self):
        """Test removing object from __objects"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        self.storage.delete(obj)
        self.assertNotIn(f"BaseModel.{obj.id}", self.storage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
