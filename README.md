# Ejecicio para ClicOH

## Ejecución del proyecto

1. Completar
2. Completar
3. Completar

## Supuestos del dominio

Ante la falta de algunos detalles más finos respecto al domino del ejercicio, se hacen suposiciones sobre algunos 
detalles en el comportamiento de los modelos para ser consistente con la solución presentada

### Modelo producto

- Agregar un producto supone establecer un nombre, precio y stock inicial para el mismo
- Editar un producto supone una modificación de nombre o precio, pero no de stock
- Eliminar un producto supone una eliminación lógica, ya que el mismo puede haber pertenecido a ordenes generadas 
anteriormente y no debería eliminarse físicamente

### Modelo orden

- Modificar una order supone reestablecer el stock de los productos de los detalles de orden que van a ser reemplazados 