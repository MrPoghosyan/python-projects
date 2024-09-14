import shutil
from pathlib import Path

class FileManager:
    def __init__(self, directory):
        self.directory = Path(directory)  # Using pathlib to handle paths

    def search_files(self, extension):
        """Search for files with the specified extension in the given directory."""
        result = []
        for file in self.directory.rglob(f'*{extension}'):  # Searching for files with the specified extension
            result.append(file)
        return result

    def rename_file(self, old_path, new_path):
        """Rename a file."""
        old_path = Path(old_path)
        new_path = Path(new_path)
        if old_path.exists():
            old_path.rename(new_path)  # Using rename() from pathlib
            print(f"File renamed: {old_path} -> {new_path}")
        else:
            print("File not found!")

    def delete_file(self, path):
        """Delete a file."""
        path = Path(path)
        if path.exists():
            path.unlink()  # unlink() from pathlib removes the file
            print(f"File deleted: {path}")
        else:
            print("File not found!")

    def backup_file(self, path, backup_dir):
        """Create a backup of a file."""
        path = Path(path)
        backup_dir = Path(backup_dir)
        if not backup_dir.exists():
            backup_dir.mkdir(parents=True, exist_ok=True)  # Create directory if it doesn't exist
        if path.exists():
            shutil.copy(path, backup_dir / path.name)  # Copying the file to the destination directory
            print(f"Backup created: {path} -> {backup_dir / path.name}")
        else:
            print("File not found!")

# Usage examples
if __name__ == "__main__":
    file_manager = FileManager('.')

    search_results = file_manager.search_files('.txt')
    print("Found files:", search_results)

    file_manager.rename_file('old_file.txt', 'new_file.txt')
    file_manager.delete_file('file_to_delete.txt')
    file_manager.backup_file('important_file.txt', 'backup')

