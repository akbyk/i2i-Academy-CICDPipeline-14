import re

def is_valid_email(email: str) -> bool:
    """
    Returns True if the given string is a valid email address format,
    False otherwise.
    """
    if not isinstance(email, str):
        return False

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None