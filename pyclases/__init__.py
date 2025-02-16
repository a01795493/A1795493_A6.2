"""
Module for handling hotel management system classes.
"""
import os
import glob

modules = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
__all__ = [
    os.path.basename(f)[:-3]
    for f in modules
    if f.endswith(".py") and os.path.basename(f) != '__init__.py'
    ]
