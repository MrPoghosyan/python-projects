"""
Check whether the input string is palindrome.
"""

def is_palindrome(s: str) -> bool:
    # Return True if the string 's' is a palindrome.
    # Lowercase and strip optional spaces if needed
    s = s.strip().lower()
    return s == s[::-1] #Reverses string and compares

def main():
    """Check palindrome."""
    # Read string from input and print 'yes' or 'no' if it's palindrome.
    s = input()
    if is_palindrome(s):
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()
