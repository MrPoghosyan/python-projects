# FileManager

FileManager is a Python-based utility for performing basic file operations such as searching, renaming, deleting, and creating backups of files. This project uses the `pathlib` module for cross-platform path handling and ensures compatibility with various operating systems.

## Features

- **Search Files**: Search for files with a specific extension in the given directory.
- **Rename Files**: Rename any file within the directory.
- **Delete Files**: Delete a file from the system.
- **Backup Files**: Create a backup of any file in a specified directory.

## Requirements

- Python 3.x
- `pathlib` and `shutil` are built-in Python modules, so no additional dependencies are required.

## How to Use

### 1. Create Test Files

Before running the script, you need to create some test files in the current directory to test the various features.
On Linux or macOS, you can use the following commands in the terminal to create files for testing:
```bash
touch old_file.txt important_file.txt file_to_delete.txt

### 2. Running the Script

Run the Python script by using the following command in the terminal:
python3 file_manager.py

### 3. Expected Output

The script will perform the following actions:

    Search Files: It will search for all .txt files in the current directory and its subdirectories, then print the results.

    Rename File: It will attempt to rename old_file.txt to new_file.txt. If the file exists, you will see a success message, otherwise an error message.

    Delete File: The script will delete file_to_delete.txt. If the file is found, it will be deleted, otherwise, you will get an error message.

    Backup File: The script will create a backup of important_file.txt in a directory called backup/. If the file exists, it will be copied to the backup directory.

### 4. Verify the Results

After running the script:

    Search: Check the terminal for a list of .txt files found.
    Rename: The file old_file.txt should now be renamed to new_file.txt.
    Delete: The file file_to_delete.txt should be removed from the directory.
    Backup: A backup of important_file.txt should appear in the backup/ directory.


Conclusion

This project demonstrates basic file management skills, showcasing how to interact with files and directories using Python. It uses the pathlib module for safe path handling across different platforms.
