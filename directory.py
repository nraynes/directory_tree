"""
directory.py

This module contains the Directory class, which models a directory
in a file system. The Directory class provides methods for adding,
removing, and listing files and subdirectories, allowing for easy
management of directory contents.

Example usage:
    my_directory = Directory("Documents")
    my_directory.add_file("resume.pdf")
    my_directory.list_contents()  # Output: ['resume.pdf']
    my_directory.remove_file("resume.pdf")
"""

class Directory:
    def __init__(self, name):
        self.name = name
        self.contents = []

    def add_file(self, file_name):
        """Adds a file to the directory."""
        self.contents.append(file_name)

    def remove_file(self, file_name):
        """Removes a file from the directory."""
        self.contents.remove(file_name)

    def list_contents(self):
        """Returns a list of files in the directory."""
        return self.contents
