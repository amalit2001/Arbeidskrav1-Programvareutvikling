from models.support_sak import SupportSak

class SupportSystem:
    def __init__(self):
        self.saker = []

    def legg_til_sak(self, beskrivelse, id):
        sak = SupportSak(id, beskrivelse)
        self.saker.append(sak)

    def vis_saker(self):
        if not self.saker:
            print("Ingen saker registrert.")
        else:
            for sak in self.saker:
                print(sak)

    def finn_sak(self, id):
        for sak in self.saker:
            if sak.id == id:
                return sak
        return None