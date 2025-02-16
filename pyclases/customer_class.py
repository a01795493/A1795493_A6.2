"""
Methods to handle the next persistent behaviors (stored in files):
1. Customers
    a. Create Customer
    b. Delete Customer
    c. Display Customer information
    d. Modify Customer Information
"""
import uuid
from pyclases.handling_helpers import HandlingHelpers


class Customer:
    """
    A class to represent a customer.
    """
    class_folder = "customer_info"
    file = "customers.json"
    helpers = HandlingHelpers()

    @classmethod
    def create_customer(cls, name, email):
        """"
        Create a new customer.
        Args:
            customer_id (str): The ID of the customer.
            name (str): The name of the customer.
            email (str): The email of the customer.
        Returns:
            str: Success message.
        """
        data = cls.helpers.load_data(cls.class_folder, cls.file)
        customer_id = None
        for c_id, customer in data.items():
            if customer["name"] == name.lower():
                customer_id = c_id
                break
        if not customer_id or data == {}:
            customer_id = str(uuid.uuid4())
            data[customer_id] = {
                "name": name.lower(),
                "email": email.lower()
            }
            cls.helpers.save_data(cls.class_folder, cls.file, data)
            return "Customer created successfully."
        return "Customer already exists."

    @classmethod
    def delete_customer(cls, customer_name):
        """
        Delete an existing customer.
        Args:
            customer_name (str): The name of the customer.
        Returns:
            str: Success message or error message.
        """
        data = cls.helpers.load_data(cls.class_folder, cls.file)
        customer_id = None
        for c_id, customer in data.items():
            if customer["name"] == customer_name.lower():
                customer_id = c_id
                break
        if customer_id:
            del data[customer_id]
            cls.helpers.save_data(cls.class_folder, cls.file, data)
            return "Customer deleted successfully."
        return "Customer not found."

    @classmethod
    def display_customer(cls, customer_name):
        """
        Display customer information.
        Args:
            customer_name (str): The name of the customer.
        Returns:
            str: Customer information or error message.
        """
        data = cls.helpers.load_data(cls.class_folder, cls.file)
        for _, customer in data.items():
            if customer["name"] == customer_name.lower():
                return (f"Customer Name: {customer['name']}, "
                        f"Customer Email: {customer['email']}")
        return "Customer not found."

    @classmethod
    def modify_customer(cls, name, email):
        """
        Modify customer information.
        Args:
            name (str): The name of the customer.
            email (str): The new email of the customer.
        Returns:
            str: Success message or error message.
        """
        data = cls.helpers.load_data(cls.class_folder, cls.file)
        customer_id = None
        for c_id, customer in data.items():
            if customer["name"] == name.lower():
                customer_id = c_id
                break
        if customer_id:
            data[customer_id]["email"] = email.lower()
            cls.helpers.save_data(cls.class_folder, cls.file, data)
            return "Customer information modified successfully."
        return "Customer not found."
