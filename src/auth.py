import bcrypt
import json
import os

def generate_password_hash(password):
    """
    Generate a secure hash of the given password using bcrypt.

    Args:
        password (str): The password to be hashed.

    Returns:
        str: The hashed password.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode()

def create_user_profile(username):
    """
    Create a new user profile with the given username and save it to a file.

    Args:
        username (str): The username for the new user profile.
    """
    profile = {"username": username, "theme": "light"}
    profiles_dir = "profiles"
    os.makedirs(profiles_dir, exist_ok=True)
    profile_path = os.path.join(profiles_dir, f"{username}.json")
    with open(profile_path, "w") as f:
        json.dump(profile, f)

def load_user_profile(username):
    """
    Load a user profile from a file.

    Args:
        username (str): The username of the user profile to load.

    Returns:
        dict: The loaded user profile, or None if the profile does not exist.
    """
    profiles_dir = "profiles"
    profile_path = os.path.join(profiles_dir, f"{username}.json")
    if os.path.exists(profile_path):
        try:
            with open(profile_path, "r") as f:
                profile = json.load(f)
            return profile
        except (IOError, ValueError) as e:
            print(f"Error loading profile for {username}: {e}")
    return None