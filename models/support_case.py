"""This class represents a single support ticket in the system.
It contains methods for updating and closing the ticket"""
class SupportCase:
    # Initializes a new support ticket
    # I included priority as it makes the system more realistic
    def __init__(self, case_id, description, priority="Normal"):
        self.id = case_id
        self.description = description
        self.status = "Open"
        self.priority = priority

    # Updates the status of the ticket (ex. Open, In Progress, Closed)
    def update_status(self, new_status):
        self.status = new_status

    # Closes the ticket by setting the status to "Closed"
    def close_ticket(self):
        self.status = "Closed"

    # Returns a string representation of the ticket, showing its details
    # This method is used when printing the ticket info in the system
    def __str__(self):
        return (
            f"ID: {self.id} | "
            f"Description: {self.description} | "
            f"Status: {self.status} | "
            f"Priority: {self.priority}"
        )