import re  # Importa la biblioteca 're' para trabajar con expresiones regulares, útil para buscar y manipular texto.

import json  # Importa la biblioteca 'json' para manejar datos en formato JSON, permitiendo la lectura y escritura de archivos JSON.

import tkinter as tk  # Importa el módulo principal de Tkinter, que se utiliza para crear interfaces gráficas de usuario (GUI).

from tkinter import ttk, messagebox  # Importa 'ttk' para widgets mejorados y 'messagebox' para mostrar diálogos de mensajes al usuario.

from datetime import datetime  # Importa 'datetime' para manejar fechas y horas, permitiendo la manipulación y formateo de fechas.

import locale  # Importa 'locale' para establecer configuraciones regionales, como formato de números y fechas.

from tkinter import simpledialog  # Importa 'simpledialog' para mostrar cuadros de diálogo simples para la entrada de datos del usuario.

# Importa canvas de reportlab para crear PDFs
from reportlab.pdfgen import canvas  # Permite crear documentos PDF utilizando el objeto 'canvas'.

# Importa el tamaño de página A4
from reportlab.lib.pagesizes import A4  # Define el tamaño de página A4 para los documentos PDF.

import os  # Importa 'os' para interactuar con el sistema de archivos, permitiendo operaciones como crear, eliminar o renombrar archivos y directorios.

from pathlib import Path  # Importa 'Path' de 'pathlib' para manejar rutas de archivos de manera más intuitiva.

from typing import Dict, List  # Importa tipos de datos para anotaciones, permitiendo especificar que ciertos objetos son diccionarios o listas.

# Importa clases y funciones para crear documentos PDF más complejos
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle  # Permite crear documentos PDF con un formato más estructurado.

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle  # Importa estilos predefinidos y permite crear estilos personalizados para el texto en PDF.

from reportlab.lib import colors  # Importa colores predefinidos para su uso en documentos PDF.

from reportlab.lib.pagesizes import letter  # Define el tamaño de página carta (letter) para los documentos PDF.

from datetime import datetime  # Importa nuevamente 'datetime' (redundante, ya que se importó anteriormente).

from PyPDF2 import PdfReader  # Importa 'PdfReader' de PyPDF2 para leer y manipular archivos PDF existentes.


class FacturaElectronica:
    # Clase para representar una factura electrónica.

    def __init__(self):
        # Constructor de la clase que inicializa la configuración de la factura.
        self.config = {
            'nombre_empresa': 'VIEJA GUARDIA BAR',  # Nombre de la empresa que emite la factura.
            'nit_empresa': '900.123.456-7',  # Número de Identificación Tributaria (NIT) de la empresa.
            'direccion_empresa': 'Calle Principal #123',  # Dirección de la empresa.
            'telefono_empresa': '(601) 123-4567',  # Número de teléfono de la empresa.
            'regimen': 'RÉGIMEN COMÚN',  # Régimen tributario de la empresa.
            'resolucion_dian': 'Resolución DIAN No. 12345678 del 2024/01/01',  # Resolución de la DIAN que autoriza la emisión de la factura.
            'prefijo_factura': 'VG',  # Prefijo que se usará en el número de la factura.
            'consecutivo_actual': 1  # Consecutivo actual de la factura, que se incrementará con cada nueva factura emitida.
        }
        
        return  # Fin del constructor, no es necesario retornar nada.


