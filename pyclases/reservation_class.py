""""
 A class to represent a reservation system.
    It allows creating, deleting, and modifying reservations.
    It also provides functionality to check
    - available rooms
    - cancel reservations.
"""
import uuid
from pyclases.handling_helpers import HandlingHelpers


class Reservation:
    """
    A class to represent a customer.
    """
    class_folder = "reservation_info"
    hotel_folder = "hotel_info"
    file = "reservation.json"
    hotel_file = "hotel.json"
    customer_file = "customers.json"
    helpers = HandlingHelpers()

    @classmethod
    def create_reservation(cls, customer_name, hotel_name):
        """
        A class to create a new reservation.
        """
        reservation_id = str(uuid.uuid4())
        data = cls.helpers.load_data(cls.class_folder, cls.file)
        hotels = cls.helpers.load_data(cls.hotel_folder, cls.hotel_file)
        hotels_id = None
        reservation_id = None
        for r_id, reservation in data.items():
            if (
                reservation["hotel_name"] == hotel_name.lower() and
                reservation["customer_name"] == customer_name.lower()
            ):
                reservation_id = r_id
            break
        if reservation_id:
            return "Customer already have a reservation."
        for h_id, hotel in hotels.items():
            if hotel["name"] == hotel_name.lower():
                hotels_id = h_id
                break
        if hotels[hotels_id]["rooms"] == 0:
            return "No rooms available."
        data[reservation_id] = {
            "customer_name": customer_name.lower(),
            "hotel_name": hotel_name.lower(),
        }
        hotels[hotels_id]["rooms"] -= 1
        cls.helpers.save_data(cls.hotel_folder, cls.hotel_file, hotels)
        cls.helpers.save_data(cls.class_folder, cls.file, data)
        return "Reservation created successfully."

    @classmethod
    def cancel_reservation(cls, customer_name, hotel_name):
        """
        A class to cancel a reservation.
        Args:
            customer_name (str): The name of the customer.
            hotel_name (str): The name of the hotel.
        Returns:
            str: Success message or error message.
        """
        data = cls.helpers.load_data(cls.class_folder, cls.file)
        hotels = cls.helpers.load_data(cls.hotel_folder, cls.hotel_file)
        hotels_id = None
        reservation_id = None
        for r_id, reservation in data.items():
            if (
                reservation["customer_name"] == customer_name.lower() and
                reservation["hotel_name"] == hotel_name.lower()
            ):
                reservation_id = r_id
                break
        if reservation_id:
            del data[reservation_id]
            cls.helpers.save_data(cls.class_folder, cls.file, data)
            for h_id, hotel in hotels.items():
                if hotel["name"] == hotel_name.lower():
                    hotels_id = h_id
                    break
            if hotels_id:
                hotels[hotels_id]["rooms"] += 1
            cls.helpers.save_data(cls.hotel_folder, cls.hotel_file, hotels)
            return "Reservation cancelled successfully."
        return "Reservation not found."
