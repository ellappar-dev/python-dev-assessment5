def safe_divide(a, b):
    """Divide a by b with error handling."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both inputs must be numbers."
    except Exception as e:
        return f"Unexpected error: {e}"


# Test cases
print(safe_divide(10, 2))     # Expected: 5.0
print(safe_divide(10, 0))     # Expected: Error message
print(safe_divide(10, "a"))   # Expected: Error message