class BarPremiumApp:  # Define la clase principal de la aplicación
    def __init__(self, root):  # Método inicializador que recibe la ventana principal
        self.root = root  # Almacena la referencia a la ventana principal
        self.root.title("★ Vieja Guardia - Sistema Premium de Bar ★")  # Establece el título de la ventana
        self.root.geometry("1200x800")  # Define el tamaño inicial de la ventana
        self.root.minsize(1000, 700)  # Define el tamaño mínimo de la ventana

        # Colores personalizados para la interfaz
        self.colors = {
            'background': '#1a1a2e',  # Color de fondo
            'accent': '#e94560',  # Color de acento
            'text': '#ffffff',  # Color del texto
            'button': '#0f3460',  # Color de los botones
            'button_hover': '#16498c',  # Color de los botones al pasar el mouse
            'highlight': '#ff4d4d',  # Color de resaltado
            'success': '#2ecc71',  # Color de éxito
            'warning': '#f39c12',  # Color de advertencia
            'panel': '#212142'  # Color de los paneles
        }
        
        self.root.configure(bg=self.colors['background'])  # Configura el color de fondo de la ventana

        self.configure_locale()  # Llama al método para configurar la localización

        self.initialize_data()  # Llama al método para inicializar los datos
        self.facturacion = FacturaElectronica()

        self.configurar_estilos()  # Llama al método para configurar los estilos
        self.crear_interfaz_premium()  # Llama al método para crear la interfaz gráfica
    
    def configure_locale(self):  # Método para configurar la localización
        locales_to_try = ['es_CO.UTF-8', 'es_CO', 'es-CO', '']  # Lista de configuraciones regionales a intentar
        for loc in locales_to_try:  # Itera sobre las configuraciones
            try:
                locale.setlocale(locale.LC_ALL, loc)  # Intenta establecer la configuración regional
                break  # Si tiene éxito, sale del bucle
            except locale.Error:  # Si ocurre un error
                continue  # Continúa con la siguiente configuración
    
   
  

    def configurar_estilos(self):  # Método para configurar estilos de widgets
        style = ttk.Style()  # Crea un objeto Style
        style.theme_use('clam')  # Establece el tema de estilo

        # Configuración de estilos para botones
        style.configure(
            "Premium.TButton",
            padding=10,
            font=('Helvetica', 11, 'bold'),
            background=self.colors['button'],
            foreground=self.colors['text'],
            borderwidth=2,
            relief="raised"
        )

        style.map(
            "Premium.TButton",
            background=[('active', self.colors['button_hover'])],
            foreground=[('active', self.colors['text'])]
        )

        style.configure(
            "Mesa.TButton",
            padding=15,
            font=('Helvetica', 12, 'bold'),
            background=self.colors['accent']
        )

        style.configure(
            "Premium.TLabel",
            font=('Helvetica', 12),
            foreground=self.colors['text'],
            background=self.colors['background'],
            padding=5
        )

        style.configure(
            "Premium.TFrame",
            background=self.colors['background'],
            borderwidth=2,
            relief="raised"
        )

        style.configure(
            "Premium.TLabelframe",
            background=self.colors['panel'],
            foreground=self.colors['text'],
            borderwidth=2,
            relief="groove"
        )

        style.configure(
            "Premium.TLabelframe.Label",
            font=('Helvetica', 12, 'bold'),
            foreground=self.colors['text'],
            background=self.colors['panel'],
            padding=10
        )

        style.configure(
            "Premium.TNotebook",
            background=self.colors['panel'],
            borderwidth=0
        )

        style.configure(
            "Premium.TNotebook.Tab",
            font=('Helvetica', 11, 'bold'),
            padding=[15, 5],
            background=self.colors['button'],
            foreground=self.colors['text']
        )

        style.map(
            "Premium.TNotebook.Tab",
            background=[('selected', self.colors['accent'])],
            foreground=[('selected', self.colors['text'])]
        )

        style.configure(
            "Premium.Vertical.TScrollbar",
            background=self.colors['button'],
            bordercolor=self.colors['text'],
            arrowcolor=self.colors['text'],
            troughcolor=self.colors['background']
        )

        style.configure(
            "Premium.Horizontal.TScrollbar",
            background=self.colors['button'],
            bordercolor=self.colors['text'],
            arrowcolor=self.colors['text'],
            troughcolor=self.colors['background']
        )

    def crear_interfaz_premium(self):
        # Crea un marco principal con estilo 'Premium.TFrame'
        main_frame = ttk.Frame(self.root, style="Premium.TFrame")
        # Empaqueta el marco principal, ocupando todo el espacio disponible con márgenes
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Crea el encabezado de la interfaz en el marco principal
        self.crear_header(main_frame)
        # Crea un contenedor con desplazamiento en el marco principal
        self.crear_contenedor_scroll(main_frame)
        # Crea un panel para las mesas
        self.crear_panel_mesas()

        # Crea un marco inferior dentro de 'inner_frame' con estilo 'Premium.TFrame'
        bottom_frame = ttk.Frame(self.inner_frame, style="Premium.TFrame")
        # Empaqueta el marco inferior, ocupando todo el espacio disponible
        bottom_frame.pack(fill=tk.BOTH, expand=True, pady=(20, 0))

        # Configura la primera columna del marco inferior para que tenga un peso mayor
        bottom_frame.columnconfigure(0, weight=3)
        # Configura la segunda columna del marco inferior para que tenga un peso menor
        bottom_frame.columnconfigure(1, weight=2)

        # Crea un panel para productos dentro del marco inferior
        self.crear_panel_productos(bottom_frame)
        # Crea un panel para la cuenta dentro del marco inferior
        self.crear_panel_cuenta(bottom_frame)


    def crear_header(self, parent):
        # Crea un marco para el encabezado con estilo 'Premium.TFrame'
        header_frame = ttk.Frame(parent, style="Premium.TFrame")
        # Empaqueta el marco del encabezado, ocupando todo el ancho disponible con un margen inferior
        header_frame.pack(fill=tk.X, pady=(0, 20))

        # Crea una etiqueta para el título con formato específico
        title_label = tk.Label(
            header_frame,
            text="✯ VIEJA GUARDIA ✯",  # Texto del título
            font=('Helvetica', 36, 'bold'),  # Fuente y tamaño del texto
            fg=self.colors['accent'],  # Color del texto
            bg=self.colors['background']  # Color de fondo
        )
        # Empaqueta la etiqueta del título con márgenes superior e inferior
        title_label.pack(pady=(10, 5))

        # Crea una etiqueta para el subtítulo con formato específico
        subtitle_label = tk.Label(
            header_frame,
            text="Sistema Premium de Bar",  # Texto del subtítulo
            font=('Helvetica', 16),  # Fuente y tamaño del texto
            fg=self.colors['text'],  # Color del texto
            bg=self.colors['background']  # Color de fondo
        )
        # Empaqueta la etiqueta del subtítulo con un margen inferior
        subtitle_label.pack(pady=(0, 10))


    def crear_contenedor_scroll(self, parent):
        # Crea un marco para el contenedor de desplazamiento con estilo 'Premium.TFrame'
        scroll_frame = ttk.Frame(parent, style="Premium.TFrame")
        # Empaqueta el marco del contenedor de desplazamiento, ocupando todo el espacio disponible
        scroll_frame.pack(fill=tk.BOTH, expand=True)

        # Crea un lienzo (canvas) para contener los elementos desplazables
        self.canvas = tk.Canvas(
            scroll_frame,
            bg=self.colors['background'],  # Color de fondo del lienzo
            highlightthickness=0  # Sin grosor de resaltado
        )
        # Empaqueta el lienzo en el lado izquierdo, ocupando todo el espacio disponible
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Crea una barra de desplazamiento vertical
        self.scrollbar_y = ttk.Scrollbar(
            scroll_frame,
            orient="vertical",  # Orientación vertical
            command=self.canvas.yview,  # Comando para desplazar el lienzo verticalmente
            style="Premium.Vertical.TScrollbar"  # Estilo de la barra de desplazamiento
        )

        # Crea una barra de desplazamiento horizontal
        self.scrollbar_x = ttk.Scrollbar(
            scroll_frame,
            orient="horizontal",  # Orientación horizontal
            command=self.canvas.xview,  # Comando para desplazar el lienzo horizontalmente
            style="Premium.Horizontal.TScrollbar"  # Estilo de la barra de desplazamiento
        )

        # Configura el lienzo para que las barras de desplazamiento controlen su vista
        self.canvas.configure(
            yscrollcommand=self.scrollbar_y.set,  # Conecta la barra de desplazamiento vertical
            xscrollcommand=self.scrollbar_x.set   # Conecta la barra de desplazamiento horizontal
        )

        # Crea un marco interno dentro del lienzo para contener otros elementos
        self.inner_frame = ttk.Frame(self.canvas, style="Premium.TFrame")
        # Crea una ventana en el lienzo para el marco interno
        self.canvas_window = self.canvas.create_window(
            (0, 0),  # Posición inicial de la ventana dentro del lienzo
            window=self.inner_frame,  # Marco interno como ventana
            anchor="nw"  # Ancla en la esquina noroeste
        )

        # Vincula el evento de configuración del marco interno para ajustar el tamaño del lienzo
        self.inner_frame.bind("<Configure>", self.on_frame_configure)
        # Vincula el evento de configuración del lienzo para ajustar el tamaño del marco interno
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        # Vincula la rueda del ratón para el desplazamiento en el lienzo
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)


    def on_frame_configure(self, event=None):
        # Configura la región de desplazamiento del lienzo para que se ajuste al tamaño de todos los elementos
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    def on_canvas_configure(self, event):
        # Ajusta el ancho de la ventana interna en el lienzo cuando se redimensiona el lienzo
        self.canvas.itemconfig(self.canvas_window, width=event.width)

    def on_mousewheel(self, event):
        # Desplaza la vista del lienzo verticalmente basado en el movimiento de la rueda del ratón
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


    def crear_panel_mesas(self):
        # Crea un marco etiquetado para las mesas disponibles con estilo 'Premium.TLabelframe'
        mesas_frame = ttk.LabelFrame(
            self.inner_frame,
            text="🏮 Mesas Disponibles",  # Título del marco
            padding="20",  # Espaciado interno
            style="Premium.TLabelframe"  # Estilo del marco
        )
        # Empaqueta el marco, ocupando todo el ancho disponible con un margen inferior
        mesas_frame.pack(fill=tk.X, pady=(0, 20))

        # Configura las columnas del marco para que se expandan equitativamente
        for i in range(5):
            mesas_frame.columnconfigure(i, weight=1)

        # Crea botones para cada mesa disponible utilizando los números de mesa de self.mesas
        for i, mesa_num in enumerate(self.mesas.keys()):
            self.crear_boton_mesa(mesas_frame, mesa_num, i)


    def crear_boton_mesa(self, parent, mesa_num, index):
        # Obtiene el estado de la mesa (libre o ocupada)
        estado = self.mesas[mesa_num]["estado"]
        # Define el color de fondo basado en el estado de la mesa
        color_fondo = self.colors['success'] if estado == "libre" else self.colors['warning']
        
        # Crea un botón para la mesa con el estado correspondiente
        btn = tk.Button(
            parent,
            text=f"Mesa {mesa_num}\n{'🟢' if estado == 'libre' else '🟡'}",  # Muestra el número y el estado de la mesa
            font=('Helvetica', 11, 'bold'),  # Estilo de la fuente
            bg=color_fondo,  # Color de fondo del botón
            fg=self.colors['text'],  # Color del texto
            relief="raised",  # Estilo de relieve del botón
            bd=3,  # Ancho del borde del botón
            command=lambda m=mesa_num: self.seleccionar_mesa(m)  # Comando para seleccionar la mesa
        )
        
        # Coloca el botón en una cuadrícula dentro del marco padre
        btn.grid(
            row=index // 5,  # Calcula la fila en la que se colocará el botón
            column=index % 5,  # Calcula la columna en la que se colocará el botón
            padx=5,  # Espaciado horizontal
            pady=5,  # Espaciado vertical
            sticky="nsew"  # Hace que el botón se expanda para ocupar todo el espacio disponible
        )


    def crear_panel_productos(self, parent):
        # Crea un marco etiquetado para el menú de productos con estilo 'Premium.TLabelframe'
        productos_frame = ttk.LabelFrame(
            parent,
            text="🍾 Menú Vieja Guardia",  # Título del marco
            padding="20",  # Espaciado interno
            style="Premium.TLabelframe"  # Estilo del marco
        )
        # Coloca el marco en la cuadrícula del contenedor padre
        productos_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        # Crea un cuaderno (notebook) para gestionar las pestañas de categorías de productos
        notebook = ttk.Notebook(
            productos_frame,
            style="Premium.TNotebook"  # Estilo del cuaderno
        )
        # Empaqueta el cuaderno para que ocupe todo el espacio disponible
        notebook.pack(fill=tk.BOTH, expand=True)

        # Crea una pestaña para cada categoría de productos
        for categoria, productos in self.categorias.items():
            self.crear_tab_categoria(notebook, categoria, productos)


    def crear_tab_categoria(self, notebook, categoria, productos):
        # Crea una nueva pestaña en el cuaderno para la categoría de productos
        tab = ttk.Frame(notebook, style="Premium.TFrame", padding=10)
        notebook.add(tab, text=categoria)  # Añade la pestaña al cuaderno

        # Crea un lienzo para permitir el desplazamiento de los productos
        canvas = tk.Canvas(
            tab,
            bg=self.colors['panel'],  # Color de fondo del lienzo
            highlightthickness=0  # Sin borde resaltado
        )
        # Crea una barra de desplazamiento vertical
        scrollbar = ttk.Scrollbar(
            tab,
            orient="vertical",
            command=canvas.yview,  # Conecta la barra de desplazamiento al lienzo
            style="Premium.Vertical.TScrollbar"
        )

        # Crea un marco para contener los productos dentro del lienzo
        productos_frame = ttk.Frame(canvas, style="Premium.TFrame")

        # Configura el lienzo para que la barra de desplazamiento funcione correctamente
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Empaqueta el lienzo
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Empaqueta la barra de desplazamiento

        # Crea una ventana dentro del lienzo para el marco de productos
        canvas_frame = canvas.create_window(
            (0, 0),
            window=productos_frame,
            anchor="nw"  # Ancla la ventana en la esquina superior izquierda
        )

        # Crea un botón para cada producto en la categoría
        for producto, precio in productos.items():
            self.crear_boton_producto(productos_frame, producto, precio)

        # Configura el lienzo para que ajuste su región de desplazamiento cuando se redimensiona el marco de productos
        productos_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))  # Ajusta la región de desplazamiento
        )
        # Configura el lienzo para que ajuste el ancho de la ventana interna al redimensionarse
        canvas.bind(
            "<Configure>",
            lambda e: canvas.itemconfig(canvas_frame, width=e.width)  # Ajusta el ancho de la ventana interna
        )

    def crear_boton_producto(self, parent, producto, precio):
        # Crea un botón para un producto específico con su precio
        btn = tk.Button(
            parent,
            font=('Helvetica', 11),  # Estilo de la fuente del botón
            bg=self.colors['button'],  # Color de fondo del botón
            fg=self.colors['text'],  # Color del texto del botón
            text=f"{producto}\n${precio:,}",  # Texto del botón que incluye el nombre del producto y su precio formateado
            activebackground=self.colors['accent'],  # Color de fondo al activar el botón
            activeforeground=self.colors['text'],  # Color del texto al activar el botón
            relief="raised",  # Estilo de relieve del botón
            bd=3,  # Ancho del borde del botón
            width=30,  # Ancho del botón
            height=2,  # Altura del botón
            command=lambda p=producto, pr=precio: self.agregar_producto(p, pr)  # Comando al hacer clic en el botón
        )
        # Empaqueta el botón en el contenedor padre con espaciado
        btn.pack(pady=5, padx=10)


    def crear_panel_cuenta(self, parent):
        # Crea un marco etiquetado para la cuenta actual con estilo 'Premium.TLabelframe'
        cuenta_frame = ttk.LabelFrame(
            parent,
            text="💰 Cuenta Actual 💰",  # Título del marco
            padding="20",  # Espaciado interno
            style="Premium.TLabelframe"  # Estilo del marco
        )
        # Coloca el marco en la cuadrícula del contenedor padre
        cuenta_frame.grid(row=0, column=1, sticky="nsew")

        # Crea una etiqueta para mostrar información sobre la selección de mesa
        self.info_mesa = tk.Label(
            cuenta_frame,
            text="Seleccione una mesa",  # Texto de la etiqueta
            font=('Helvetica', 14, 'bold'),  # Estilo de la fuente
            fg=self.colors['text'],  # Color del texto
            bg=self.colors['panel']  # Color de fondo
        )
        self.info_mesa.pack(pady=(0, 10))  # Empaqueta la etiqueta con espaciado

        # Crea un área de texto para mostrar la lista de pedidos
        self.lista_pedidos = tk.Text(
            cuenta_frame,
            height=15,  # Altura del área de texto
            width=40,  # Ancho del área de texto
            font=('Helvetica', 12),  # Estilo de la fuente
            bg=self.colors['button'],  # Color de fondo
            fg=self.colors['text'],  # Color del texto
            relief="sunken",  # Estilo de relieve
            bd=3  # Ancho del borde
        )
        self.lista_pedidos.pack(pady=10, fill=tk.BOTH, expand=True)  # Empaqueta el área de texto

        # Crea una etiqueta para mostrar el total de la cuenta
        self.label_total = tk.Label(
            cuenta_frame,
            text="Total: $0",  # Texto de la etiqueta
            font=('Helvetica', 16, 'bold'),  # Estilo de la fuente
            fg=self.colors['accent'],  # Color del texto
            bg=self.colors['panel']  # Color de fondo
        )
        self.label_total.pack(pady=10)  # Empaqueta la etiqueta del total

        # Crea botones de acción en el marco de la cuenta
        self.crear_botones_accion(cuenta_frame)


    def crear_botones_accion(self, parent):
        # Crea un botón para pagar
        tk.Button(
            parent,
            text="💳 Pagar 💳 ",  # Texto del botón
            font=('Helvetica', 12, 'bold'),  # Estilo de la fuente
            bg=self.colors['success'],  # Color de fondo
            fg=self.colors['text'],  # Color del texto
            activebackground=self.colors['highlight'],  # Color de fondo al activar
            activeforeground=self.colors['text'],  # Color del texto al activar
            relief="raised",  # Estilo de relieve
            bd=3,  # Ancho del borde
            command=self.generar_recibo  # Comando al hacer clic
        ).pack(pady=5, fill=tk.X)  # Empaqueta el botón

        # Crea un botón para eliminar el último pedido
        tk.Button(
            parent,
            text="❌ Eliminar Último Pedido❌",  # Texto del botón
            font=('Helvetica', 12, 'bold'),  # Estilo de la fuente
            bg=self.colors['warning'],  # Color de fondo
            fg=self.colors['text'],  # Color del texto
            activebackground=self.colors['highlight'],  # Color de fondo al activar
            activeforeground=self.colors['text'],  # Color del texto al activar
            relief="raised",  # Estilo de relieve
            bd=3,  # Ancho del borde
            command=self.eliminar_ultimo_pedido  # Comando al hacer clic
        ).pack(pady=5, fill=tk.X)  # Empaqueta el botón

        # Crea un botón para apagar la aplicación
        tk.Button(
            parent,
            text="🔌 Apagar Aplicación",  # Texto del botón
            font=('Helvetica', 12, 'bold'),  # Estilo de la fuente
            bg=self.colors['warning'],  # Color de fondo
            fg=self.colors['text'],  # Color del texto
            activebackground=self.colors['highlight'],  # Color de fondo al activar
            activeforeground=self.colors['text'],  # Color del texto al activar
            relief="raised",  # Estilo de relieve
            bd=3,  # Ancho del borde
            command=self.apagar_aplicacion  # Comando al hacer clic
        ).pack(pady=5, fill=tk.X)  # Empaqueta el botón

        # Crea un botón para generar la factura electrónica
        tk.Button(
            parent,
            text="🧾 Factura Electrónica🧾",  # Texto del botón
            font=('Helvetica', 12, 'bold'),  # Estilo de la fuente
            bg=self.colors.get('info', self.colors['highlight']),  # Color de fondo
            fg=self.colors['text'],  # Color del texto
            activebackground=self.colors['highlight'],  # Color de fondo al activar
            activeforeground=self.colors['text'],  # Color del texto al activar
            relief="raised",  # Estilo de relieve
            bd=3,  # Ancho del borde
            command=self.generar_factura_electronica  # Comando al hacer clic
        ).pack(pady=5, fill=tk.X)  # Empaqueta el botón

        # Crea un botón para modificar productos
        tk.Button(
            parent,
            text="🛠 Modificar Productos",  # Texto del botón
            font=('Helvetica', 12, 'bold'),  # Estilo de la fuente
            bg=self.colors.get('info', self.colors['button']),  # Color de fondo
            fg=self.colors['text'],  # Color del texto
            activebackground=self.colors['highlight'],  # Color de fondo al activar
            activeforeground=self.colors['text'],  # Color del texto al activar
            relief="raised",  # Estilo de relieve
            bd=3,  # Ancho del borde
            command=self.abrir_ventana_modificacion  # Comando al hacer clic
        ).pack(pady=5, fill=tk.X)  # Empaqueta el botón

        # Crea un botón para ver las ventas del día
        tk.Button(
            parent,
            text="📊 Ver Ventas del Día 📊",  # Texto del botón
            font=('Helvetica', 12, 'bold'),  # Estilo de la fuente
            bg=self.colors['button'],  # Color de fondo
            fg=self.colors['text'],  # Color del texto
            command=self.analizar_ventas_del_dia  # Comando al hacer clic
        ).pack(pady=5, fill=tk.X)  # Empaqueta el botón

    

 
    def abrir_ventana_modificacion(self):
        # Crea una nueva ventana para modificar productos
        ventana_mod = tk.Toplevel(self.root)
        ventana_mod.title("Modificar Productos")  # Título de la ventana
        ventana_mod.geometry("800x600")  # Tamaño de la ventana
        ventana_mod.configure(bg=self.colors['background'])  # Color de fondo

        # Frame principal para contener los elementos de la ventana
        main_frame = ttk.Frame(ventana_mod, style="Premium.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)  # Empaqueta el frame principal

        # Etiqueta para el selector de categorías
        ttk.Label(
            main_frame,
            text="Seleccionar Categoría:",  # Texto de la etiqueta
            style="Premium.TLabel"  # Estilo de la etiqueta
        ).pack(pady=5)  # Empaqueta la etiqueta con un margen vertical

        # Variable para almacenar la categoría seleccionada
        categoria_var = tk.StringVar()
        
        # Combobox para seleccionar la categoría de productos
        combo_categorias = ttk.Combobox(
            main_frame,
            textvariable=categoria_var,  # Vincula la variable a este combobox
            values=list(self.categorias.keys())  # Carga las categorías disponibles
        )
        combo_categorias.pack(pady=5)  # Empaqueta el combobox con un margen vertical
        combo_categorias.set(list(self.categorias.keys())[0])  # Establece la primera categoría como seleccionada

        # Frame para listar los productos de la categoría seleccionada
        frame_productos = ttk.Frame(main_frame, style="Premium.TFrame")
        frame_productos.pack(fill=tk.BOTH, expand=True, pady=10)  # Empaqueta el frame de productos

        # Scrollbar para la lista de productos
        scrollbar = ttk.Scrollbar(frame_productos)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Empaqueta la scrollbar a la derecha

        # Lista donde se mostrarán los productos
        lista_productos = tk.Listbox(
            frame_productos,
            bg=self.colors['panel'],  # Color de fondo de la lista
            fg=self.colors['text'],  # Color del texto de la lista
            selectmode=tk.SINGLE,  # Permite seleccionar un solo elemento
            yscrollcommand=scrollbar.set,  # Conecta la scrollbar a la lista
            font=('Helvetica', 11)  # Estilo de la fuente de la lista
        )
        lista_productos.pack(fill=tk.BOTH, expand=True)  # Empaqueta la lista para que ocupe todo el espacio
        scrollbar.config(command=lista_productos.yview)  # Configura la scrollbar para controlar la vista de la lista

        # Función para actualizar la lista de productos según la categoría seleccionada
        def actualizar_lista_productos(*args):
            lista_productos.delete(0, tk.END)  # Limpia la lista de productos
            categoria = categoria_var.get()  # Obtiene la categoría seleccionada
            if categoria in self.categorias:  # Verifica si la categoría existe
                for producto, precio in self.categorias[categoria].items():
                    lista_productos.insert(tk.END, f"{producto} - ${precio:,}")  # Inserta productos en la lista

        categoria_var.trace('w', actualizar_lista_productos)  # Observa cambios en la categoría seleccionada
        actualizar_lista_productos()  # Llama a la función para llenar la lista inicialmente

        # Frame para botones de acción
        frame_botones = ttk.Frame(main_frame, style="Premium.TFrame")
        frame_botones.pack(fill=tk.X, pady=10)  # Empaqueta el frame de botones

        # Función para modificar un producto seleccionado
        def modificar_producto():
            seleccion = lista_productos.curselection()  # Obtiene el índice del producto seleccionado
            if not seleccion:  # Si no hay selección
                messagebox.showwarning("Aviso", "Por favor seleccione un producto")  # Muestra advertencia
                return

            producto_actual = lista_productos.get(seleccion[0]).split(" - ")[0]  # Obtiene el nombre del producto
            categoria = categoria_var.get()  # Obtiene la categoría seleccionada

            # Ventana para modificar el producto
            ventana_edit = tk.Toplevel(ventana_mod)
            ventana_edit.title("Editar Producto")  # Título de la ventana de edición
            ventana_edit.geometry("400x200")  # Tamaño de la ventana
            ventana_edit.configure(bg=self.colors['background'])  # Color de fondo

            # Etiqueta y campo de entrada para el nombre del producto
            ttk.Label(
                ventana_edit,
                text="Nombre del Producto:",
                style="Premium.TLabel"
            ).pack(pady=5)
            nombre_var = tk.StringVar(value=producto_actual)  # Variable para el nombre del producto
            entry_nombre = ttk.Entry(ventana_edit, textvariable=nombre_var)  # Campo de entrada para el nombre
            entry_nombre.pack(pady=5)

            # Etiqueta y campo de entrada para el precio
            ttk.Label(
                ventana_edit,
                text="Precio:",
                style="Premium.TLabel"
            ).pack(pady=5)
            precio_var = tk.StringVar(value=str(self.categorias[categoria][producto_actual]))  # Precio actual
            entry_precio = ttk.Entry(ventana_edit, textvariable=precio_var)  # Campo de entrada para el precio
            entry_precio.pack(pady=5)

            # Función para guardar los cambios realizados
            def guardar_cambios():
                try:
                    nuevo_precio = int(precio_var.get())  # Obtiene el nuevo precio
                    nuevo_nombre = nombre_var.get()  # Obtiene el nuevo nombre

                    if nuevo_nombre != producto_actual:  # Si el nombre ha cambiado
                        del self.categorias[categoria][producto_actual]  # Elimina el producto antiguo
                    self.categorias[categoria][nuevo_nombre] = nuevo_precio  # Agrega el nuevo producto

                    self.guardar_productos()  # Guarda los cambios
                    actualizar_lista_productos()  # Actualiza la lista de productos
                    self.crear_panel_productos(self.inner_frame)  # Regenera el panel de productos
                    ventana_edit.destroy()  # Cierra la ventana de edición
                    messagebox.showinfo("Éxito", "Producto modificado correctamente")  # Mensaje de éxito
                except ValueError:
                    messagebox.showerror("Error", "El precio debe ser un número válido")  # Manejo de error

            # Botón para guardar los cambios
            ttk.Button(
                ventana_edit,
                text="Guardar",
                command=guardar_cambios,
                style="Premium.TButton"
            ).pack(pady=10)

        # Función para agregar un nuevo producto
        def agregar_producto():
            categoria = categoria_var.get()  # Obtiene la categoría seleccionada

            # Ventana para agregar un nuevo producto
            ventana_add = tk.Toplevel(ventana_mod)
            ventana_add.title("Agregar Producto")  # Título de la ventana de agregar
            ventana_add.geometry("400x200")  # Tamaño de la ventana
            ventana_add.configure(bg=self.colors['background'])  # Color de fondo

            # Etiqueta y campo de entrada para el nombre del producto
            ttk.Label(
                ventana_add,
                text="Nombre del Producto:",
                style="Premium.TLabel"
            ).pack(pady=5)
            nombre_var = tk.StringVar()  # Variable para el nombre del nuevo producto
            entry_nombre = ttk.Entry(ventana_add, textvariable=nombre_var)  # Campo de entrada para el nombre
            entry_nombre.pack(pady=5)

            # Etiqueta y campo de entrada para el precio
            ttk.Label(
                ventana_add,
                text="Precio:",
                style="Premium.TLabel"
            ).pack(pady=5)
            precio_var = tk.StringVar()  # Variable para el precio del nuevo producto
            entry_precio = ttk.Entry(ventana_add, textvariable=precio_var)  # Campo de entrada para el precio
            entry_precio.pack(pady=5)

            # Función para guardar el nuevo producto
            def guardar_nuevo():
                try:
                    precio = int(precio_var.get())  # Obtiene el precio
                    nombre = nombre_var.get()  # Obtiene el nombre

                    if nombre and precio > 0:  # Verifica que los campos no estén vacíos
                        self.categorias[categoria][nombre] = precio  # Agrega el nuevo producto
                        self.guardar_productos()  # Guarda los cambios
                        actualizar_lista_productos()  # Actualiza la lista de productos
                        self.crear_panel_productos(self.inner_frame)  # Regenera el panel de productos
                        ventana_add.destroy()  # Cierra la ventana de agregar
                        messagebox.showinfo("Éxito", "Producto agregado correctamente")  # Mensaje de éxito
                    else:
                        messagebox.showwarning("Aviso", "Por favor complete todos los campos")  # Advertencia
                except ValueError:
                    messagebox.showerror("Error", "El precio debe ser un número válido")  # Manejo de error

            # Botón para guardar el nuevo producto
            ttk.Button(
                ventana_add,
                text="Guardar",
                command=guardar_nuevo,
                style="Premium.TButton"
            ).pack(pady=10)

        # Función para eliminar un producto seleccionado
        def eliminar_producto():
            seleccion = lista_productos.curselection()  # Obtiene el índice del producto seleccionado
            if not seleccion:  # Si no hay selección
                messagebox.showwarning("Aviso", "Por favor seleccione un producto")  # Muestra advertencia
                return

            # Confirma si el usuario quiere eliminar el producto
            if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este producto?"):
                producto = lista_productos.get(seleccion[0]).split(" - ")[0]  # Obtiene el nombre del producto
                categoria = categoria_var.get()  # Obtiene la categoría seleccionada
                del self.categorias[categoria][producto]  # Elimina el producto de la categoría
                self.guardar_productos()  # Guarda los cambios
                actualizar_lista_productos()  # Actualiza la lista de productos
                self.crear_panel_productos(self.inner_frame)  # Regenera el panel de productos
                messagebox.showinfo("Éxito", "Producto eliminado correctamente")  # Mensaje de éxito

        # Botones de acción
        ttk.Button(
            frame_botones,
            text="Modificar Seleccionado",
            command=modificar_producto,
            style="Premium.TButton"
        ).pack(side=tk.LEFT, padx=5)  # Botón para modificar el producto seleccionado

        ttk.Button(
            frame_botones,
            text="Agregar Nuevo",
            command=agregar_producto,
            style="Premium.TButton"
        ).pack(side=tk.LEFT, padx=5)  # Botón para agregar un nuevo producto

        ttk.Button(
            frame_botones,
            text="Eliminar Seleccionado",
            command=eliminar_producto,
            style="Premium.TButton"
        ).pack(side=tk.LEFT, padx=5)  # Botón para eliminar el producto seleccionado


    def guardar_productos(self):
        try:
            # Abre (o crea) el archivo 'productos.json' en modo escritura
            with open('productos.json', 'w', encoding='utf-8') as f:
                # Guarda el contenido de self.categorias en formato JSON
                json.dump(self.categorias, f, ensure_ascii=False, indent=4)
        except Exception as e:
            # Manejo de errores: muestra un mensaje si ocurre un problema al guardar
            messagebox.showerror("Error", f"Error al guardar productos: {str(e)}")

    def cargar_productos(self):
        try:
            # Verifica si el archivo 'productos.json' existe
            if os.path.exists('productos.json'):
                # Abre el archivo en modo lectura
                with open('productos.json', 'r', encoding='utf-8') as f:
                    # Carga el contenido del archivo JSON en self.categorias
                    self.categorias = json.load(f)
        except Exception as e:
            # Manejo de errores: muestra un mensaje si ocurre un problema al cargar
            messagebox.showerror("Error", f"Error al cargar productos: {str(e)}")

    def initialize_data(self):  # Control de datos de las mesas
        # Inicializa un diccionario para las mesas, cada una con su estado y pedidos
        self.mesas = {i: {
            "estado": "libre",  # Estado inicial de cada mesa
            "pedidos": [],  # Lista de pedidos para la mesa
            "total": 0.0,  # Total acumulado de la mesa
            "hora_inicio": None  # Hora de inicio del servicio
        } for i in range(1, 26)}  # Crea mesas del 1 al 25
        self.mesa_actual = None  # Inicializa la mesa actual como None

        # Cargar productos desde el archivo JSON si existe
        self.cargar_productos()
        
        # Si no hay productos cargados, usar los valores por defecto
        if not hasattr(self, 'categorias') or not self.categorias:
            self.categorias = {
                "🥃 litro 🥃": {
                    "Aguardiente Litro Azul": 100000,
                    "Aguardiente Verde/Rojo Litro": 98000,
                    "Ron Caldas Litro": 130000,
                    "Ron Medellín Litro": 120000,  
                },
                "🥃 media🥃": {
                    "Aguardiente Media Azul": 50000,
                    "Aguardiente Verde/Rojo Media": 48000,
                    "Ron Caldas Media": 56000,
                    "Ron Medellín Media": 52000,
                    "Whisky Media": 200000
                },
                " 🍹 trago 🍹 ": {
                    "Ron Caldas Trago": 5000,
                    "Aguardiente Trago": 4000,
                    "Tequila": 8000,
                    "Whisky Trago": 15000,
                    "Sangría Copa": 15000,
                },
                "🍺 Cervezas🍺": {
                    "Aguila": 5000,
                    "Aguila Lite": 5000,
                    "Pilsen": 5000,
                    "Poker": 5000,
                    "Coronita": 6000,
                    "Club Colombia": 6000,
                },
                " 🍺 Micheladas 🎉 ": {
                    "Aguila Michelada": 6000,
                    "Aguila Lite Michelada": 6000,
                    "Club Colombia Michelada": 7000,
                    "Poker Michelada": 6000,
                    "Pilsen Michelada": 6000,
                    "Coronita Michelada": 7000,
                    "Gaseosa Michelada": 5000,
                },
                "🥤 Bebidas🥤": {
                    "Gatorade": 5000,
                    "Electrolit": 13000,
                    "Agua Botella Grande": 4000,
                    "Agua Botella Personal": 3000,
                    "Tutti Fruti": 3000,
                    "Té de Limón": 3000,
                    "Sprite": 4000,
                    "Cuatro": 4000,
                    "Coca-Cola": 4000,
                    "Soda": 4000,
                },
                "🍸 Cocteles": {
                    "Margarita": 16000,
                    "Tequila Sunrise": 16000,
                },
                "Otros": {
                    "Vino Botella": 50000,
                    "Chicles": 3000,
                    "Alka Seltzer": 4000,
                    "Cigarillos": 1000,
                },
            }
            self.guardar_productos()  # Guarda los productos por defecto

    
            
    def analizar_ventas_del_dia(self):
        try:
            

            # Inicializar contadores y listas
            total_ventas = 0
            productos_vendidos = {}
            total_recibos = 0
            total_facturas = 0

            # Lista para almacenar detalles de cada documento
            detalles_recibos = []
            detalles_facturas = []

            fecha_actual = datetime.now().strftime("%Y-%m-%d")

            # Analizar recibos
            carpeta_recibos = "recibos"
            if os.path.exists(carpeta_recibos):
                for archivo in os.listdir(carpeta_recibos):
                    if archivo.endswith('.pdf'):
                        ruta_archivo = os.path.join(carpeta_recibos, archivo)
                        try:
                            reader = PdfReader(ruta_archivo)
                            texto = reader.pages[0].extract_text()

                            if fecha_actual in texto:
                                total_recibos += 1

                                # Extraer información del recibo
                                match_mesa = re.search(r'Mesa: (\d+)', texto)
                                match_total = re.search(r'Total: \$([0-9,]+(?:\.[0-9]{2})?)', texto)
                                match_hora = re.search(r'Hora: (\d{2}:\d{2})', texto)

                                if match_mesa and match_total:
                                    mesa = match_mesa.group(1)
                                    total_str = match_total.group(1).replace(',', '')
                                    total = float(total_str)
                                    hora = match_hora.group(1) if match_hora else "N/A"

                                    detalles_recibos.append({
                                        'mesa': mesa,
                                        'total': total,
                                        'hora': hora,
                                        'archivo': archivo
                                    })

                                    total_ventas += total

                                    # Extraer productos
                                    lineas = texto.split('\n')
                                    for linea in lineas:
                                        if '$' in linea and 'Total' not in linea:
                                            producto = linea.split('$')[0].strip()
                                            if producto:
                                                productos_vendidos[producto] = productos_vendidos.get(producto, 0) + 1

                        except Exception as e:
                            print(f"Error al leer recibo {archivo}: {str(e)}")

            # Analizar facturas
            carpeta_facturas = "facturas"
            if os.path.exists(carpeta_facturas):
                for archivo in os.listdir(carpeta_facturas):
                    if archivo.endswith('.pdf'):
                        try:
                            reader = PdfReader(os.path.join(carpeta_facturas, archivo))
                            texto = reader.pages[0].extract_text()

                            if fecha_actual in texto:
                                total_facturas += 1

                                # Extraer información de la factura
                                match_cliente = re.search(r'Cliente: (.*)', texto)
                                match_total = re.search(r'Total: \$([0-9,]+(?:\.[0-9]{2})?)', texto)
                                match_hora = re.search(r'Hora: (\d{2}:\d{2})', texto)

                                if match_cliente and match_total:
                                    cliente = match_cliente.group(1)
                                    total_str = match_total.group(1).replace(',', '')
                                    total = float(total_str)
                                    hora = match_hora.group(1) if match_hora else "N/A"

                                    detalles_facturas.append({
                                        'cliente': cliente,
                                        'total': total,
                                        'hora': hora,
                                        'archivo': archivo
                                    })

                        except Exception as e:
                            print(f"Error al leer factura {archivo}: {str(e)}")

            # Crear ventana de resultados
            ventana_resumen = tk.Toplevel(self.root)
            ventana_resumen.title("Resumen Detallado de Ventas del Día")
            ventana_resumen.geometry("800x900")
            ventana_resumen.configure(bg=self.colors['background'])

            # Crear Text widget
            texto_resumen = tk.Text(
                ventana_resumen,
                font=('Helvetica', 12),
                bg=self.colors['panel'],
                fg=self.colors['text'],
                padx=20,
                pady=20
            )
            texto_resumen.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

            # Insertar información detallada
            texto_resumen.insert(tk.END, f"📊 RESUMEN DE VENTAS - {fecha_actual} 📊\n\n")
            texto_resumen.insert(tk.END, f"💰 Total de Ventas: ${total_ventas:,.2f}\n")
            texto_resumen.insert(tk.END, f"🧾 Recibos Generados: {total_recibos}\n")
            texto_resumen.insert(tk.END, f"📄 Facturas Generadas: {total_facturas}\n\n")

            # Detalles de recibos
            texto_resumen.insert(tk.END, "🧾 DETALLE DE RECIBOS:\n")
            texto_resumen.insert(tk.END, "------------------------\n")
            for recibo in sorted(detalles_recibos, key=lambda x: x['hora']):
                texto_resumen.insert(tk.END, 
                    f"Mesa {recibo['mesa']} - Hora: {recibo['hora']} - Total: ${recibo['total']:,.2f}\n")

            # Detalles de facturas
            texto_resumen.insert(tk.END, "\n📄 DETALLE DE FACTURAS:\n")
            texto_resumen.insert(tk.END, "------------------------\n")
            for factura in sorted(detalles_facturas, key=lambda x: x['hora']):
                texto_resumen.insert(tk.END, 
                    f"Cliente: {factura['cliente']} - Hora: {factura['hora']} - Total: ${factura['total']:,.2f}\n")

            # Productos vendidos
            texto_resumen.insert(tk.END, "\n📋 PRODUCTOS VENDIDOS HOY:\n")
            texto_resumen.insert(tk.END, "------------------------\n")
            for producto, cantidad in sorted(productos_vendidos.items()):
                texto_resumen.insert(tk.END, f"➤ {producto}: {cantidad} unidades\n")

            texto_resumen.configure(state='disabled')

            # Botón para guardar resumen en PDF
            tk.Button(
                ventana_resumen,
                text="Guardar Resumen en PDF",
                font=('Helvetica', 12, 'bold'),
                bg=self.colors['button'],
                fg=self.colors['text'],
                command=lambda: self.guardar_resumen_pdf(
                    fecha_actual, total_ventas, total_recibos, total_facturas, detalles_recibos, detalles_facturas, productos_vendidos
                )
            ).pack(pady=10)

            # Botón para cerrar
            tk.Button(
                ventana_resumen,
                text="Cerrar Resumen",
                font=('Helvetica', 12, 'bold'),
                bg=self.colors['button'],
                fg=self.colors['text'],
                command=ventana_resumen.destroy
            ).pack(pady=10)

        except Exception as e:
            messagebox.showerror("Error", f"Error al generar el resumen: {str(e)}")


    def guardar_resumen_pdf(self, fecha, total_ventas, total_recibos, total_facturas, detalles_recibos, detalles_facturas, productos_vendidos):
        try:
            # Crear directorio para reportes si no existe
            os.makedirs("reportes", exist_ok=True)
            
            # Nombre del archivo
            filename = f"reportes/resumen_ventas_{fecha}.pdf"
            
            # Crear el PDF
            doc = SimpleDocTemplate(
                filename,
                pagesize=letter,
                rightMargin=72,
                leftMargin=72,
                topMargin=72,
                bottomMargin=72
            )
            
            # Estilos para el PDF
            styles = getSampleStyleSheet()
            
            # Contenido del PDF
            elements = []
            
            # Título
            elements.append(Paragraph(f"RESUMEN DE VENTAS - {fecha}", styles["Heading1"]))
            elements.append(Spacer(1, 12))
            
            # Información general
            data = [
                ["Total Ventas:", f"${total_ventas:,.2f}"],
                ["Recibos:", str(total_recibos)],
                ["Facturas:", str(total_facturas)]
            ]
            table = Table(data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,0), colors.grey),
                ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
                ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('FONTSIZE', (0,0), (-1,0), 14),
                ('BOTTOMPADDING', (0,0), (-1,0), 12),
                ('BACKGROUND', (0,1), (-1,-1), colors.beige),
                ('GRID', (0,0), (-1,-1), 1, colors.black)
            ]))
            elements.append(table)
            elements.append(Spacer(1, 12))
            
            # Detalle de ventas
            elements.append(Paragraph("Detalle de Ventas", styles["Heading2"]))
            
            # Crear lista combinada de detalles con el tipo de documento
            detalles_combinados = []
            for recibo in detalles_recibos:
                detalles_combinados.append({
                    'hora': recibo['hora'],
                    'tipo': 'Recibo',
                    'identificador': f"Mesa {recibo['mesa']}",
                    'total': recibo['total']
                })
            
            for factura in detalles_facturas:
                detalles_combinados.append({
                    'hora': factura['hora'],
                    'tipo': 'Factura',
                    'identificador': factura['cliente'],
                    'total': factura['total']
                })
            
            # Ordenar por hora
            detalles_combinados.sort(key=lambda x: x['hora'])
            
            # Crear tabla de detalles
            data = [["Hora", "Tipo", "Identificador", "Total"]]
            data.extend([
                [detalle['hora'], detalle['tipo'], detalle['identificador'], f"${detalle['total']:,.2f}"]
                for detalle in detalles_combinados
            ])
            
            table = Table(data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,0), colors.grey),
                ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
                ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('FONTSIZE', (0,0), (-1,0), 14),
                ('BOTTOMPADDING', (0,0), (-1,0), 12),
                ('BACKGROUND', (0,1), (-1,-1), colors.white),
                ('GRID', (0,0), (-1,-1), 1, colors.black)
            ]))
            elements.append(table)
            
            # Productos más vendidos
            elements.append(Paragraph("Productos Más Vendidos", styles["Heading2"]))
            data = [["Producto", "Cantidad"]]
            data.extend([
                [producto, str(cantidad)]
                for producto, cantidad in sorted(productos_vendidos.items(), key=lambda x: x[1], reverse=True)
            ])
            table = Table(data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,0), colors.grey),
                ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
                ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('FONTSIZE', (0,0), (-1,0), 14),
                ('BOTTOMPADDING', (0,0), (-1,0), 12),
                ('BACKGROUND', (0,1), (-1,-1), colors.white),
                ('GRID', (0,0), (-1,-1), 1, colors.black)
            ]))
            elements.append(table)
            
            # Construir el PDF
            doc.build(elements)

            # Mensaje de éxito
            messagebox.showinfo("Éxito", f"Resumen de ventas exportado a: {filename}")

        except Exception as e:
            messagebox.showerror("Error", f"Error al exportar el resumen: {str(e)}")

    
    def generar_factura_electronica(self):
        if self.mesa_actual is None:
            messagebox.showwarning("Aviso", "Por favor seleccione una mesa primero.")
            return

        mesa_info = self.mesas[self.mesa_actual]
        pedidos = mesa_info['pedidos']
        total = mesa_info['total']
        fecha = datetime.now().strftime("%Y-%m-%d")
        hora = datetime.now().strftime("%H:%M:%S")

        # Solicitar datos del cliente
        nombre_cliente = simpledialog.askstring("Datos del Cliente", "Ingrese el nombre del cliente:")
        if not nombre_cliente:
            return
        direccion_cliente = simpledialog.askstring("Datos del Cliente", "Ingrese la dirección del cliente:")
        if not direccion_cliente:
            return
        cedula_NIT_cliente = simpledialog.askstring("Datos del Cliente", "Ingrese la cédula/NIT del cliente:")
        if not cedula_NIT_cliente:
            return
        telefono_cliente = simpledialog.askstring("Datos del Cliente", "Ingrese el teléfono del cliente:")
        if not telefono_cliente:
            return

        # Crear la carpeta para las facturas si no existe
        carpeta_facturas = "facturas"
        os.makedirs(carpeta_facturas, exist_ok=True)

        # Generar el nombre del archivo PDF
        filename = os.path.join(carpeta_facturas, f"factura_{nombre_cliente.replace(' ', '_')}.pdf")
        pdf = canvas.Canvas(filename, pagesize=A4)
        pdf.setFont("Helvetica", 12)

        # Escribir información en el PDF
        try:
            pdf.drawString(100, 800, f"Nombre del Local: {self.facturacion.config['nombre_empresa']}")
            pdf.drawString(100, 780, f"NIT: {self.facturacion.config['nit_empresa']}")
            pdf.drawString(100, 760, f"Dirección: {self.facturacion.config['direccion_empresa']}")
            pdf.drawString(100, 740, f"Teléfono: {self.facturacion.config['telefono_empresa']}")
            pdf.drawString(100, 720, f"Régimen: {self.facturacion.config['regimen']}")
            pdf.drawString(100, 700, f"Resolución DIAN: {self.facturacion.config['resolucion_dian']}")
            pdf.drawString(100, 680, f"Fecha: {fecha}")
            pdf.drawString(100, 660, f"Hora: {hora}")
            pdf.drawString(100, 640, f"Número de Mesa: {self.mesa_actual}")
            pdf.drawString(100, 620, f"Cliente: {nombre_cliente}")
            pdf.drawString(100, 600, f"Dirección: {direccion_cliente}")
            pdf.drawString(350, 640, f"Cédula/NIT: {cedula_NIT_cliente}")
            pdf.drawString(350, 620, f"Teléfono: {telefono_cliente}")

            # Detalle de pedidos
            pdf.drawString(100, 580, "Detalle de Compras:")
            y_position = 560
            for producto, precio in pedidos:
                pdf.drawString(100, y_position, f"{producto}: ${precio:.2f}")
                y_position -= 20

            pdf.drawString(100, y_position - 20, f"Total: ${total:.2f}")

            # Finalizar PDF
            pdf.save()

            messagebox.showinfo("Éxito", f"Factura generada: {filename}")

            # Limpiar mesa actual después de generar la factura
            self.mesas[self.mesa_actual]['pedidos'] = []
            self.mesas[self.mesa_actual]['total'] = 0.0
            self.mesa_actual = None

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al generar la factura: {str(e)}")

        

    def generar_recibo(self):
        if self.mesa_actual is None:
            messagebox.showwarning("Aviso", "Por favor seleccione una mesa primero.")
            return

        # Obtener información de la mesa
        mesa_info = self.mesas[self.mesa_actual]
        pedidos = mesa_info['pedidos']
        total = mesa_info['total']
        fecha = datetime.now().strftime("%Y-%m-%d")
        hora = datetime.now().strftime("%H:%M:%S")

        # Especificar la carpeta donde se guardarán los PDFs
        carpeta_recibos = "recibos"
        os.makedirs(carpeta_recibos, exist_ok=True)  # Crear la carpeta si no existe

        # Generar el nombre del archivo PDF
        filename = os.path.join(carpeta_recibos, f"recibo_mesa_{self.mesa_actual}.pdf")
        pdf = canvas.Canvas(filename, pagesize=A4)
        pdf.setFont("Helvetica", 12)

        # Escribir información en el PDF
        pdf.drawString(100, 800, f"Nombre del Local: {self.facturacion.config['nombre_empresa']}")
        pdf.drawString(100, 780, f"Fecha: {fecha}")
        pdf.drawString(100, 760, f"Hora: {hora}")
        pdf.drawString(100, 740, f"Número de Mesa: {self.mesa_actual}")

        # Detalle de pedidos
        pdf.drawString(100, 700, "Detalle de Compras:")
        y_position = 680
        for producto, precio in pedidos:
            pdf.drawString(100, y_position, f"{producto}: ${precio:.2f}")
            y_position -= 20

        pdf.drawString(100, y_position - 20, f"Total: ${total:.2f}")

        # Finalizar PDF
        pdf.save()

        messagebox.showinfo("Éxito", f"Recibo generado: {filename}")

        # Limpiar mesa actual después de pagar
        self.mesas[self.mesa_actual]['pedidos'] = []
        self.mesas[self.mesa_actual]['total'] = 0.0
        self.mesa_actual = None
    
    def seleccionar_mesa(self, numero):
        # Selecciona la mesa indicada por el número
        self.mesa_actual = numero
        # Si la mesa está libre, se registra la hora de inicio
        if self.mesas[numero]["estado"] == "libre":
            self.mesas[numero]["hora_inicio"] = datetime.now()
        # Actualiza la vista de la mesa seleccionada
        self.actualizar_vista_mesa()

    def agregar_producto(self, producto, precio):
        # Verifica si se ha seleccionado una mesa
        if self.mesa_actual is None:
            messagebox.showwarning("Aviso", "Por favor seleccione una mesa primero")
            return

        # Agrega el producto y su precio a la lista de pedidos de la mesa actual
        self.mesas[self.mesa_actual]["pedidos"].append((producto, precio))
        # Actualiza el total de la mesa
        self.mesas[self.mesa_actual]["total"] += precio
        # Cambia el estado de la mesa a ocupada
        self.mesas[self.mesa_actual]["estado"] = "ocupada"
        # Actualiza la vista de la mesa
        self.actualizar_vista_mesa()

    def eliminar_ultimo_pedido(self):
        # Verifica si se ha seleccionado una mesa
        if self.mesa_actual is None:
            messagebox.showwarning("Aviso", "Por favor seleccione una mesa primero")
            return

        mesa_data = self.mesas[self.mesa_actual]
        # Verifica si hay pedidos para eliminar
        if mesa_data["pedidos"]:
            # Elimina el último pedido
            producto, precio = mesa_data["pedidos"].pop()
            # Actualiza el total de la mesa
            mesa_data["total"] -= precio
            # Si no hay más pedidos, cambia el estado a libre
            if not mesa_data["pedidos"]:
                mesa_data["estado"] = "libre"
                mesa_data["hora_inicio"] = None
            # Actualiza la vista de la mesa
            self.actualizar_vista_mesa()
        else:
            messagebox.showinfo("Información", "No hay pedidos para eliminar")

    
    def actualizar_vista_mesa(self):
        # Verifica si hay una mesa seleccionada
        if self.mesa_actual is None:
            return

        mesa_data = self.mesas[self.mesa_actual]
        estado_texto = mesa_data['estado'].upper()  # Obtiene el estado de la mesa en mayúsculas
        # Define el color basado en el estado de la mesa
        color_estado = self.colors['success'] if estado_texto == "LIBRE" else self.colors['warning']

        tiempo_transcurrido = ""
        # Calcula el tiempo transcurrido desde que se ocupó la mesa
        if mesa_data["hora_inicio"]:
            tiempo = datetime.now() - mesa_data["hora_inicio"]
            horas = tiempo.seconds // 3600
            minutos = (tiempo.seconds % 3600) // 60
            tiempo_transcurrido = f"\nTiempo: {horas}h {minutos}m"

        # Actualiza el texto de la información de la mesa
        self.info_mesa.config(
            text=f"Mesa {self.mesa_actual} - {estado_texto}{tiempo_transcurrido}",
            fg=color_estado
        )

        # Limpia la lista de pedidos y la actualiza con los productos de la mesa
        self.lista_pedidos.delete(1.0, tk.END)
        for producto, precio in mesa_data["pedidos"]:
            self.lista_pedidos.insert(tk.END, f"➤ {producto}: ${precio:,}\n")

        # Actualiza la etiqueta del total
        self.label_total.config(text=f"Total: ${mesa_data['total']:,}")

 
    def imprimir_recibo(self, venta):
        try:
            # Crear directorio para recibos si no existe
            Path("recibos").mkdir(exist_ok=True)

            # Nombre del archivo
            fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"recibos/recibo_mesa_{venta['mesa']}_{fecha}.pdf"

            # Crear PDF
            c = canvas.Canvas(filename, pagesize=A4)
            c.setFont("Helvetica-Bold", 24)
            c.drawString(50, 800, "VIEJA GUARDIA")

            c.setFont("Helvetica", 12)
            c.drawString(50, 770, f"Fecha: {venta['fecha']}")
            c.drawString(50, 750, f"Mesa: {venta['mesa']}")
            c.drawString(50, 730, f"Tiempo total: {venta['tiempo']}")

            y = 700
            total = 0

            # Dibujar línea de encabezado
            c.line(50, y + 10, 500, y + 10)
            c.drawString(50, y - 10, "Producto")
            c.drawString(450, y - 10, "Precio")
            c.line(50, y - 20, 500, y - 20)
            y -= 40

            # Listar productos
            for producto, precio in venta["pedidos"]:
                c.drawString(50, y, f"{producto}")
                c.drawString(450, y, f"${precio:,}")
                y -= 20
                total += precio

            # Total
            c.line(50, y - 10, 500, y - 10)
            c.setFont("Helvetica-Bold", 14)
            c.drawString(350, y - 40, f"Total: ${total:,}")

            # Mensaje de agradecimiento
            c.setFont("Helvetica-Oblique", 12)
            c.drawString(50, y - 80, "¡Gracias por su visita!")

            c.save()
            # Intentar imprimir
            try:
                os.startfile(filename, "print")
            except Exception as e:
                messagebox.showinfo("Información", f"Recibo guardado como: {filename}")

        except Exception as e:
            messagebox.showerror("Error", f"Error al generar recibo: {str(e)}")

    def apagar_aplicacion(self):
        if messagebox.askokcancel("Salir", "¿Desea cerrar la aplicación?"):
            self.root.destroy()

