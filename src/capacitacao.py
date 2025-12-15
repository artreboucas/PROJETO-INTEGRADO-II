class Capacitacao:
    def __init__(self, id_capacitacao, titulo, descricao, data, rede):
        self.id_capacitacao = id_capacitacao
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.rede = rede
        self.arquivos = []
        self.participacoes = []

    def adicionar_arquivo(self, arquivo):
        self.arquivos.append(arquivo)

    def adicionar_participacao(self, participacao):
        self.participacoes.append(participacao)
        
