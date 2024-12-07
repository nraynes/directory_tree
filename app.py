"""
app.py

This module is the entry point of this file system application. Running this file will
start the file system application and allow the user to add, move, and delete items in the
file system.

Example usage:
    python3 <path_to_project>/app.py
"""
from file_system import FileSystem

file_system = FileSystem()

file_system.start()
