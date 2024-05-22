# Data Platform

## Atualização do Gerenciador de Pacotes

Atualize o gerenciador de pacotes com os seguintes comandos:

```
sudo apt update -y && \
sudo apt upgrade -y && \
sudo apt-get update -y && \
sudo apt-get upgrade -y
```

## Instalação do Docker

Instale o Docker e adicione o seu usuário ao grupo de permissões com o seguinte comando:

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin && \
sudo usermod -a -G docker <nome do usuário (na dúvida, veja com o comando "whoami")>
```

## Configuração Inicial

No diretório raiz, clone o repositório e mova os diretórios para suas respectivas localizações:

```
git clone https://github.com/ViniSpeck/DataPlatform.git && \
mv DataPlatform/airflow airflow && \
mv DataPlatform/hop hop && \
mv DataPlatform/postgresql postgresql && \
rm -drf DataPlatform
```

## Atenção ao ID de Usuário

Verifique o ID do seu usuário com o comando echo $UID. Se o seu ID de usuário não for 1000, altere os seguintes arquivos, substituindo o valor 1000 (antes dos ":") pelo seu ID de usuário:

 - hop/Dockerfile
 - hop/docker-compose.yml

## Configuração Adicional

Crie pastas de apoio e o arquivo .env:

```
cd airflow && \
echo -e "AIRFLOW_UID=0\nAIRFLOW_GID=0" > .env && \
mkdir ./logs ./plugins && \
cd ../hop && \
mkdir ./projects && \
mkdir ./projects/dw
```

## Subir os Containers
Inicie os containers PostgreSQL, HOP e Airflow com os seguintes comandos:

```
cd ../postgresql && \
docker compose up -d && \
cd ../hop && \
docker compose build && \
docker compose up -d && \
cd ../airflow && \
docker compose up -d && \
cd ..
```

## Parar e Remover os Containers
Para parar e remover os containers, vá para o diretório desejado (airflow, hop ou postgresql) e execute:

```
docker compose down
```
