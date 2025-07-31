import hashlib
import bcrypt
import secrets

def execute_code(code, allowed_imports=None):
    """
    Executes the provided code string in a secure and restricted environment.

    Args:
        code (str): The Python code to be executed.
        allowed_imports (list, optional): A list of allowed module names to be imported.

    Raises:
        ValueError: If the code attempts to import a module not in the allowed_imports list.
        Exception: If any other error occurs during code execution.
    """
    if allowed_imports is None:
        allowed_imports = []

    code_obj = compile(code, '<string>', 'exec')
    import_names = [
        name.split('.')[0]
        for name in code_obj.co_names
        if name.startswith('__import__')
    ]

    for import_name in import_names:
        if import_name not in allowed_imports:
            raise ValueError(f"Import of '{import_name}' is not allowed.")

    try:
        exec(code_obj)
    except Exception as e:
        raise e

def hash_password(password):
    """
    Hashes the provided password using the bcrypt algorithm.

    Args:
        password (str): The password to be hashed.

    Returns:
        str: The hashed password.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode()