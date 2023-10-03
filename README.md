# Tercera Entrega
## Definiciones del Sistema
Vamos a hacer un sistema que nos permita vender ropa usada, para ello tendremos las tablas de productos, donde cargaremos la ropa que vamos a vender, la tabla de clientes donde registareremos quienes nos compran esa ropa y la tabla de ordenes que nos dice que cliente compró que producto.

Al no ser una línea de producción ni tener en la generalidad productos repetidos se decide que cada prenda que ingresa es un producto por lo que no le definiremos cantidad ya que un producto siempre será único.

## Descripción de las URLs

### app/inicio
Esta es la url de inicio del sistema,  muestra el template base.html que es de donde heredamos el header, la navbar y el footer para mantener siempre la misma estética en nuestra página y luego va a buscar todos los productos cargados en la tabla de productos para mostrarlos cada uno en una Card por medio del template resultados.html

### app/cliente
Esta dirección nos permite ingresar un cliente en nuestra base pidiendonos el nombre y su email.

### app/producto
Esta dirección nos permite ingresar un producto nuevo nuestra base pidiendonos el nombre, que tipo de producto es (Hombre o Mujer) y su precio actualizando con el nuevo producto la pàgina de inicio.

### app/buscar
Nos permite buscar un producto que contenga en el nombre lo que ponemos para buscar.






