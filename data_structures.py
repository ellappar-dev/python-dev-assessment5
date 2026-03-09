def filter_and_sort_evens(numbers):
    """Return a sorted list of even numbers from the input list."""
    return sorted([n for n in numbers if n % 2 == 0])


def count_character_frequency(text):
    """Return a dictionary with character frequencies in the given text."""
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq


# Test cases
print(filter_and_sort_evens([3, 1, 4, 7, 1, 5, 9, 2, 6, 8]))
print(count_character_frequency("This my task for Basic Data Structures & Algorithms"))
