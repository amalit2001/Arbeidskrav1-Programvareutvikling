from models.support_system import SupportSystem

def meny():
    system = SupportSystem()
    teller = 1

    while True:
        print("\n--- IT SUPPORT SYSTEM ---")
        print("1. Registrer sak")
        print("2. Vis saker")
        print("3. Oppdater status")
        print("4. Avslutt sak")
        print("5. Avslutt program")

        valg = input("Velg et alternativ: ")

        if valg == "1":
            beskrivelse = input("Beskriv problemet: ")
            system.legg_til_sak(beskrivelse, teller)
            print("Sak registrert!")
            teller += 1

        elif valg == "2":
            system.vis_saker()

        elif valg == "3":
            try:
                id = int(input("Oppgi ID: "))
                sak = system.finn_sak(id)
                if sak:
                    ny_status = input("Ny status: ")
                    sak.oppdater_status(ny_status)
                    print("Status oppdatert!")
                else:
                    print("Fant ikke sak.")
            except:
                print("Ugyldig input.")

        elif valg == "4":
            try:
                id = int(input("Oppgi ID: "))
                sak = system.finn_sak(id)
                if sak:
                    sak.avslutt_sak()
                    print("Sak avsluttet!")
                else:
                    print("Fant ikke sak.")
            except:
                print("Ugyldig input.")

        elif valg == "5":
            print("Program avsluttes...")
            break

        else:
            print("Ugyldig valg")


if __name__ == "__main__":
    meny()