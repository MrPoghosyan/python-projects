import os
import sys
import zipfile
import tempfile
import shutil
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def find_root_dir(path):
    """Detect the top-level directory inside the extracted archive."""
    items = os.listdir(path)
    if len(items) == 1 and os.path.isdir(os.path.join(path, items[0])):
        return os.path.join(path, items[0])
    return path


def remove_invalid_dirs(root):
    """
    Find and remove directories that do not contain __init__.py.
    Returns a list of removed directories (relative paths).
    """
    removed = []

    # Walk the directory tree bottom-up (important!)
    for current_dir, dirs, files in os.walk(root, topdown=False):

        # Skip root directory (it may be without __init__.py)
        if current_dir == root:
            continue

        # Check if __init__.py exists in the directory
        if "__init__.py" not in files:
            rel_path = os.path.relpath(current_dir, root)
            removed.append(rel_path)

            logging.info(f"Removing directory: {rel_path}")
            shutil.rmtree(current_dir, ignore_errors=True)

    removed.sort()
    return removed


def create_cleaned_txt(root, removed_dirs):
    """Create cleaned.txt and write the list of removed directories."""
    cleaned_file = os.path.join(root, "cleaned.txt")

    with open(cleaned_file, "w") as f:
        for d in removed_dirs:
            f.write(d + "\n")

    logging.info(f"cleaned.txt created with {len(removed_dirs)} entries")


def create_new_zip(root, original_zip):
    """Create a new ZIP archive with the _new suffix."""
    new_zip = original_zip.replace(".zip", "_new.zip")

    with zipfile.ZipFile(new_zip, "w", zipfile.ZIP_DEFLATED) as z:
        for dirpath, dirnames, filenames in os.walk(root):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                arcname = os.path.relpath(full_path, root)
                z.write(full_path, arcname)

    logging.info(f"New archive created: {new_zip}")


def main():
    if len(sys.argv) != 2:
        print("Usage:")
        print("python clean_app.py <archive.zip>")
        sys.exit(1)

    zip_file = sys.argv[1]

    if not zip_file.endswith(".zip"):
        print("Error: input file must be a .zip archive")
        sys.exit(1)

    if not os.path.exists(zip_file):
        print("Error: file not found")
        sys.exit(1)

    logging.info(f"Processing archive: {zip_file}")

    # Create temporary directory
    temp_dir = tempfile.mkdtemp()
    logging.info(f"Temporary directory: {temp_dir}")

    # Extract the archive
    with zipfile.ZipFile(zip_file, "r") as z:
        z.extractall(temp_dir)
    logging.info("Archive extracted")

    # Detect root directory
    root_dir = find_root_dir(temp_dir)
    logging.info(f"Detected root directory: {root_dir}")

    # Remove non-package directories
    removed = remove_invalid_dirs(root_dir)

    # Create cleaned.txt
    create_cleaned_txt(root_dir, removed)

    # Create the new ZIP archive
    create_new_zip(root_dir, zip_file)

    # Clean up temporary directory
    shutil.rmtree(temp_dir, ignore_errors=True)

    logging.info("Completed successfully.")


if __name__ == "__main__":
    main()
