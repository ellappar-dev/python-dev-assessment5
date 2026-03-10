# Task 3.1: Fetch and Process API Data
import requests

def fetch_and_display_users(num_users):
    """Fetches user data from JSONPlaceholder API and prints name, email, and city."""
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise exception for non-200 status
        users = response.json()

        for i, user in enumerate(users[:num_users]):
            try:
                name = user["name"]
                email = user["email"]
                city = user["address"]["city"]
                print(f"{i+1}. {name} | {email} | {city}")
            except KeyError as ke:
                print(f"Missing expected key in user data: {ke}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"Network or request error: {e}")
        return None
    except ValueError:
        print("Error parsing JSON response")
        return None

# Example usage
if __name__ == "__main__":
    fetch_and_display_users(5)