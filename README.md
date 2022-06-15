# Ejecicio para ClicOH

## Ejecución del proyecto

1. Completar
2. Completar
3. Completar

## Supuestos del dominio

Ante la falta de algunos detalles más finos respecto al domino del ejercicio, se hacen suposiciones sobre algunos 
detalles en el comportamiento de los modelos para ser consistente con la solución presentada

### Modelo usuario

- Para implementar la autenticación, es necesesario tener usuarios, implementé un modelo basico donde solo se tienen 
los campos de username, password, first_name (opcional) y last_name (opcional)
- Generé una acción para los usuarios que permite cambiar la contraseña cuando estas logueado, al cambiar la 
contraseña el JWT activo en ese momento debería ser deshecho y el usuario debería generar uno nuevo por seguridad, este 
comportamiento no está desarrollado y se puede seguir usando el token actual solo para simplificar la solución, pero 
quería notificar que si lo tuve en cuenta 

### Modelo producto

- Agregar un producto permite establecer un nombre, precio y stock inicial para el mismo
- Editar un producto permite una modificación de nombre o precio, pero no de stock
- Eliminar un producto permite una eliminación lógica, ya que el mismo puede haber pertenecido a ordenes generadas 
anteriormente y no debería eliminarse físicamente

### Modelo orden

- Agregar una orden obliga a establecer al menos un detalle de orden
- Modificar una order reestablece el stock de los productos de los detalles de orden que van a ser reemplazados antes de 
generarse los nuevos detalles de orden