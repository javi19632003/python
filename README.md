# Tercera Entrega

## Definiciones del Sistema
Vamos a hacer un sistema que nos permita vender ropa usada, para ello tendremos las tablas de productos, donde cargaremos la ropa que vamos a vender, la tabla de clientes donde registareremos quienes nos compran esa ropa y la tabla de ordenes que nos dice que cliente compró que producto.

Al no ser una línea de producción ni tener en la generalidad productos repetidos se decide que cada prenda que ingresa es un producto por lo que no le definiremos cantidad ya que un producto siempre será único.

el usuario de admin es anico y la clave 123
Un usuario normal es alejandro  y la clave Pepe123!


## Descripción de las URLs

### /inicio
Esta es la url de inicio del sistema,  muestra el template base.html que es de donde heredamos el header, la navbar y el footer para mantener siempre la misma estética en nuestra página y luego va a buscar todos los productos cargados en la tabla de productos para mostrarlos cada uno en una Card por medio del template resultados.html

### /about
Esta dirección nos permite ver una página estática que habla un poco sobre mi.

### /producto
Esta dirección nos permite ingresar un producto nuevo nuestra base pidiendonos el nombre, a que categoría de productos pertenece, su precio y una foto para el catalogo actualizando con el nuevo producto la pàgina de inicio.

### /buscar
Nos permite buscar un producto que contenga en el nombre lo que ponemos para buscar y nos muestra la selección.

### /registro
Nos permite agregar un usuario nuevo al sitio y en un futuro que pueda comprar.

### /edit
Nos permite modificar los datos de un usuario.

### /login
Sirve para que un usuario ingrese al sito, lo que en un futuro le va a permitir hacer una compra.

### /logout
Sirve para que un usuario termine su sesión en el sitio.

### /class-detalle-producto/<pk>
Nos permite ver el detalle de un producto

### /class-up-producto/<pk>
Nos permite modificar los datos de un producto

### /class-del-producto/<pk>
Nos permite borrar un producto cargado 

