class Produtor:
    def __init__(self, id_produtor, nome, tipo, local, email, usuario):
        self.id_produtor = id_produtor
        self.nome = nome
        self.tipo = tipo
        self.local = local
        self.email = email
        self.usuario = usuario
        self.consultorias = []
        self.participacoes = []
    
    def agendar_consultoria(self, consultoria):
        self.consultorias.append(consultoria)
    
    def participar_capacitacao(self, particpacao):
        self.participacoes.append(participacao)
        
