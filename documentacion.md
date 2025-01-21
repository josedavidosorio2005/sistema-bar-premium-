





 
software vieja guardia documentación proyecto
 
Juan Jose Roman Bedoya  
1037856118
					+57 316 3456062
Jose David Osorio Gallego
1037856337
+57 3506072725











cotizaciones 

En Colombia, el valor de un software como el que tienes depende mucho del mercado objetivo, el nivel de personalización, y a quién se lo ofrezcas (un pequeño negocio local, una cadena de bares, o una empresa más grande). Basándonos en el contexto colombiano, aquí está una estimación ajustada:

1. Para un Pequeño Negocio Local
Este tipo de cliente usualmente busca soluciones económicas y rápidas de implementar. El precio podría estar en el rango de:

COP $1,000,000 - $3,000,000
Este rango cubre un software funcional como el tuyo, con soporte básico y sin grandes personalizaciones adicionales.
2. Para una Cadena de Bares o Restaurantes
Si el software se vende a una cadena con varios locales, se espera un nivel más alto de soporte y posiblemente integración con otros sistemas. El precio podría subir a:

COP $5,000,000 - $12,000,000
Esto incluiría adaptaciones específicas para el cliente, soporte técnico, y quizás opciones adicionales como generación de reportes avanzados o integración con sistemas de facturación electrónica.
3. Para un Mercado Escalable o Licenciado
Si planeas comercializarlo como un producto que pueda ser vendido a múltiples clientes, el precio por licencia o instalación individual podría ser más bajo pero con volumen de ventas, como:

COP $300,000 - $1,000,000 por instalación
Con esta estrategia, podrías ganar más a largo plazo, vendiendo el software a muchos negocios pequeños.
Factores que Pueden Justificar un Precio Mayor:
Soporte técnico continuo: Actualizaciones y asistencia.
Cumplimiento normativo: Como la facturación electrónica bajo la DIAN.
Integración con hardware: Impresoras de tickets, escáneres de código de barras, etc.
Optimización y diseño: Mejora de la interfaz y experiencia de usuario.












Documentación para el Proyecto de Sistema Premium de Bar
Introducción
Este proyecto es un sistema de gestión para un bar llamado "Vieja Guardia". Permite llevar el control de mesas, pedidos y generar facturas electrónicas y recibos en PDF. Está construido utilizando Python y la biblioteca Tkinter para la interfaz gráfica, junto con ReportLab para la generación de PDFs.

Requisitos
Python 3.x
Bibliotecas necesarias:
tkinter
reportlab
PyPDF2
json
os
datetime
re
reportlab
pathlib

Puedes instalar las bibliotecas necesarias usando pip:

Copiar
pip install reportlab PyPDF2

Estructura del Proyecto
El código se organiza en varias clases y métodos que gestionan la lógica de la aplicación.

Clases Principales
FacturaElectronica:

Contiene la configuración básica de la empresa.
Almacena datos como nombre, NIT, dirección, teléfono, etc.
BarPremiumApp:

Clase principal que maneja la interfaz gráfica y la lógica del sistema.
Configura la ventana principal, estilos y los diferentes paneles de la aplicación.
Métodos Clave
__init__: Inicializa la aplicación y configura la ventana principal.
configure_locale: Configura la localización para el idioma español.
initialize_data: Inicializa los datos de las mesas y productos.
crear_interfaz_premium: Crea la interfaz gráfica principal.
generar_factura_electronica: Genera una factura electrónica en formato PDF.
generar_recibo: Genera un recibo en formato PDF.
analizar_ventas_del_dia: Analiza las ventas del día y genera un resumen.
guardar_productos: Guarda los productos en un archivo JSON.
cargar_productos: Carga los productos desde un archivo JSON.
Funcionalidades
Gestión de Mesas: Permite seleccionar mesas, ver su estado y realizar pedidos.
Menú de Productos: Muestra un menú categorizado con precios.
Generación de Recibos y Facturas: Genera documentos en PDF para las ventas realizadas.
Análisis de Ventas: Proporciona un resumen de las ventas del día.
Ejecución del Proyecto
Para ejecutar el proyecto, asegúrate de tener Python instalado y las bibliotecas requeridas. Luego, ejecuta el archivo principal:


Ejecución del Proyecto
Para ejecutar el proyecto, asegúrate de tener Python instalado y las bibliotecas requeridas. Luego, ejecuta el archivo principal:
python nombre_del_archivo.py

Conclusión
Este sistema proporciona una solución integral para la gestión de un bar, facilitando la administración de mesas, pedidos y la generación de documentos necesarios para el negocio. Se puede expandir con más funcionalidades según las necesidades del negocio.

Notas Adicionales
Asegúrate de tener permisos para crear archivos y carpetas en el directorio donde se ejecuta el script.
Los PDFs generados se almacenan en carpetas específicas (recibos , factura
s y reportes).








EXPLICACIÓN DEL FUNCIONAMIENTO DEL SISTEMA 

Lo primero es seleccionar una de las 25 mesas que aparecen en color verde luego debes de seleccionar los productos a cargarle de cualquiera de las categorías 
para realizar el pago debes de elegir qué tipo de factura deseas sea una normal o una electrónica la diferencia entre estas dos son la complejidad de las mismas la factura normal solo mostrara los productos consumidos mientras que la factura electrónica solicitara ciertos datos que se deben de llenar con los datos del cliente y esta contara con ciertos datos de la empresa como el NIT el nombre del local la direccion del mismo y la fecha y hora en la que se genero la factura 


otras de las funciones del sistema es  la de modificar producto para usar esta función basta con seleccionar el botón y se desplegará una ventana con la cual se puede interactuar en la parte superior aparece un menú desplegable en donde se mostrarán las categorías que se tienen en el momento para modificarlo lo primero es seleccionar lo que se desea modificar posteriormente presionar el botón en la parte inferior llamado modificar seleccionado este a su vez desplegará otra ventana con las siguientes funciones modificar el nombre y el precio del producto puedes modificar el que desees o ambos luego debes de darle en guardar y cerrar esa ventana para regresar a hacer algún otro cambio una vez tengas todos los cambios echos debes de apagar la aplicación o cerrarla para así que una vez se abra de nuevo los cambios se vean reflejados.
otro apartado de esta función es el de agregar nuevo producto en el cual puedes como anteriormente mencione agregar nuevo producto con su respectivo nombre y  precio cabe recalcar que para que los cambios se vean reflejados debes de reiniciar la aplicación
 y para la última función de este botón es la de eliminar producto la cual solo es seleccionar el producto que deseas eliminar de cualquiera de la categorías y seleccionar el botón de eliminar y tambien debes de reiniciar la aplicación para que los cambios se vean reflejado  

en ventas actues lee los pdf que se generar en recibos solamente en recibos y   te da  cunto gangster   mutra  q  se compro y pago atraves de factura elctronic ay cules fueron todos lo s productos vendidos en el dia  y tinen un afuncion q  ase q  se guarde en pdf ese 
