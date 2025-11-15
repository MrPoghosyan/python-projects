"""
    Reverse characters in each world of a sentence while preserving word order.
"""

def main():
    """Reverse each word in the input string."""
    # Read the entire input line
    s = input()
    # Split the sentence into words by spaces
    words = s.split(" ")
    # Reverse each word individually
    reversed_words = [word[::-1] for word in words]
    # Join the reversed words back into a sentence
    result = " ".join(reversed_words)
    # Print the final result
    print(result)

if __name__ == "__main__":
    main()
