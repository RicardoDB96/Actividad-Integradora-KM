# Usa la imagen oficial de Python
FROM python:3.9

# Copia los archivos de los servicios al contenedor
COPY servicioA /app/servicioA
COPY servicioB /app/servicioB

# Instala las dependencias de ambos servicios
COPY servicioA/requirements.txt /app/servicioA/requirements.txt
COPY servicioB/requirements.txt /app/servicioB/requirements.txt

RUN pip install -r /app/servicioA/requirements.txt
RUN pip install -r /app/servicioB/requirements.txt

# Copia el script de inicio al contenedor
COPY start_services.sh /app/start_services.sh

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Expone los puertos en los que los servicios escuchan
EXPOSE 5000

# Define el comando para ejecutar el script de inicio cuando se inicie el contenedor
CMD ["bash", "start_services.sh"]
