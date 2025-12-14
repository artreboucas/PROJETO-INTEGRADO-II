class Arquivo:
    def __init__(self, id_arquivo, nome, tipo, link, capacitacao=None, consultoria=None):
        self.id_arquivo = id_arquivo
        self.nome = nome
        self.tipo = tipo
        self.link = link
        self.capacitacao = capacitacao
        self.consultoria = consultoria
