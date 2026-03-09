def write_to_file(filename, content):
    """Write the given content to a file."""
    try:
        with open(filename, "w") as f:
            f.write(content)
        return f"Successfully wrote to {filename}"
    except Exception as e:
        return f"Error writing to file: {e}"


def read_from_file(filename):
    """Read and return the content of a file."""
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: {filename} not found."
    except Exception as e:
        return f"Error reading file: {e}"


# Test the functions
print(write_to_file("sample.txt", "Hello, this is Task 2.4!"))
print(read_from_file("sample.txt"))
print(read_from_file("missing.txt"))  # should trigger error handling
