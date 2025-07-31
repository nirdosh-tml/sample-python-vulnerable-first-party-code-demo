"""
User Service
"""
from typing import Optional

from src.db import create_db, add_user, get_user_by_id
from src.auth import create_user_profile, load_user_profile, hash_password
from src.config import API_KEY

def print_masked_api_key(api_key: str) -> None:
    """
    Prints the first 5 characters of the API key followed by '***'.

    Args:
        api_key (str): The API key to be masked.
    """
    masked_key = f"{api_key[:5]}***"
    print(f"Using API key: {masked_key}")

def create_and_add_users() -> None:
    """
    Creates the database and adds two users to it.
    """
    create_db()
    add_user("alice", 30)
    add_user("bob", 22)

def get_and_print_user(user_id: int) -> None:
    """
    Retrieves a user by ID and prints their information.

    Args:
        user_id (int): The ID of the user to retrieve.
    """
    user = get_user_by_id(user_id)
    print(f"User {user_id}: {user}")

def manage_user_profiles(username: str) -> None:
    """
    Creates and loads a user profile.

    Args:
        username (str): The username for the user profile.
    """
    create_user_profile(username)
    load_user_profile(username)

def main() -> None:
    """
    Main entry point for the User Service.
    """
    print("User Service Starting...")
    print_masked_api_key(API_KEY)

    create_and_add_users()

    get_and_print_user(1)

    manage_user_profiles("alice")

    password = "pass123"
    hashed_password = hash_password(password)
    print(f"Password hash: {hashed_password}")

if __name__ == "__main__":
    main()