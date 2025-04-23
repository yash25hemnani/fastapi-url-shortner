import uuid

def generate_short_code(length=8):
    return uuid.uuid4().hex[:length]
