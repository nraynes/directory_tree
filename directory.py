"""
directory.py

This module contains the Directory class, which models a directory in a file system.
The Directory class provides methods for adding, removing, and listing files and subdirectories,
allowing for easy management of directory contents.

Example usage:
    folder = Directory("Documents")
    folder.add(Directory("school"))
    folder.list_contents()  # Output: school
    folder.remove("school")
    removed_folder = folder.pop("school")
    sub_folder = folder.open("school")
"""
from typing import Optional, Self


class Directory:
    """
    Class modeling a directory in a file system.
    """

    def __init__(self, name: str, is_root: bool = False):
        """
        Initializes the Directory object.
        :param name: The name of this Directory.
        """
        self.name = name
        self._is_root = is_root
        self._contents = {}

    @property
    def name(self) -> str:
        """
        Getter for this object's _name attribute.
        :return: The name of this directory.
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Setter for this object's _name attribute.
        :param value: The new name of this directory.
        """
        self._name = value

    @property
    def contents(self) -> dict[str, Self]:
        """
        Getter for this object's _contents attribute.
        :return: The contents of this directory.
        """
        return self._contents

    def add(self, directory: Self) -> None:
        """
        Adds a subdirectory to this directory.
        :param directory: The subdirectory to add to this directory.
        """
        self._contents[directory.name] = directory

    def remove(self, name: str) -> None:
        """
        Removes a subdirectory from this directory.
        :param name: The name of the subdirectory to remove from this directory.
        """
        if name in self._contents:
            del self._contents[name]

    def pop(self, name: str) -> Optional[Self]:
        """
        Removes a subdirectory from this directory and returns it.
        :param name: The name of the subdirectory to remove from this directory.
        :return: The subdirectory that was removed.
        """
        if name in self._contents:
            return self._contents.pop(name)
        return None

    def open(self, name: str) -> Optional[Self]:
        """
        Retrieves a subdirectory contained in this directory.
        :param name: The name of the subdirectory to open.
        :return: The subdirectory, if it exists.
        """
        try:
            return self._contents[name]
        except KeyError:
            return None

    def list_contents(self, tab_count: int = 0) -> None:
        """
        Prints the contents of this directory to the console.
        :param tab_count: How many tabs to prepend to output.
        """
        if not self._is_root:
            print(f"{"".join(['  ' for _ in range(tab_count)])}{self._name}")
        else:
            tab_count -= 1
        for subdirectory in sorted(self._contents.values(), key=lambda item: item.name):
            subdirectory.list_contents(tab_count+1)
