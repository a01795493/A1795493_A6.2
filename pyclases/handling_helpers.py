""""
handling_helpers.py
This module provides helper functions to handle data loading and saving.
It includes methods to load data from a JSON file and save data to a JSON file.
"""
import json
import os


class HandlingHelpers:
    """
    A class to handle data loading and saving.
    """
    def __init__(self):
        """
        Initialize the HandlingHelpers class.
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.project_dir = os.path.abspath(os.path.join(base_dir, ".."))

    def load_data(self, class_folder, filename):
        """
        Load data from a JSON file.
        Args:
            filename (str): The name of the file to load data from.
            Args:
            data (dict): The data to save to the file.
        Returns:
            dict: The loaded data.
        """
        file_path = os.path.join(self.project_dir, class_folder, filename)
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8-sig') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_data(self, class_folder, filename, data):
        """
        Save data to a JSON file.
        Args:
            filename (str): The name of the file to save data to.
            data (dict): The data to save to the file.
        """
        file_path = os.path.join(self.project_dir, class_folder, filename)
        try:
            with open(file_path, 'w', encoding='utf-8-sig') as file:
                json.dump(data, file, indent=4)
        except json.JSONDecodeError:
            with open(file_path, 'w', encoding='utf-8-sig') as file:
                json.dump({}, file, indent=4)
