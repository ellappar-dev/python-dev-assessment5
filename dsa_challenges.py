# Task 2.1: Basic Data Structures & Algorithms

def filter_and_sort_evens(numbers):
    """
    Takes a list of integers and returns a sorted list of even numbers.
    """
    evens = [num for num in numbers if num % 2 == 0]
    return sorted(evens)


def count_character_frequency(text):
    """
    Takes a string and returns a dictionary of character frequencies (case-insensitive).
    """
    text = text.lower()
    freq = {}
    for char in text:
        if char.isalpha():  # count only letters
            freq[char] = freq.get(char, 0) + 1
    return freq


# Example calls / test cases
if __name__ == "__main__":
    # Test filter_and_sort_evens
    numbers = [3, 1, 4, 7, 1, 5, 9, 2, 6, 8]
    print("Even numbers sorted:", filter_and_sort_evens(numbers))
    
    # Test count_character_frequency
    text = "This my task for Basic Data Structures & Algorithms"
    print("Character frequencies:", count_character_frequency(text))