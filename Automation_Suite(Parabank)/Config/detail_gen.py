import time
import random
import string


def get_dynamic_user_data():
    """Generates a unique dataset for personal details and credentials."""
    ts = str(int(time.time())) + str(random.randint(100, 999))
    random_str = "".join(random.choices(string.ascii_lowercase, k=4))

    return {
        "first_name": f"Leo_{random_str}",
        "last_name": f"Messi_{random_str}",
        "address": f"{random.randint(10, 99)} Jaya Rd",
        "city": "Colombo",
        "state": "Western",
        "zip_code": "00500",  
        "phone": f"071{ts[-7:]}",
        "ssn": f"458{ts[-6:]}",
        "username": f"user_{ts}",
        "password": "Password123!",
        "confirm_password": "Password123!"  
    }