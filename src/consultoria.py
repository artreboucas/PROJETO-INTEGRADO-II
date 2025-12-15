class Consultoria:
    def __init__(self, id_consultoria, tema, horario, produtor, rede):
        self.id_consultoria = id_consultoria
        self.tema = tema
        self.horario = horario
        self.produtor = produtor
        self.rede = rede

    def confirmar(self):
        return f"Consultoria sobre {self.tema} confirmada para {self.horario}"
