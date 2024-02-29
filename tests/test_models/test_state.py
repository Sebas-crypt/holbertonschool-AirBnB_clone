#1/usr/bin/python3
"""unittest of the State Class"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def test_state_attributes(self):
        """
        Test case to verify the attributes of the State instance.
        """
        state = State()
        self.assertEqual(state.name, "")

    def test_attributes_existence(self):
        """Test that the instance has all the expected attributes."""
        self.assertTrue(hasattr(self.state_instance, "name"))
        self.assertTrue(hasattr(self.state_instance, "id"))
        self.assertTrue(hasattr(self.state_instance, "created_at"))
        self.assertTrue(hasattr(self.state_instance, "updated_at"))

    def test_state_inheritance(self):
        """
        Test case to verify the inheritance of the State class.
        """
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_state_init(self):
        """
        Test case to verify the initialization of the State instance.
        """
        state = State(id="123", created_at="2022-01-01T00:00:00", updated_at="2022-01-01T00:00:00")
        self.assertEqual(state.id, "123")
        self.assertEqual(state.created_at, "2022-01-01T00:00:00")
        self.assertEqual(state.updated_at, "2022-01-01T00:00:00")

    def test_state_name(self):
        """
        Test case to verify the name attribute of the State instance.
        """
        state = State()
        self.assertEqual(state.name, "")

        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_state_str(self):
        """
        Test case to verify the __str__ method of the State instance.
        """
        state = State()
        state.name = "New York"
        expected_str = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str(state), expected_str)

    def test_state_to_dict(self):
        """
        Test case to verify the to_dict method of the State instance.
        """
        state = State()
        state.name = "Texas"
        state_dict = state.to_dict()
        self.assertEqual(state_dict["name"], "Texas")
        self.assertEqual(state_dict["__class__"], "State")

    def test_state_from_dict(self):
        """
        Test case to verify the from_dict method of the State class.
        """
        state_dict = {
            "id": "456",
            "created_at": "2022-02-01T00:00:00",
            "updated_at": "2022-02-01T00:00:00",
            "name": "Florida",
            "__class__": "State"
        }
        state = State.from_dict(state_dict)
        self.assertEqual(state.id, "456")
        self.assertEqual(state.created_at, "2022-02-01T00:00:00")
        self.assertEqual(state.updated_at, "2022-02-01T00:00:00")
        self.assertEqual(state.name, "Florida")

if __name__ == '__main__':
    unittest.main()
