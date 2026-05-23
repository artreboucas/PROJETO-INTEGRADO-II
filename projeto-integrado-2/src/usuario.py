class Usuario:
    def __init__(self, id_usuario, nome, email, senha, tipo_usuario):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self._senha = senha
        self.tipo_usuario = tipo_usuario
    def login(self, email, senha):
        return self.email == email and self._senha == senha
