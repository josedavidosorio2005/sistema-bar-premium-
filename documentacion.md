Sistema de Gestión Vieja Guardia Bar
Documentación técnica
1. Descripción general
El Sistema de Gestión Vieja Guardia Bar es una aplicación de escritorio desarrollada en Python que utiliza Tkinter para la interfaz gráfica. Está diseñado para gestionar las operaciones diarias de un bar, incluyendo el manejo de mesas, pedidos, facturación y análisis de ventas.
2. Requisitos del Sistema

Python 3.x
Bibliotecas requeridas:

Intercambio de palabras
laboratorio de informes
PyPDF2
fecha y hora
lugar
json
sistema operativo
biblioteca de rutas
mecanografía



3. Estructura del sistema
3.1 Clases principales
Factura Electronica
Gestiona la configuración y generación de facturas electrónicas.

Atributos de configuración:

nombre_empresa
nit_empresa
direccion_empresa
teléfono_empresa
régimen
resolucion_dian
prefijo_factura
consecutivo_actual



Aplicación BarPremium
Clase principal que maneja la interfaz y lógica del sistema.
3.2 Funcionalidades Principales
Gestión de mesas

Capacidad para manejar hasta 25 mesas.
Estados de mesa: libre/ocupada
Seguimiento de tiempo de ocupación
Control de pedidos por mesa

Gestión de productos

Organización por categorías:

Licores por litro
Licores por media
Tragos
Cervezas
Micheladas
Bebidas no alcohólicas
Cócteles
Otros productos


Funcionalidades:

Agregar productos
Modificar productos existentes
Eliminar productos
Gestión de precios



Sistema de Facturación

Generación de recibos simples
Generación de facturas electrónicas con:

Datos del cliente
Información fiscal
Desglose de productos
Calculo automatico de totales



Análisis de ventas

Informes diarios que incluyen:

Total de ventas
Productos más vendidos
Registro de facturas y recibos
Análisis por mesa
Exportación a PDF



4. Interfaz de usuario
4.1 Diseño visual

Tema oscuro profesional
Colores personalizados:

Fondo: #1a1a2e
Acento: #e94560
Texto: #ffffff
Botones: #0f3460
Paneles: #212142



4.2 Componentes principales

Panel de mesa
Catálogo de productos
Panel de cuenta actual
Botones de acción:

Pagar
Eliminar último pedido
Generar factura
Modificar productos
Ver ventas del día



5. Almacenamiento de datos
5.1 Archivos del Sistema

productos.json: Catálogo de productos y precios
Carpeta recibos/: Almacena recibos generados
Carpeta facturas/: Almacena facturas electrónicas
Carpeta reportes/: Almacena informes de ventas

5.2 Estructura de datos
pitónCopiarmesas = {
    numero_mesa: {
        "estado": "libre/ocupada",
        "pedidos": [(producto, precio)],
        "total": float,
        "hora_inicio": datetime
    }
}

categorias = {
    categoria: {
        producto: precio
    }
}
6. Generación de documentos
6.1 Recibos

Formato PDF
Incluye:

Información del establecimiento
Número de mesa
Detalle de pedidos
Total
Fecha y hora



6.2 Facturas Electrónicas

Formato PDF
Incluye:

Datos fiscales del establecimiento
Información del cliente
Resolución DIAN
Desglose de productos
Totales
Información legal requerida



7. Análisis y reportes
7.1 Informes de ventas

Análisis diario
Métricas incluidas:

Ventas totales
Cantidad de recibos y facturas
Productos más vendidos
Análisis por mesa
Desglose horario



7.2 Exportación de datos

Formato PDF
Incluye gráficos y tablas
Organización cronológica
Totales y subtotales

8. Mantenimiento
8.1 Respaldo de datos
Se recomienda:

Copia de seguridad diaria de archivos JSON
Respaldo semanal de carpetas de recibos y facturas
Exportación mensual de informes de ventas.

8.2 Actualizaciones
Para actualizar el sistema:

Respaldar datos actuales
Actualizar código fuente
Verificar integridad de datos
Probar funcionalidades principales

9. Recomendaciones de uso

Realizar cierre de caja diario
Verificar estado de mesas al inicio de turno
Mantener actualizado el catálogo de productos.
Generar y revisar informes de ventas diariamente.
Realizar respaldo de periódicos de la información

10. Soporte y mantenimiento
Para soporte técnico o reportar problemas:

Documentar el error encontrado
Capturar pantalla si es posible
Anotar pasos para reproducir el problema
Contactar al equipo de soporte técnico
