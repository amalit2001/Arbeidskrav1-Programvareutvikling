"""The main entry point of the program,
allowing the user to interact with the system.
The program uses a simple menu to navigate between different functions
Ensuring that the user can only update to valid statuses"""
from models.support_system import SupportSystem
from models.support_case import VALID_STATUSES
from models.user import User

# This function contains the main menu loop and user interaction
# To make the program easy to use in the terminal, I used a simple menu system
def menu():
    system = SupportSystem()
    case_id = 1
    # The user can choose to log in as either an employee or an IT admin
    print("Choose role:")
    print("1. Employee")
    print("2. IT Admin")

    # Asking the user to select a role based on the menu options
    while True:
        role_choice = input("Select role: ")
        if role_choice == "1":
            current_user = User("EmployeeUser", "Employee")
            break
        elif role_choice == "2":
            current_user = User("AdminUser", "IT Admin")
            break
        else:
            print("Invalid choice, try again.")

    # Loop keeps running until the user chooses to exit the program
    while True:
        print("\n--- IT SUPPORT SYSTEM ---")
        print(f"Logged in as: {current_user.name} ({current_user.role})")
        print("0. Log out")

        if current_user.is_employee():
            print("1. Register case")

        elif current_user.is_admin():
            print("2. Show cases")
            print("3. Update status")
            print("4. Close case")
            print("5. Delete case")
        
        # User can select an option from the menu
        choice = input("Choose alternative: ")

        # Loggin out of the program for all users:
        if choice == "0":
            print("Log out...")
            break

        # For employees:
        # Adds a description of the issue and set the priority level
        elif choice == "1" and current_user.is_employee():
            description = input("Describe the issue: ")
            priority = input("Priority (Low/Medium/High): ")
            system.create_case(description, case_id, priority)
            print("Case registered!")
            case_id += 1
        
        #For admins:
        # Shows all existing tickets in the system to the IT admin
        elif choice == "2" and current_user.is_admin():
            system.show_cases()

        # The user can update the status of a selected ticket
        # The user needs to enter a valid ID and a valid status to update 
        elif choice == "3" and current_user.is_admin():
            try:
                case_id_input = int(input("Write ID: "))
                case = system.find_case(case_id_input)

                if case:
                    while True:
                       new_status = input("New status (Open / In Progress / Closed): ")
                       if new_status in VALID_STATUSES:
                           case.update_status(new_status)
                           print("Status updated!")
                           break
                       else:
                           print("Invalid status, please try again")
                else:
                    print("Did not find case.")
            except ValueError:
                print("You do not have permission or invalid choice.")

        # Closes selected ticket by changing the status to "Closed"
        elif choice == "4" and current_user.is_admin():
            try:
                case_id_input = int(input("ID: "))
                case = system.find_case(case_id_input)
                if case:
                    case.close_ticket()
                    print("Case closed!")
                else:
                    print("Did not find case.")

            # Handles the case where the user enters an invalid ID (not a number)
            except ValueError:
                print("You do not have permission or invalid choice.")

        # Deletes a selected case
        elif choice == "5" and current_user.is_admin():
            try:
                case_id_input = int(input("ID: "))
                if system.delete_case(case_id_input):
                    print("Case deleted!")
                else:
                    print("Did not find case.")
            except ValueError:
                print("You do not have permission or invalid choice.")

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()