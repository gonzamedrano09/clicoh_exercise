# Ejecicio para ClicOH

## Ejecución del proyecto en un entorno local

1. Teniendo instalado Python 3.10 y virtualenv, crear el entorno virtual con `python3 -m virtualenv venv`.
2. Activar el entorno virtual, en Linux lo hacemos con `source venv/bin/activate`.
3. Instalar los paquetes necesarios en el entorno virtual con `pip install -r requirements.txt`.
4. Generar un archivo con las variables de entorno .env a partir del archivo .env.example `cp .env.example .env`.
5. Setear en el archivo .env la variable SECRET_KEY.
6. Ejecutar las migraciones necesarias con `python manage.py migrate`.
7. Correr el servidor para pruebas de django con `python manage.py runserver`.
8. Acceder a la interfaz web a través de [http://localhost:8000/][url]

## Supuestos del dominio

Ante la falta de algunos detalles más finos respecto al domino del ejercicio, se hacen suposiciones sobre algunos 
detalles en el comportamiento de los modelos para ser consistente con la solución presentada.

### Modelo usuario

- Para implementar la autenticación, es necesesario tener usuarios, implementé un modelo basico donde solo se tienen 
los campos de username, password, first_name (opcional) y last_name (opcional).
- Cualquier usuario registrado tiene permisos para interactuar con las apis de productos y ordenes.
- Generé una acción para los usuarios que permite cambiar la contraseña cuando estas logueado, al cambiar la 
contraseña el JWT activo en ese momento debería ser deshecho y el usuario debería generar uno nuevo por seguridad, este 
comportamiento no está desarrollado y se puede seguir usando el token actual solo para simplificar la solución, pero 
quería notificar que si lo tuve en cuenta.

### Modelo producto

- Agregar un producto permite establecer un nombre, precio y stock inicial para el mismo.
- Editar un producto permite una modificación de nombre o precio, pero no de stock.
- Eliminar un producto permite una eliminación lógica, ya que el mismo puede haber pertenecido a ordenes generadas 
anteriormente y no debería eliminarse físicamente.

### Modelo orden

- Agregar una orden obliga a establecer al menos un detalle de orden.
- Modificar una order reestablece el stock de los productos de los detalles de orden que van a ser reemplazados antes de 
generarse los nuevos detalles de orden.
