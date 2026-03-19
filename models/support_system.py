from models.support_case import SupportCase


class SupportSystem:
    def __init__(self):
        self.cases = []

    def add_to_case(self, description, id, priority):
        case = SupportCase(id, description, priority)
        self.cases.append(case)

    def show_cases(self):
        if not self.cases:
            print("No cases registered.")
        else:
            for case in self.cases:
                print(case)

    def find_case(self, id):
        for case in self.cases:
            if case.id == id:
                return case
        return None