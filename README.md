# API WEDEV - PLATAFORMA DE CURSOS
Desafio Wedev.software

## Tecnologias
    - FastAPI
    - SqlAlchemy
    - PostgreSQL
    - Black/PEP8 (lint)
    - Tailwind
    - Pytest

## Módulos (CRUD)
    - Usuários (based role) -> professor, aluno e staff
    - Cursos

### Configurações do projeto:
Para configurar o container refaça os seguintes passos antes de prosseguir (garanta que o [docker](https://docs.docker.com/engine/install/) esteja instalado e configurado corretamente em sua máquina)

### Iniciando
```bash
    docker-compose up
```

Após isso container será executado em sua máquina
- Para acessar abra o seu navegador e digite a seguinte url: `http://localhost:8000`

O container será executado com `FastAPI` e `PostgreSQL`

Caso não deseje o modo verboso feche o terminal e abra com o seguinte comando:

```bash
    # para ligar
    docker-compose start
    # para desligar
    docker-compose stop
```

### Documentação
    `Swagger OpenAPI`
    - http://localhost:8000/docs


### Rodando testes
Abra o terminal e digite o seguinte comando:

```bash
    pytest
```