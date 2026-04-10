"""User model representing a user in the system"""

VALID_ROLES = ["Employee", "IT Admin"]

class User:
    def __init__(self, name, role):
        if role not in VALID_ROLES:
            raise ValueError(f"Role must be one of {VALID_ROLES}")
        self.name = name
        self.role = role

    def is_admin(self):
        return self.role == "IT Admin"

    def is_employee(self):
        return self.role == "Employee"

    def __str__(self):
        return f"User: {self.name} ({self.role})"