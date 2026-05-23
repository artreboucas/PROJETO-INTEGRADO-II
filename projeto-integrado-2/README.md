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

**Abstração,** ao representar conceitos do mundo real, como produtores, capacitações e redes de apoio, por meio de classes;

**Encapsulamento,** ao agrupar atributos e comportamentos relacionados dentro de cada classe;

**Herança,** considerada na modelagem do sistema como possibilidade de especialização de usuários e papéis no sistema, estando prevista para ser aplicada nas próximas etapas de evolução do MVP;

**Baixo acoplamento,** permitindo que as classes se relacionem sem dependências excessivas;

**Polimorfismo,** também previsto para versões futuras do sistema,permitindo que comportamentos semelhantes foram implementados de forma que possam ser reutilizados de maneira flexível, permitindo futuras extensões do sistema sem grandes alterações no código existente.

Além disso, foram adotadas boas práticas como, separação de responsabilidades entre classes, métodos curtos e objetivos, nomenclatura clara e coerente. Essas práticas contribuem diretamente para a qualidade do MVP e facilitam a evolução do projeto nas próximas etapas.

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

## Sprint 2 – Projeto Físico de Banco de Dados (EP2)

No Sprint 2, foi desenvolvido o Projeto Físico de Banco de Dados do MVP do Sistema de Gestão de Feiras Agroecológicas Locais, a partir do Diagrama Entidade-Relacionamento (DER) definido no Projeto Integrador I.

Nesta etapa, as entidades do modelo conceitual foram transformadas em tabelas, com definição de tipos de dados, chaves primárias, chaves estrangeiras e restrições de integridade, garantindo coerência entre a modelagem e a implementação do sistema.

As principais tabelas projetadas foram: usuario, produtor, rede_de_apoio, capacitacao, consultoria, participacao e arquivo, refletindo diretamente as classes implementadas no Sprint 1.

## 📚 O que é Projeto Físico de Banco de Dados?

(Componente Extensionista)

O projeto físico de banco de dados é a fase em que o modelo conceitual é convertido em tabelas reais, prontas para serem criadas em um banco de dados.

Para quem está aprendendo a programar, essa etapa é importante porque ajuda a entender como os dados são armazenados, garante a integridade das informações e facilita a integração entre o banco de dados e a aplicação.

## Sprint 3 – Prototipação do Wireframe e do Sitemap do MVP (EP3)

No Sprint 3, foi desenvolvido a prototipação do wireframe e a estrutura do sitemap do MVP, com o objetivo de organizar as principais telas do sistema e definir o fluxo de navegação entre elas.

O wireframe foi utilizado para representar de forma simplificada a estrutura das interfaces do sistema, permitindo visualizar a organização dos elementos das telas, como menus, botões, campos de formulário e áreas de conteúdo. Essa etapa é importante para planejar como o usuário irá interagir com o sistema antes da implementação.

Além disso, foi definido o sitemap do MVP, que representa a estrutura de navegação entre as páginas da aplicação. Ele mostra como as telas estão conectadas e quais caminhos o usuário pode seguir dentro do sistema.

## Prototipação de Wireframes

(Componente Extensionista)

A prototipação de wireframes é uma etapa importante no desenvolvimento de sistemas, pois permite visualizar de forma simples como as telas da aplicação serão organizadas antes da implementação. O wireframe funciona como um esboço da interface, mostrando a disposição de elementos como menus, botões, campos de formulário e áreas de conteúdo. Durante esse processo, o foco principal não está no design visual ou nas cores, mas sim na estrutura das telas e no fluxo de navegação do usuário dentro do sistema. Isso permite identificar se as funcionalidades estão organizadas de forma clara e se o usuário consegue realizar suas tarefas de maneira simples e intuitiva.

Além disso, a criação de wireframes facilita a comunicação entre os membros da equipe, permitindo discutir ideias e realizar ajustes ainda na fase de planejamento, antes do desenvolvimento do sistema.

## Design Centrado no Usuário e Impacto no Dia a Dia

O design centrado no usuário busca desenvolver sistemas considerando as necessidades e a experiência das pessoas que irão utilizá-los. Isso envolve criar interfaces claras, organizadas e fáceis de usar.

Quando esses princípios são aplicados, os sistemas se tornam mais intuitivos e acessíveis, facilitando o uso da tecnologia no dia a dia. Dessa forma, as pessoas conseguem realizar tarefas com mais rapidez, menos erros e maior eficiência ao utilizar aplicações digitais.

## 👥 Equipe

Projeto desenvolvido pelos discentes do curso de Análise e Desenvolvimento de Sistemas (ADS) da UFCA, como parte das atividades do Projeto Integrado II.

- Arthur Rebouças do Carmo  
- Sheila Matias Barroso  
- Rubens Lopes dos Santos 
- Carlos Rodrigo Ferreira da Silva 
- Viviana Barros Gomes de Sousa 
- Samuelson da Silva Lima 
- Vitoria Cavalcante Souza
