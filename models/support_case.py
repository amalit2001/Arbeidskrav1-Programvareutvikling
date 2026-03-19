class SupportCase:
    def __init__(self, id, description, priority="Normal"):
        self.id = id
        self.description = description
        self.status = "Open"
        self.priority = priority

    def update_status(self, new_status):
        self.status = new_status

    def close_ticket(self):
        self.status = "Closed"

    def __str__(self):
        return (
            f"ID: {self.id} | "
            f"Description: {self.description} | "
            f"Status: {self.status} | "
            f"Priority: {self.priority}"
        )