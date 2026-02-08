CREATE table if not exists usuario (
    id_usuario INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(100) NOT NULL,
    tipo_usuario VARCHAR(30) NOT NULL
);

CREATE TABLE if not exists produtor (
    id_produtor INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    local VARCHAR(100),
    email VARCHAR(100) NOT NULL,
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);
CREATE INDEX idx_produtor_usuario ON produtor(id_usuario);

CREATE TABLE if not exists rede_de_apoio (
    id_rede INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    area VARCHAR(100),
    foco VARCHAR(100),
    localizacao VARCHAR(100),
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

CREATE INDEX idx_rede_usuario ON rede_de_apoio(id_usuario);

CREATE table if not exists capacitacao (
    id_capacitacao INT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    descricao TEXT,
    data DATE NOT NULL,
    id_rede INT NOT NULL,
    FOREIGN KEY (id_rede) REFERENCES rede_de_apoio (id_rede)
);

CREATE INDEX idx_capacitacao_rede ON capacitacao(id_rede);

CREATE table if not exists consultoria (
    id_consultoria INT PRIMARY KEY,
    tema VARCHAR(100) NOT NULL,
    horario VARCHAR(20) NOT NULL,
    id_produtor INT NOT NULL,
    id_rede INT NOT NULL,
    FOREIGN KEY (id_produtor) REFERENCES produtor(id_produtor),
    FOREIGN KEY (id_rede) REFERENCES rede_de_apoio(id_rede)
);

CREATE INDEX idx_consultoria_produtor ON consultoria(id_produtor);
CREATE INDEX idx_consultoria_rede ON consultoria(id_rede);

CREATE TABLE participacao (
    id_participacao INT PRIMARY KEY,
    id_produtor INT NOT NULL,
    id_capacitacao INT NOT NULL,
    presenca BOOLEAN NOT NULL,
    status VARCHAR(30) NOT NULL,
    FOREIGN KEY (id_produtor) REFERENCES produtor(id_produtor),
    FOREIGN KEY (id_capacitacao) REFERENCES capacitacao(id_capacitacao)
);

CREATE INDEX idx_participacao_produtor ON participacao(id_produtor);
CREATE INDEX idx_participacao_capacitacao ON participacao(id_capacitacao);

CREATE table if not exists  arquivo (
    id_arquivo INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo VARCHAR(30) NOT NULL,
    link VARCHAR(255) NOT NULL,
    id_capacitacao INT,
    id_consultoria INT,
    FOREIGN KEY (id_capacitacao) REFERENCES capacitacao(id_capacitacao),
    FOREIGN KEY (id_consultoria) REFERENCES consultoria(id_consultoria),
    CHECK (
        id_capacitacao IS NOT NULL OR id_consultoria IS NOT NULL
    )
);
