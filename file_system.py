"""
file_system.py

This module contains the FileSystem class, which represents a hierarchical file system.

Example usage:
    file_system = FileSystem()
    folder.start()
"""
from directory import Directory
from typing import Optional


class FileSystem:
    """
    Main application class for controlling a file system.
    """

    def __init__(self):
        """
        Initializes the app.
        """
        self._root = Directory("Root", is_root=True)
        self._not_found = None  # Used to store directory name not found in recursive search.

    def _get_dir_from_path(self, path: list[str], current_dir: Optional[Directory] = None) -> Optional[Directory]:
        """
        Retrieves the directory at the path provided.
        :param path: The path to the directory to retrieve.
        :param current_dir: Current directory from recursive call.
        :return: The directory at the path provided.
        """
        if len(path) > 0:  # Ensure path provided isn't empty.
            if current_dir is None:
                current_dir = self._root

            #Ensure next directory in path exists.
            next_dir = current_dir.open(path[0])
            if next_dir is not None:
                if len(path) > 1:
                    # Recursively go through every directory in path until the last one.
                    return self._get_dir_from_path(path[1:], next_dir)
                elif len(path) == 1:
                    # If path is length 1, then this is the directory we need.
                    return next_dir
                else:
                    # If path is empty, just return the root directory.
                    return self._root

        # If not directory was found, save the path to the missing directory for later logging.
        self._not_found = path[0]
        return None

    def create_dir(self, path: str) -> None:
        """
        Creates a directory in the file system.
        :param path: The path to the new directory.
        """
        # Acquire directory that will contain the new directory.
        split_path = path.split("/")
        new_dir_name = split_path[-1]
        dir_to_add_to = self._get_dir_from_path(split_path[0:-1]) if len(split_path) > 1 else self._root

        # Ensure the directory exists, then add it.
        if dir_to_add_to is not None:
            dir_to_add_to.add(Directory(new_dir_name))
        else:
            print(f"Cannot create {path} - {self._not_found} does not exist")

    def delete_dir(self, path: str) -> None:
        """
        Deletes a directory from the file system.
        :param path: The path to the directory to delete.
        """
        # Acquire directory containing the directory that needs to be deleted.
        split_path = path.split("/")
        name_of_dir_to_delete = split_path[-1]
        dir_to_remove_dir_from = self._get_dir_from_path(split_path[0:-1]) if len(split_path) > 1 else self._root

        # Ensure all directories exist, then remove the directory.
        if dir_to_remove_dir_from is not None:
            dir_to_delete = dir_to_remove_dir_from.open(name_of_dir_to_delete)
            if dir_to_delete is not None:
                dir_to_remove_dir_from.remove(name_of_dir_to_delete)
            else:
                print(f"Cannot delete {path} - {name_of_dir_to_delete} does not exist")
        else:
            print(f"Cannot delete {path} - {self._not_found} does not exist")

    def move_dir(self, path: str, receiving_path: str) -> None:
        """
        Moves a directory to another directory.
        :param path: The path of the directory to move.
        :param receiving_path: The path of the directory receiving the directory being moved.
        """
        # Acquire directory containing the directory that needs to be moved.
        split_path = path.split("/")
        split_path_to_receiving_dir = receiving_path.split("/")
        dir_being_moved_name = split_path[-1]
        dir_containing_dir_being_moved = self._get_dir_from_path(split_path[0:-1]) if len(split_path) > 1 else self._root

        # Ensure all directories exist, then pop the directory from its current location and add it to the new one.
        if dir_containing_dir_being_moved is not None:
            receiving_dir = self._get_dir_from_path(split_path_to_receiving_dir)
            if receiving_dir is not None:
                dir_being_moved = dir_containing_dir_being_moved.pop(dir_being_moved_name)
                if dir_being_moved is not None:
                    receiving_dir.add(dir_being_moved)
                else:
                    print(f"Cannot move {path} to {receiving_path} - {dir_being_moved_name} does not exist")
            else:
                print(f"Cannot move {path} to {receiving_path} - {self._not_found} does not exist")
        else:
            print(f"Cannot move {path} to {receiving_path} - {self._not_found} does not exist")

    def start(self) -> None:
        """
        Starts the application.
        """
        print("""
        Welcome to file system application!
        
        COMMANDS:
            
            EXIT: Exits the application.
            
            LIST: List the contents of the file system.
            
            CREATE: Create a directory.
                -- args --
                argument 1: The path of the directory to create.
                
            DELETE: Deletes a directory.
                -- args --
                argument 1: The path of the directory to delete.
                
            MOVE: Move a directory.
                -- args --
                argument 1: The path of the directory to move.
                argument 2: The path of the directory to receive the directory being moved.
        """)
        while True:
            # Receive input from user.
            input_str = input("@User: ")
            input_list = input_str.split(" ")
            command = input_list[0].upper()
            args = input_list[1:]

            # Exit if applicable.
            if command.upper() == "EXIT":
                print("Exiting program...")
                break

            # Run appropriate function for command given.
            match command:
                case "LIST":
                    self._root.list_contents()
                case "CREATE":
                    if len(args) < 1 or len(args[0]) < 1:
                        print("Please provide a path create the new directory at.")
                        continue
                    self.create_dir(args[0])
                case "DELETE":
                    if len(args) < 1 or len(args[0]) < 1:
                        print("Please provide a path to the directory to delete.")
                        continue
                    self.delete_dir(args[0])
                case "MOVE":
                    if len(args) < 1 or len(args[0]) < 1:
                        print("Please provide argument containing path to directory to move.")
                        continue
                    elif len(args) < 2 or len(args[1]) < 1:
                        print("Please provide argument containing path to directory to receive the directory being moved.")
                        continue
                    self.move_dir(args[0], args[1])
                case _:
                    print("Invalid command.")
