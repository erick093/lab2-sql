# Laboratorio 2 - SQL

## Indice

1. [Introducción](#introducción)
2. [Estructura del proyecto](#estructura-del-proyecto)
3. [Ejecucion](#ejecucion)

## Introducción

En este laboratorio pondremos a practica los conocimientos adquiridos en la clase de SQL. 
En la primera parte del laboratorio encontraran una serie de preguntas con sus respectivas respuestas.
En la segunda se les pedi crear una base de datos de acuerdo al modelo proporcionado. 
En la tercera parte del laboratorio se les pedira que realicen consultas SQL para obtener los resultados solicitados.


## Estrucutra del proyecto
Dentro de la carpeta `data` se encuentran los archivos `csv` que se utilizarán para la creación de las tablas en la base de datos. 
Los archivos son los siguientes:

* `payment.csv`: contiene los datos relacionados a los metodos de pago.
* `rate.csv`: contiene informacion sobre la tarifa establecida en el viaje.
* `taxi_zone_lookup.csv`: contiene informacion sobre las zonas de taxis.
* `vendor.csv`: contiene informacion sobre los proveedores de los datos de cada viaje.


## Ejecución
Para ejectuar el laboratorio se debe ejecutar el siguiente comando:

```bash
docker-compose up
```

O alternativamente se puede ejecutar el siguiente comando, para deatachar el proceso de la terminal:


```bash
docker-compose up -d
```

El archivo `docker-compose.yml` contiene la configuración para ejecutar el laboratorio en un contenedor de docker.




