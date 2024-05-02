#!/bin/bash

# Inicia el servicio A en segundo plano
cd /app/servicioA
flask run --host=0.0.0.0 --port=5000 &

# Inicia el servicio B en segundo plano
cd /app/servicioB
flask run --host=0.0.0.0 --port=5001 &

# Espera indefinidamente para mantener el contenedor en ejecución
while true; do sleep 1; done
