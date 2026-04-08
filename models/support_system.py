"""This class manages a collection of support tickets(cases)
It stores and manages all the support tickets"""
from models.support_case import SupportCase

class SupportSystem:

    # Initializes an empty list that all tickets will be stored in
    def __init__(self):
        self.cases = []

    # Creates and adds a new support case to the system
    def create_case(self, description, id, priority):
        case = SupportCase(id, description, priority)
        self.cases.append(case)

    # Prints all existing tickets in the system
    # If no tickets exist, it will print a message saying "No cases registered."
    def show_cases(self):
        if not self.cases:
            print("No cases registered.")
        else:
            for case in self.cases:
                print(case)

    # Searches for a ticket by its ID and returns it
    # If no given ID is found, it returns None
    def find_case(self, id):
        for case in self.cases:
            if case.id == id:
                return case
        return None