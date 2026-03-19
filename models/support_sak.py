class SupportSak:
    def __init__(self, id, beskrivelse, prioritet="Normal"):
        self.id = id
        self.beskrivelse = beskrivelse
        self.status = "Åpen"
        self.prioritet = prioritet

    def oppdater_status(self, ny_status):
        self.status = ny_status

    def avslutt_sak(self):
        self.status = "Lukket"

    def __str__(self):
        return (
            f"ID: {self.id} | "
            f"Beskrivelse: {self.beskrivelse} | "
            f"Status: {self.status} | "
            f"Prioritet: {self.prioritet}"
        )