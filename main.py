from usuario import Usuario
from produtor import Produtor
from rede_apoio import RedeDeApoio
from consultoria import Consultoria
from capacitacao import Capacitacao
from arquivo import Arquivo
from participacao import Participacao


def main():
    # Classe usuario
    usuario1 = Usuario(1, "Administrador", "admin@email.com", "123456", "gestor")

    # Classe produtor
    produtor1 = Produtor(
        1,
        "João da Silva",
        "Agricultor Familiar",
        "Região do Cariri",
        "joao@email.com",
        usuario1
    )

    # Classe rede de apoio
    rede1 = RedeDeApoio(
        1,
        "UFCA",
        "Educação",
        "Agroecologia",
        "Juazeiro do Norte - CE",
        usuario1
    )

    # Classe consultoria
    consultoria1 = Consultoria(
        1,
        "Manejo Sustentável do Solo",
        "09:00",
        produtor1,
        rede1
    )

    # Classe capacitação
    capacitacao1 = Capacitacao(
        1,
        "Curso Básico de Agroecologia",
        "Capacitação voltada para práticas agrícolas sustentáveis",
        "2025-03-15",
        rede1
    )

    # Classe arquivo
    arquivo1 = Arquivo(
        1,
        "apostila_agroecologia.pdf",
        "PDF",
        "https://link-exemplo.com/apostila",
        capacitacao=capacitacao1
    )

    capacitacao1.arquivos.append(arquivo1)

    # Classe participação
    participacao1 = Participacao(
        1,
        produtor1,
        capacitacao1,
        presenca=True,
        status="Confirmado"
    )

    produtor1.participacoes.append(participacao1)
    capacitacao1.participacoes.append(participacao1)

    print("Sistema de Gestão de Feiras Agroecológicas Locais")
    print(f"Produtor: {produtor1.nome}")
    print(f"Capacitação: {capacitacao1.titulo}")
    print(f"Status da Participação: {participacao1.status}")


if __name__ == "__main__":
    main()
