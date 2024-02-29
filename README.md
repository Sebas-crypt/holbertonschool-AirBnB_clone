# AirBnB Clone - README

This project is an AirBnB clone that simulates a simplified version of the popular rental platform. It includes a set of Python classes representing various components such as Amenity, City, Place, Review, State, User, and a BaseModel serving as the base class for others.

## Table of Contents
Environment Setup
Installation
File Descriptions
Classes Inherited from BaseModel
Usage Example
Running Tests

## Environment Setup
Python 3.x
## Installation
Clone the repository to your local machine:

cd airbnb_clone

## File Descriptions
## BaseModel Class
The BaseModel class serves as the base class for all other classes. It includes attributes such as id, created_at, and updated_at. This class also provides methods for string representation, saving, and conversion to dictionaries.

## Amenity Class
The Amenity class represents an amenity that can be associated with a rental place. It inherits from the BaseModel class.

## City Class
The City class represents a city where rental places are located. It inherits from the BaseModel class.

## Place Class
The Place class represents a rental place with attributes like city_id, user_id, name, description, and others. It inherits from the BaseModel class.

## Review Class
The Review class represents a review for a rental place. It includes attributes such as place_id, user_id, and text. It inherits from the BaseModel class.

## State Class
The State class represents a state or region where rental places are situated. It inherits from the BaseModel class.

## User Class
The User class represents a user account. It includes attributes like email, password, first_name, and last_name. It inherits from the BaseModel class.

## FileStorage Class
The FileStorage class is a file storage system for objects in the AirBnB clone project. It provides methods for handling object storage in a JSON file.

## Classes Inherited from BaseModel
Amenity
City
Place
Review
State
User
## Usage Example

### Import the necessary classes
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

### Create instances of the classes
amenity = Amenity(name="Swimming Pool")
city = City(state_id="state_id_1", name="City Name")
place = Place(city_id="city_id_1", user_id="user_id_1", name="Cozy House", description="A lovely place to stay",
              number_rooms=2, number_bathrooms=1, max_guest=4, price_by_night=100, latitude=37.7749, longitude=-122.4194,
              amenity_ids=[amenity.id])
review = Review(place_id=place.id, user_id="user_id_2", text="Great experience!")
state = State(name="California")
user = User(email="user@example.com", password="password123", first_name="John", last_name="Doe")

### Access and modify attributes
print(f"Amenity Name: {amenity.name}")
amenity.name = "Gym"
print(f"Updated Amenity Name: {amenity.name}")

### Save the instances (assuming a working FileStorage)
amenity.save()
city.save()
place.save()
review.save()
state.save()
user.save()

### To retrieve all instances of a specific class
all_amenities = Amenity.all()
for amenity_instance in all_amenities.values():
    print(f"Amenity ID: {amenity_instance.id}, Name: {amenity_instance.name}")

### Accessing attributes through dictionaries
place_dict = place.to_dict()
print(f"Place Dictionary: {place_dict}")


### Running Tests
Run tests using the following command in your terminal:

python -m unittest discover -v

##Authors
Robert Santana
Sebastian Qui~ones