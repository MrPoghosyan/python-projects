import re
from setuptools import setup, find_packages

# Get version from snapshot/_init__.py
with open("snapshot/__init__.py", "r") as f:
    content = f.read()
    version_match = re.search(r'^__version__ = ["\']([^"\']+)["\']', content, re.MULTILINE)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Cannot find version in __init__.py")

setup(
    name="snapshot",
    version=version,
    packages=find_packages(),
    install_requires=[
        "psutil>=5.9.0"
    ],
    entry_points={
        "console_scripts": [
            "snapshot=snapshot.snapshot:main"
        ]
    },
    description="Simple system snapshot tool",
    long_description=open("./snapshot/README.md").read(),
    long_description_content_type="text/markdown",
    author="Vahag Poghosyan",
    url="https://gitlab.com/MrPoghosyan",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
