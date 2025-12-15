class RedeDeApoio:
    def __init__(self, id_rede, nome, area, foco, localizacao, usuario):
        self.id_rede = id_rede
        self.nome = nome
        self.area = area
        self.foco = foco
        self.localizacao = localizacao
        self.usuario = usuario
        self.capacitacoes = []

    def adicionar_capacitacao(self, capacitacao):
        self.capacitacoes.append(capacitacao)
        
