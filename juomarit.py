class Juomari():
    def __init__(self):
        self.name = ''
        self.juomat = 0
        self.vedet = 0
        self.juomat_putkeen = 0
        self.juomalista = []
    
    def lisaa_juoma(self, uusi_juoma):
        found = False
        for juoma in self.juomalista:
            if juoma.lower() == uusi_juoma.lower():
                found = True
                break
        if found == False:
            self.juomalista.append(uusi_juoma.lower())

    def poista_juoma(self, poistettava_juoma):
        for juoma in self.juomalista:
            if juoma.lower() == poistettava_juoma.lower():
                break
        self.juomalista.remove(poistettava_juoma.lower())  

