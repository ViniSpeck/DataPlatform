FROM apache/hop-web:latest

USER root

#troque o 1000 pelo seu id de usuário
RUN chown -R 1000:0 /opt /home /usr/local/tomcat

# Altere o 300 pelo timeout em minutos desejado
RUN sed -i 's/<session-timeout>30<\/session-timeout>/<session-timeout>300<\/session-timeout>/' /usr/local/tomcat/conf/web.xml

# Configuração para alocar o máximo possível de memória no container
ENV HOP_OPTIONS="-XX:+AggressiveHeap"

#troque o 1000 pelo seu id de usuário
USER 1000
