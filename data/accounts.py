ADMIN = {"email": "admin@practicesoftwaretesting.com", "password": "welcome01"}

INVALID_LOGINS = [
    {"email": "invalid01@practicesoftwaretesting.com", "password": "welcome01", "expected_code": 401},
    {"email": "admin@practicesoftwaretesting.com", "password": "", "expected_code": 401}
]           
