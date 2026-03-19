from models.support_system import SupportSystem


def meny():
    system = SupportSystem()
    numerator = 1

    while True:
        print("\n--- IT SUPPORT SYSTEM ---")
        print("1. Registrer case")
        print("2. Show cases")
        print("3. Update status")
        print("4. Close case")
        print("5. Close program")

        choice = input("Choose alternative: ")

        if choice == "1":
            description = input("Describe the issue: ")
            priority = input("Priority (Low/Normal/High): ")
            system.add_to_case(description, numerator, priority)
            print("Case registerred!")
            numerator += 1

        elif choice == "2":
            system.show_cases()

        elif choice == "3":
            try:
                id = int(input("Oppgi ID: "))
                case = system.find_case(id)
                if case:
                    new_status = input("New status: ")
                    case.update_status(new_status)
                    print("Status oppdatert!")
                else:
                    print("Did not find case.")
            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            try:
                id = int(input("ID: "))
                case = system.find_case(id)
                if case:
                    case.close_ticket()
                    print("Case closed!")
                else:
                    print("Did not find case.")
            except ValueError:
                print("Invalid input.")

        elif choice == "5":
            print("Program closing...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    meny()