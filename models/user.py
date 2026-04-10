"""Represents a user of the system with a specific role"""

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"User: {self.name} ({self.role})"