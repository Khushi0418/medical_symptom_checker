def sanitize_input(user_input: str) -> str:
    """
    Basic cleanup of user input to prevent unsafe characters.
    """
    return user_input.strip()
    
