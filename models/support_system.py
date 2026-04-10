"""This class manages a collection of support tickets(cases)
It stores and manages all the support tickets"""
from models.support_case import SupportCase

class SupportSystem:

    def __init__(self):
        self.cases = []
        self.next_id = 1

    # Creates and adds a new support case to the system
    def create_case(self, description, priority):
        case = SupportCase(self.next_id, description, priority)
        self.cases.append(case)
        self.next_id += 1

    # Prints all existing tickets in the system
    # If no tickets exist, it will print a message saying "No cases registered."
    def show_cases(self):
        if not self.cases:
            print("No cases registered.")
        else:
            for case in self.cases:
                print(case)
    
    # Updates the status of a ticket by its ID
    def update_case_status(self, case_id, new_status):
        case = self.find_case(case_id)
        if case:
            case.update_status(new_status)
            return True
        return False

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
    
