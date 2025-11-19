"""
Find common items in 2 lists without duplicates. Sort the result list before output.
"""


def main():
    """Find common numbers."""
    li1 = list(map(int, input().split()))
    li2 = list(map(int, input().split()))

    # Convert lists to sets to remove duplicates and find intersection
    common = set(li1) & set(li2) # & operator = intersection
    result = sorted(common) # Sort the result list
    print(result)


if __name__ == "__main__":
    main()
