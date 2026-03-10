import requests

def fetch_and_display_users(num_users):
    """Fetch users from JSONPlaceholder API and display name, email, and city."""
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response.raise_for_status()  # Raises error for non-200 status codes
        users = response.json()

        for user in users[:num_users]:
            try:
                name = user.get("name", "N/A")
                email = user.get("email", "N/A")
                city = user.get("address", {}).get("city", "N/A")
                print(f"Name: {name}, Email: {email}, City: {city}")
            except KeyError:
                print("Error: Unexpected JSON structure for user data.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None
    except ValueError:
        print("Error: Failed to parse JSON response.")
        return None


# Example calls
print("Fetching 3 users:")
fetch_and_display_users(3)

print("\nFetching 5 users:")
fetch_and_display_users(5)
