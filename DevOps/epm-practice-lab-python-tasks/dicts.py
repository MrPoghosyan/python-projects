"""
 Drop empty items from a dictionary.
"""
import json


def main():
    """Drop empty items from a dictionary."""
    d = json.loads(input())
    # Filter out items with value None
    filtered = {k: v for k, v in d.items() if v is not None}
    print(filtered)


if __name__ == "__main__":
    main()
