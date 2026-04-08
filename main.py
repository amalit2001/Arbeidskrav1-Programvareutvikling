"""The main entry point of the program,
allowing the user to interact with the system.
The program uses a simple menu to navigate between different functions"""
from models.support_system import SupportSystem

# This function contains the main menu loop and user interaction
# To make the program easy to use in the terminal, I used a simple menu system
def meny():
    system = SupportSystem()
    case_id = 1
    # Loop keeps running until the user chooses to exit the program
    while True:
        print("\n--- IT SUPPORT SYSTEM ---")
        print("1. Register case")
        print("2. Show cases")
        print("3. Update status")
        print("4. Close case")
        print("5. Close program")
        # User can select an option from the menu
        choice = input("Choose alternative: ")

        # User can add a description of the issue and set the priority level
        if choice == "1":
            description = input("Describe the issue: ")
            priority = input("Priority (Low/Medium/High): ")
            system.create_case(description, case_id, priority)
            print("Case registered!")
            case_id += 1

        # Shows all existing tickets in the system
        elif choice == "2":
            system.show_cases()

        # The user can update the status of a selected ticket
        elif choice == "3":
            try:
                case_id_input = int(input("Write ID: "))
                case = system.find_case(case_id_input)
                if case:
                    new_status = input("New status: ")
                    case.update_status(new_status)
                    print("Status updated!")
                else:
                    print("Did not find case.")
            except ValueError:
                print("Invalid input.")

        # Closes selected ticket by changing the status to "Closed"
        elif choice == "4":
            try:
                id = int(input("ID: "))
                case = system.find_case(id)
                if case:
                    case.close_ticket()
                    print("Case closed!")
                else:
                    print("Did not find case.")

            # Handles the case where the user enters an invalid ID (not a number)
            except ValueError:
                print("Invalid input.")

        # Exits the program
        elif choice == "5":
            print("Program closing...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    meny()