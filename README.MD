### Template FastAPI

### Pre requisitos

- Docker - https://docs.docker.com/install/
- Docker-compose - https://docs.docker.com/compose/install/

Tambem e necessario criar o arquivo `.env` com os valores atribuidos conforme arquivo `.env.example`

### Pre requisitos - Somente WINDOWS
Neste template foi aplicado o conceito de CONTAINER-FIRST,
logo para iniciar o desenvolvimento e necessario configurar a seguinte variavel de ambiente no seu sistema operacional: 

`COMPOSE_CONVERT_WINDOWS_PATHS=1`


## Executar - Desenvolvimento
Abra o terminal, entre na pasta root do projeto e execute o seguinte comando:

`docker-compose up`

## Acessar
Para acessar apenas abra o navegar e acesse: http://localhost:5000/docs