def generar_factura_electronica(self):
    # Verifica si hay una mesa seleccionada y si tiene pedidos
    if self.mesa_actual is None or not self.mesas[self.mesa_actual]["pedidos"]:
        messagebox.showwarning("Aviso", "No hay pedidos para pagar")
        return
        
    # Crea un diccionario con los detalles de la venta
    venta = {
        'fecha': datetime.now().strftime('%d/%m/%Y %H:%M'),  # Fecha y hora actual
        'mesa': self.mesa_actual,  # Número de la mesa
        'pedidos': self.mesas[self.mesa_actual]['pedidos'],  # Lista de pedidos
        'total': self.mesas[self.mesa_actual]['total'],  # Total a pagar
        'tiempo': str(datetime.now() - self.mesas[self.mesa_actual]['hora_inicio']) if self.mesas[self.mesa_actual]['hora_inicio'] else "N/A"  # Tiempo transcurrido
    }

    # Aquí podrías agregar la lógica para generar la factura electrónica, como guardarla en un archivo o enviarla a un servicio externo.

        
if __name__ == "__main__": 
    root = tk.Tk()  # Crea la ventana principal de la aplicación
    app = BarPremiumApp(root)  # Crea una instancia de la aplicación
    root.mainloop()  # Inicia el bucle principal de la interfaz gráfica

    
