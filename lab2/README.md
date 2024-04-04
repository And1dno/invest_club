# File Manager

This Python-based file manager allows users to create, delete, and move folders.

## Features

1. Create folders: Users can create new folders within the current directory.
2. Delete folders: Users can delete existing folders.
3. Move folders: Users can move folders to a different location within the file system.

## Installation

To use the file manager, follow these steps:

1. Clone the repository:
   
Bash

   git clone https://github.com/yourusername/file_manager.git
   

2. Navigate to the project directory:
   
Bash

   cd file_manager
   

3. Run the file manager:
   
Bash

   python file_manager.py
   

## Usage

Upon running the file manager, users can interact with the following commands:

- create_folder: Create a new folder in the current directory.
- delete_folder: Delete a specified folder.
- move_folder: Move a folder to a different location.

Example usage:
Python

# Create a new folder
create_folder("NewFolder")

# Delete an existing folder
delete_folder("OldFolder")

# Move a folder to a different location
move_folder("FolderToMove", "DestinationPath")

## Dependencies

This project requires Python 3.x to be installed on your machine.

## Contributions

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
