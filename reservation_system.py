""""
This module implements a simple hotel reservation system.
It allows creating hotels, customers, and reservations.g
It also provides functionality to cancel reservations.
"""
import unittest
from pyclases.hotel_class import Hotel
from pyclases.customer_class import Customer
from pyclases.reservation_class import Reservation


class TestHotelReservationSystem(unittest.TestCase):
    """
    Unit tests for the hotel reservation system.
    """
    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.customer_name = "Gustavo"
        self.hotel_name = "Hotel California"
        self.mail = "a01795493@tec.mx"
        self.location = "Mexico"
        self.rooms = 10

    def test_create_hotel(self):
        """
        Test the creation of a hotel.
        """
        result = Hotel.create_hotel(
            self.hotel_name,
            self.location,
            self.rooms)
        self.assertIn(result, [
            "Hotel created successfully.",
            "Hotel already exists."
        ])


    def test_modify_hotel(self):
        """
        Test the modification of a hotel.
        """
        result = Hotel.modify_hotel_info(
            self.hotel_name,
            self.location,
            self.rooms)
        self.assertIn(
            result, [
                "Hotel modified successfully.",
                "Hotel not found."
            ])

    def test_get_hotel_info(self):
        """
        Test the retrieval of hotel information.
        """
        result = Hotel.display_hotel_info(self.hotel_name)
        self.assertIn(
            result, [
                "Hotel not found.",
                "Hotel information retrieved successfully."
            ])

    def test_create_customer(self):
        """
        Test the creation of a customer.
        """
        result = Customer.create_customer(
            self.customer_name,
            self.mail)
        self.assertIn(
            result, [
                "Customer created successfully.",
                "Customer already exists."
            ])

    def test_modify_customer(self):
        """
        Test the modification of a customer.
        """
        result = Customer.modify_customer(
            self.customer_name,
            self.mail)
        self.assertIn(
            result, [
                "Customer information modified successfully.",
                "Customer not found."
            ])

    def test_get_customer_info(self):
        """
        Test the retrieval of customer information.
        """
        result = Customer.display_customer(self.customer_name)
        self.assertIn(
            result, [
                "Customer not found.",
                "Customer information retrieved successfully."
            ])

    def test_create_reservation(self):
        """
        Test the creation of a reservation.
        """
        result = Reservation.create_reservation(
            self.customer_name, self.hotel_name)
        self.assertIn(
            result, [
                "Reservation created successfully.",
                "Customer already have a reservation.",
                "No rooms available."
            ])

    def test_cancel_reservation(self):
        """
        Test the cancellation of a reservation.
        """
        result = Reservation.cancel_reservation(
            self.customer_name, self.hotel_name)
        self.assertIn(
            result, [
                "Reservation cancelled successfully.",
                "Reservation not found."
            ])

    def test_delete_customer(self):
        """
        Test the deletion of a customer.
        """
        result = Customer.delete_customer(self.customer_name)
        self.assertIn(
            result, [
                "Customer deleted successfully.",
                "Customer not found."
            ])

    def test_delete_hotel(self):
        """
        Test the deletion of a hotel.
        """
        result = Hotel.delete_hotel(self.hotel_name)
        self.assertIn(
            result, [
                "Hotel deleted successfully.",
                "Hotel not found."
            ])

if __name__ == "__main__":
    unittest.main()
