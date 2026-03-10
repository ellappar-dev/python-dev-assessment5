def calculate_average(numbers):
    try:
        if len(numbers) == 0:
            print("Error: Cannot calculate average of an empty list.")
            return None
        total = 0
        for i in range(len(numbers)):
            total += numbers[i]
        return total / len(numbers)
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def get_list_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print("Error: Index out of bounds.")
        return None
    except TypeError:
        print("Error: Provided object is not a list.")
        return None


# Example calls
data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []  # Empty list

print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")

print(get_list_element([1, 2, 3], 1))     # Valid
print(get_list_element([1, 2, 3], 5))     # Out of bounds
print(get_list_element("not a list", 0))  # Wrong type
