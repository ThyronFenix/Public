# Ghibli RESTapi
La api esta intencionada a funcionar con una base de datos PostgreSQL y se utiliza el ORM Django para el modelaje de datos.
He omitido la plantilla HTML con el fin de concentrarme en el backend.
Los modelos de datos y el consumo de la API deberia funcionar ajustando los argumentos y parametros segun el rol y usuarios una vez creada la base de tados.

ejecutar el comando ' manage.py makemigrations' para crear los datos segun el modelado, y posteriormente ejecutar el comando 'manage.py migrate' para ejecutar la migracion y llenar la base de datos.
