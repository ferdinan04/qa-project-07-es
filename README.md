# Proyecto 7 - Pruebas para comprobar la funcionalidad de la web de Urban.Routes

## Acerca del proyecto

Este proyecto tiene como objetivo realizar pruebas para validar el comportamiento que tienen ejecutar ciertas acciones por un usuario en la aplicación Urban.Routes

## Tecnologías utilizadas

- Python
- Pytest
- Request
- Selenium

## Instalación y uso de librerías

Para la ejecución de pruebas se requiere tener instalados los siguientes paquetes:

- pytest
- request
- selenium

Su instalación puede hacerse con pip, de la siguiente manera:

1. Abrir la terminal o consola en PyCharm
2. Ingresar el comando py -m pip install requests
3. Ingresar el comando py -m pip install pytest

De igual modo, para la ejecución de pruebas con pytest:

1. En el menú "Run" de PyCharm, selecciona "Edit Configurations" (Editar configuraciones).
2. Haz clic en "+ (Add New Configuration)" (Agregar nueva configuración). Se abrirá una ventana nueva.
3. Selecciona "Python tests → pytest" (Pruebas de Python → Pytest) en la lista de configuraciones.
4. Aparecerá una ventana nueva. Selecciona "Custom" (Personalizar) en la línea "Target" (Objetivo).
5. Haz clic en "Apply" (Aplicar) y luego en "OK" (Aceptar).
6. Ahora haz clic en el ícono de la flecha verde para iniciar la configuración y observa los resultados.

Para el uso de Selenium se requiere instalar su controlador de navegador:

1. Se puede encontrar el archivo comprimido en el siguiente enlace: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/
2. Descarga el que coincida con tu sistema operativo.
3. Descomprime el archivo. Crea una carpeta llamada WebDriver/bin y guarda el archivo allí.
4. Agrega la ruta a bin a la variable de entorno PATH. El algoritmo depende del sistema operativo.

Para Windows
1. Abre el Panel de Control.
2. Ve a Sistema → Configuración avanzada del sistema → Variables de entorno.
3. Busca y edita la variable PATH agregando la ruta completa hacia la carpeta bin que acabas de crear. Debería ser algo como C:\WebDriver\bin.

Para MacOS y Linux

1. Abre la terminal.
2. Ejecuta el siguiente comando para agregar la carpeta bin al PATH del sistema:
export PATH=/Users/<username>/Downloads/WebDriver/bin:$PATH

Ejecución de otros navegadores y versiones:
1. Si planeas descargar WebDriver para otros navegadores y sus versiones, guarda todos los archivos en la misma carpeta: WebDriver/bin. De esta manera, no tendrás que editar PATH de nuevo.

## Detalles de las pruebas
Las pruebas se centran en el archivo main.py.
Se utiliza el Modelo de Objetos de Página (POM) para la estructura del código, en este se crean las siguientes clases:
### Clase UrbanRoutesPage 
Contiene los Locators o Localizadores
Contiene los métodos de clase
### Clase TestUrbanRoutes
Contiene métodos de clase de inicio y cierre de controlador (setup_class y teardown_class)
Contiene los métodos de las pruebas que se desean evaluar, las cuales se presentan a continuación:
1. Configurar la dirección.
2. Seleccionar la tarifa Comfort.
3. Rellenar el número de teléfono.
4. Agregar una tarjeta de crédito.
5. Escribir un mensaje para el controlador.
6. Pedir una manta y pañuelos.
7. Pedir 2 helados.
8. Aparece el modal para buscar un taxi.

## Información Adicional
Para obtener más detalles sobre este proyecto, consulta al equipo de pruebas del proyecto, se comparte detalles de contactos debajo.

## Desarrollador
- Nombre: Ferdinan Rebaza
- Cohort: 07
- Sprint: 07