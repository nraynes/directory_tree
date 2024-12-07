# Python File System Simulation  

This project is a Python-based file system simulation. It enables users to interact with a virtual file system by creating, moving, and deleting directories through a command-line interface.  

## Features  
- **List Contents**: View the hierarchical structure of the file system.  
- **Create Directory**: Add new directories to the file system at specified paths.  
- **Delete Directory**: Remove directories by specifying their paths.  
- **Move Directory**: Relocate a directory to a new parent directory within the system.  

## How to Run  

1. **Prerequisites**: Ensure you have Python 3.x installed.  
2. **Navigate to the Project Directory**:  
   Open a terminal and use the `cd` command to navigate to the folder containing the project files.  

   ```bash
   cd /path/to/project
   ```  
3. **Run the Application**:  
   Execute the following command to start the application:  
   ```bash
   python3 app.py
   ```  

## Usage Instructions  

Once the application starts, you will see a welcome message and a list of available commands.  
### Available Commands:  
- `EXIT`: Exit the application.  
- `LIST`: Display the contents of the file system in a hierarchical format.  
- `CREATE <path>`: Create a directory at the specified path.  
- `DELETE <path>`: Remove the directory located at the specified path.  
- `MOVE <path> <new_path>`: Move a directory from the current path to a new path.


### Example Interactions  

1. Create a directory:  
   ```bash
   CREATE Documents
   CREATE Documents/Work
   CREATE Documents/Personal
   ```

2. List file system contents:  
   ```bash
   LIST
   ```  
   Output:  
   ```
   Documents
     Personal
     Work
   ```  

3. Move a directory:  
   ```bash
   MOVE Documents/Work Documents/Personal
   LIST
   ```  
   Output:  
   ```
   Documents
     Personal
       Work
   ```  

4. Delete a directory:  
   ```bash
   DELETE Documents/Personal/Work
   LIST
   ```  
   Output:  
   ```
   Documents
     Personal
   ```  

5. Exit the application:  
   ```bash
   EXIT
   ```  
   Output:  
   ```
   Exiting program...
   ```  

---  

## Project Structure  
- `app.py`: Entry point for the application.  
- `file_system.py`: Contains the core logic for managing the file system and its commands.  
- `directory.py`: Implements the `Directory` class for handling individual directories and their contents.  
