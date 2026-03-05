import os
from importlib import resources
from pathlib import Path
from types import ModuleType
from typing import Union


def get_data_file_path(package: Union[str, ModuleType], 
                       relative_path: str) -> Path:
    """
    Return the path to a data file inside a Python package, including 
    subdirectories.

    Args:
        package: The package name (e.g., "mypackage") or a module object.
        relative_path: The path to the file within the package.

    Returns:
        A Path-like object (Traversable) pointing to the data file. It supports
        standard Path operations like `.read_text()` or `.open()`.

    Raises:
        FileNotFoundError: If the file does not exist inside the package.
    """
    resource = resources.files(package).joinpath(relative_path)

    if not resource.exists():
        raise FileNotFoundError(
            f"Data file '{relative_path}' not found in package '{package}'"
        )

    return resource



def print_directory_tree(start_path, indent="", 
                         ignore_git_folder=True,
                         ignore_pycache_folder=True):
    """
    Recursively prints the folder structure starting from start_path.
    """
    try:
        # List all items in the directory
        items = sorted(os.listdir(start_path))
    except PermissionError:
        print(f"{indent}[Permission Denied]")
        return
    except FileNotFoundError:
        print(f"{indent}[Path Not Found]")
        return

    for index, item in enumerate(items):
        path = os.path.join(start_path, item)
        is_last = index == len(items) - 1
        connector = "└── " if is_last else "├── "
        if ignore_git_folder and item == ".git":
            pass
        elif ignore_pycache_folder and item == "__pycache__":
            pass
        else:
            print(f"{indent}{connector}{item}")

            # If it's a directory, recurse into it
            if os.path.isdir(path) and not os.path.islink(path):
                new_indent = indent + ("    " if is_last else "│   ")
                print_directory_tree(path, new_indent)