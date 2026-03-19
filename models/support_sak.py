class SupportSak:
    def __init__(self, id, beskrivelse):
        self.id = id
        self.beskrivelse = beskrivelse
        self.status = "Åpen"

    def oppdater_status(self, ny_status):
        self.status = ny_status

    def avslutt_sak(self):
        self.status = "Lukket"

    def __str__(self):
        return f"ID: {self.id}, Beskrivelse: {self.beskrivelse}, Status: {self.status}"