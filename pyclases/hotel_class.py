"""
Methods to handle the next persistent behaviors (stored in files):
1. Hotels
    a. Create Hotel
    b. Delete Hotel
    c. Display Hotel information
    d. Modify Hotel Information
    e. Reserve a Room
    f. Cancel a Reservation
"""
import uuid
from pyclases.handling_helpers import HandlingHelpers
from pyclases.reservation_class import Reservation


class Hotel:
    """
    A class to represent a hotel.
    """
    class_folder = "hotel_info"
    file = "hotel.json"
    helpers = HandlingHelpers()
    reservation = Reservation()

    @classmethod
    def create_hotel(cls, name, location, rooms):
        """
        Create a new hotel.
        Args:
            hotel_id (str): The ID of the hotel.
            name (str): The name of the hotel.
            location (str): The location of the hotel.
            rooms (int): The number of rooms in the hotel.
        Returns:
            str: Success message.
        """
        data = cls.helpers.load_data(cls.class_folder, cls.file)
        hotel_id = None
        for h_id, hotel in data.items():
            if hotel["name"] == name.lower():
                hotel_id = h_id
                break
        if not hotel_id or data == {}:
            hotel_id = str(uuid.uuid4())
            data[hotel_id] = {
                "name": name.lower(),
                "location": location.lower(),
                "rooms": rooms
            }
            cls.helpers.save_data(cls.class_folder, cls.file, data)
            return "Hotel created successfully."
        return "Hotel already exists."

    @classmethod
    def delete_hotel(cls, name):
        """
        Delete an existing hotel.
        Args:
            name (str): The name of the hotel.
        Returns:
            str: Success message or error message.
        """
        data = cls.helpers.load_data(cls.class_folder, cls.file)
        hotel_id = None
        for h_id, hotel in data.items():
            if hotel["name"] == name.lower():
                hotel_id = h_id
                break
        if hotel_id:
            del data[hotel_id]
            cls.helpers.save_data(cls.class_folder, cls.file, data)
            return "Hotel deleted successfully."
        return "Hotel not found."

    @classmethod
    def display_hotel_info(cls, name):
        """
        Display hotel information.
        Args:
            name (str): The name of the hotel.
        Returns:
            str: Hotel information or error message.
        """
        data = cls.helpers.load_data(cls.class_folder, cls.file)
        for hotel in data.values():
            if hotel["name"] == name.lower():
                return (
                        f"Hotel Name: {hotel['name']}, "
                        f"Location: {hotel['location']}, "
                        f"Rooms: {hotel['rooms']}")
        return "Hotel not found."

    @classmethod
    def modify_hotel_info(cls, name=None, location=None, rooms=None):
        """
        Modify hotel information by hotel name.
        Args:
            name (str): The new name of the hotel.
            location (str): The new location of the hotel.
            rooms (int): The new number of rooms in the hotel.
        Returns:
            str: Success message or error message.
        """
        data = cls.helpers.load_data(cls.class_folder, cls.file)
        hotel_id = None
        for h_id, hotel in data.items():
            if hotel["name"] == name.lower():
                hotel_id = h_id
                break
        if hotel_id:
            if name:
                data[hotel_id]["name"] = name.lower()
            if location:
                data[hotel_id]["location"] = location.lower()
            if rooms:
                data[hotel_id]["rooms"] = rooms
            cls.helpers.save_data(cls.class_folder, cls.file, data)
            return "Hotel information modified successfully."
        return "Hotel not found."

    @classmethod
    def reserve_room(cls, customer_name, hotel_name):
        """
        Reserve a room in a hotel.
        Args:
            customer_name (str): The name of the customer.
            hotel_name (str): The name of the hotel.
        Returns:
            str: Success message or error message.
        """
        cls.reservation.create_reservation(customer_name, hotel_name)
        return "Room reserved successfully."

    @classmethod
    def cancel_reservation(cls, customer_name, hotel_name):
        """
        Cancel a reservation.
        Args:
            customer_name (str): The name of the customer.
            hotel_name (str): The name of the hotel.
        Returns:
            str: Success message or error message.
        """
        cls.reservation.cancel_reservation(customer_name, hotel_name)
        return "Reservation cancelled successfully."
