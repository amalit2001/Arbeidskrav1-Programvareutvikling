"""This class manages a collection of support tickets(cases)
It stores and manages all the support tickets"""
from models.support_case import SupportCase

class SupportSystem:

    # Initializes an empty list that all tickets will be stored in
    def __init__(self):
        self.cases = []

    # Creates and adds a new support case to the system
    def create_case(self, description, case_id, priority):
        case = SupportCase(case_id, description, priority)
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
    def find_case(self, case_id):
        for case in self.cases:
            if case.id == case_id:
                return case
        return None
    
    def delete_case(self, case_id):
        case = self.find_case(case_id)
        if case:
               self.cases.remove(case)
               return True
        return False