# Sistema de Gestão de Feiras Agroecológicas Locais

## 📌 Contexto Acadêmico
Este projeto foi desenvolvido no âmbito do **Projeto Integrado II (ADS0013)** do curso de **Análise e Desenvolvimento de Sistemas (ADS)**, vinculado ao **Centro de Educação a Distância (CEAD)** da **Universidade Federal do Cariri (UFCA)**.

O presente repositório corresponde ao **Entregável Parcial 1 (EP1)**, cujo objetivo é a implementação das **classes principais do MVP**, aplicando os conceitos de **Programação Orientada a Objetos (POO)**, com base na documentação produzida no **Projeto Integrador I**.

---

## 🎯 Objetivo do EP1
O EP1 tem como objetivo transformar a modelagem conceitual previamente desenvolvida, especialmente o **Diagrama Entidade-Relacionamento (DER)**, em código orientado a objetos visando organização do código-fonte e alinhamento entre análise e implementação.

---

## 🧩 Modelagem 

As classes implementadas neste projeto foram diretamente derivadas das entidades definidas no **DER do Projeto Integrador I**, garantindo coerência entre a fase de análise e a implementação.

### 🔹 Classes Implementadas

- **Usuario**  
  Representa os usuários responsáveis pela gestão do sistema.

- **Produtor**  
  Representa agricultores familiares participantes das feiras agroecológicas.

- **RedeDeApoio**  
  Representa universidades, instituições de apoio ou empresas juniores que oferecem suporte técnico.

- **Consultoria**  
  Representa consultorias técnicas oferecidas aos produtores pelas redes de apoio.

- **Capacitacao**  
  Representa cursos, treinamentos e capacitações voltados à agricultura sustentável.

- **Arquivo**  
  Representa materiais de apoio vinculados a capacitações ou consultorias.

- **Participacao**  
  Representa a participação do produtor em capacitações, controlando presença e status, conforme definido no DER.

Os relacionamentos entre as entidades foram implementados por meio de **associações entre objetos**, substituindo chaves estrangeiras por referências diretas entre as instâncias.

---

## 🧠 Princípios e Práticas

O desenvolvimento do projeto seguiu os principais fundamentos da Programação Orientada a Objetos:

- **Abstração**, ao representar entidades do mundo real por meio de classes;
- **Encapsulamento**, organizando atributos e comportamentos;
- **Responsabilidade Única**, garantindo que cada classe possua uma função específica;
- **Baixo acoplamento**, permitindo maior independência entre as classes;

---

## ▶️ Execução do Projeto

Para executar o projeto e visualizar o funcionamento das classes:
```bash
python main.py
```
O arquivo main.py demonstra a criação dos objetos e os relacionamentos entre as classes implementadas.

## 🌱 Possíveis usos da nossa solução

(Componente Extensionista)

A solução desenvolvida pode ser aplicada no mundo real para apoiar agricultores familiares, facilitando o acesso a consultorias técnicas e capacitações oferecidas por universidades e redes de apoio. Além disso, pode auxiliar gestores públicos e instituições na organização de feiras agroecológicas, no acompanhamento da participação dos produtores e na disponibilização de materiais educativos, contribuindo para o fortalecimento da economia local e para a promoção da sustentabilidade social, econômica e ambiental.

## 👥 Equipe

Projeto desenvolvido pelos discentes do curso de Análise e Desenvolvimento de Sistemas (ADS) da UFCA, como parte das atividades do Projeto Integrado II.

- Arthur Rebouças do Carmo  
- Sheila Matias Barroso  
- Rubens Lopes dos Santos 
- Carlos Rodrigo Ferreira da Silva 
- Viviana Barros Gomes de Sousa 
- Samantha Daniel da Silva 
- Vitoria Cavalcante Souza
