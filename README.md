# Data Platform
 
Atualização do gerenciador de pacotes:
sudo apt update -y && \
sudo apt upgrade -y && \
sudo apt-get update -y && \
sudo apt-get upgrade -y
 
Instalar Docker:
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin && \
sudo usermod -a -G docker <nome do usuário (na dúvida, veja com o comando "whoami")>
 
No diretório raíz, executar o comando:
git clone <repo> && \
mv <nomedorepo>/airflow airflow && \
mv <nomedorepo>/hop hop && \
mv <nomedorepo>/postgresql postgresql
rm -drf <nomedorepo>
 
 
Atenção com o id de usuário! Se seu ID de usuário não for 1000 (para verificar use o comando "echo $UID"), altere os seguintes arquivos, trocando o 1000 (antes dos ":") pelo seu ID de usuário: airflow/.env, hop/Dockerfile, hop/docker-compose.yml.
 
Criar pastas de apoio e arquivo .env:
cd airflow && echo -e "AIRFLOW_UID=1000\nAIRFLOW_GID=0" > .env && mkdir ./logs ./plugins && cd .. && cd hop && mkdir ./projects && mkdir ./projects/dw && cd ..
 
Subir os containers:
cd postgresql && docker compose up -d && cd .. && cd hop && docker compose build && docker compose up -d && cd .. && cd airflow && docker compose up -d && cd ..

Parar e remover os containers:
cd <airflow/hop/postgresql> && docker compose down
