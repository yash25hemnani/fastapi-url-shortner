import uuid

def generate_short_code(length=8):
    """
    Generates a unique short code of the specified length.

    Args:
        length (int): Length of the short code (default is 8).

    Returns:
        str: Unique 8-lettered code
    """

    return uuid.uuid4().hex[:length]
