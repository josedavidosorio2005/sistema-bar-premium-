import re
import json
import tkinter as tk  # Importa el módulo principal de Tkinter
from tkinter import ttk, messagebox  # Importa ttk para widgets mejorados y messagebox para diálogos de mensajes
from datetime import datetime  # Importa datetime para manejar fechas y horas
import locale
from tkinter import simpledialog
from tkinter.tix import Meter  # Importa locale para establecer configuraciones regionales
from reportlab.pdfgen import canvas  # Importa canvas de reportlab para crear PDFs
from reportlab.lib.pagesizes import A4  # Importa el tamaño de página A4
import os  # Importa os para interactuar con el sistema de archivos
from pathlib import Path  # Importa Path de pathlib para manejar rutas de archivos
from typing import Dict, List
from reportlab.pdfgen import canvas  # Importa canvas de reportlab para crear PDFs
from reportlab.lib.pagesizes import A4  # Importa el tamaño de página A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import os
from reportlab.lib.pagesizes import letter
from datetime import datetime
from PyPDF2 import PdfReader

class FacturaElectronica:

    def __init__(self):
        self.config = {
            'nombre_empresa': ' VIEJA GUARDIA BAR',
            'nit_empresa': ' 900.123.456-7',
            'direccion_empresa': ' Calle Principal #123',
            'telefono_empresa': ' (601) 123-4567',
            'regimen': ' RÉGIMEN COMÚN',
            'resolucion_dian': ' Resolución DIAN No. 12345678 del 2024/01/01',
            'prefijo_factura': ' VG',
            'consecutivo_actual': 1
        }
        
        return 

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
        main_frame = ttk.Frame(self.root, style="Premium.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.crear_header(main_frame)
        self.crear_contenedor_scroll(main_frame)
        self.crear_panel_mesas()

        bottom_frame = ttk.Frame(self.inner_frame, style="Premium.TFrame")
        bottom_frame.pack(fill=tk.BOTH, expand=True, pady=(20, 0))

        bottom_frame.columnconfigure(0, weight=3)
        bottom_frame.columnconfigure(1, weight=2)

        self.crear_panel_productos(bottom_frame)
        self.crear_panel_cuenta(bottom_frame)

    def crear_header(self, parent):
        header_frame = ttk.Frame(parent, style="Premium.TFrame")
        header_frame.pack(fill=tk.X, pady=(0, 20))

        title_label = tk.Label(
            header_frame,
            text="✯ VIEJA GUARDIA ✯",
            font=('Helvetica', 36, 'bold'),
            fg=self.colors['accent'],
            bg=self.colors['background']
        )
        title_label.pack(pady=(10, 5))

        subtitle_label = tk.Label(
            header_frame,
            text="Sistema Premium de Bar",
            font=('Helvetica', 16),
            fg=self.colors['text'],
            bg=self.colors['background']
        )
        subtitle_label.pack(pady=(0, 10))

    def crear_contenedor_scroll(self, parent):
        scroll_frame = ttk.Frame(parent, style="Premium.TFrame")
        scroll_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(
            scroll_frame,
            bg=self.colors['background'],
            highlightthickness=0
        )
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar_y = ttk.Scrollbar(
            scroll_frame,
            orient="vertical",
            command=self.canvas.yview,
            style="Premium.Vertical.TScrollbar"
        )

        self.scrollbar_x = ttk.Scrollbar(
            scroll_frame,
            orient="horizontal",
            command=self.canvas.xview,
            style="Premium.Horizontal.TScrollbar"
        )

        self.canvas.configure(
            yscrollcommand=self.scrollbar_y.set,
            xscrollcommand=self.scrollbar_x.set
        )

        self.inner_frame = ttk.Frame(self.canvas, style="Premium.TFrame")
        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.inner_frame,
            anchor="nw"
        )

        self.inner_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_window, width=event.width)

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def crear_panel_mesas(self):
        mesas_frame = ttk.LabelFrame(
            self.inner_frame,
            text="🏮 Mesas Disponibles",
            padding="20",
            style="Premium.TLabelframe"
        )
        mesas_frame.pack(fill=tk.X, pady=(0, 20))

        for i in range(5):
            mesas_frame.columnconfigure(i, weight=1)

        for i, mesa_num in enumerate(self.mesas.keys()):
            self.crear_boton_mesa(mesas_frame, mesa_num, i)

    def crear_boton_mesa(self, parent, mesa_num, index):
        estado = self.mesas[mesa_num]["estado"]
        color_fondo = self.colors['success'] if estado == "libre" else self.colors['warning']
        btn = tk.Button(
            parent,
            text=f"Mesa {mesa_num}\n{'🟢' if estado == 'libre' else '🟡'}",
            font=('Helvetica', 11, 'bold'),
            bg=color_fondo,
            fg=self.colors['text'],
            relief="raised",
            bd=3,
            command=lambda m=mesa_num: self.seleccionar_mesa(m)
        )
        btn.grid(
            row=index // 5,
            column=index % 5,
            padx=5,
            pady=5,
            sticky="nsew"
        )

    def crear_panel_productos(self, parent):
        productos_frame = ttk.LabelFrame(
            parent,
            text="🍾 Menú Vieja Guardia",
            padding="20",
            style="Premium.TLabelframe"
        )
        productos_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        notebook = ttk.Notebook(
            productos_frame,
            style="Premium.TNotebook"
        )
        notebook.pack(fill=tk.BOTH, expand=True)

        for categoria, productos in self.categorias.items():
            self.crear_tab_categoria(notebook, categoria, productos)

    def crear_tab_categoria(self, notebook, categoria, productos):
        tab = ttk.Frame(notebook, style="Premium.TFrame", padding=10)
        notebook.add(tab, text=categoria)

        canvas = tk.Canvas(
            tab,
            bg=self.colors['panel'],
            highlightthickness=0
        )
        scrollbar = ttk.Scrollbar(
            tab,
            orient="vertical",
            command=canvas.yview,
            style="Premium.Vertical.TScrollbar"
        )

        productos_frame = ttk.Frame(canvas, style="Premium.TFrame")

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas_frame = canvas.create_window(
            (0, 0),
            window=productos_frame,
            anchor="nw"
        )

        for producto, precio in productos.items():
            self.crear_boton_producto(productos_frame, producto, precio)

        productos_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.bind(
            "<Configure>",
            lambda e: canvas.itemconfig(canvas_frame, width=e.width)
        )

    def crear_boton_producto(self, parent, producto, precio):
        btn = tk.Button(
            parent,
            font=('Helvetica', 11),
            bg=self.colors['button'],
            fg=self.colors['text'],
            text=f"{producto}\n${precio:,}",
            activebackground=self.colors['accent'],
            activeforeground=self.colors['text'],
            relief="raised",
            bd=3,
            width=30,
            height=2,
            command=lambda p=producto, pr=precio: self.agregar_producto(p, pr)
        )
        btn.pack(pady=5, padx=10)

    def crear_panel_cuenta(self, parent):
        cuenta_frame = ttk.LabelFrame(
            parent,
            text="💰 Cuenta Actual 💰",
            padding="20",
            style="Premium.TLabelframe"
        )
        cuenta_frame.grid(row=0, column=1, sticky="nsew")

        self.info_mesa = tk.Label(
            cuenta_frame,
            text="Seleccione una mesa",
            font=('Helvetica', 14, 'bold'),
            fg=self.colors['text'],
            bg=self.colors['panel']
        )
        self.info_mesa.pack(pady=(0, 10))

        self.lista_pedidos = tk.Text(
            cuenta_frame,
            height=15,
            width=40,
            font=('Helvetica', 12),
            bg=self.colors['button'],
            fg=self.colors['text'],
            relief="sunken",
            bd=3
        )
        self.lista_pedidos.pack(pady=10, fill=tk.BOTH, expand=True)

        self.label_total = tk.Label(
            cuenta_frame,
            text="Total: $0",
            font=('Helvetica', 16, 'bold'),
            fg=self.colors['accent'],
            bg=self.colors['panel']
        )
        self.label_total.pack(pady=10)

        self.crear_botones_accion(cuenta_frame)
    

    def crear_botones_accion(self, parent):
        tk.Button(
            parent,
            text="💳 Pagar 💳 ",
            font=('Helvetica', 12, 'bold'),
            bg=self.colors['success'],
            fg=self.colors['text'],
            activebackground=self.colors['highlight'],
            activeforeground=self.colors['text'],
            relief="raised",
            bd=3,
            command=self.generar_recibo
        ).pack(pady=5, fill=tk.X)

        tk.Button(
            parent,
            text="❌ Eliminar Último Pedido❌",
            font=('Helvetica', 12, 'bold'),
            bg=self.colors['warning'],
            fg=self.colors['text'],
            activebackground=self.colors['highlight'],
            activeforeground=self.colors['text'],
            relief="raised",
            bd=3,
            command=self.eliminar_ultimo_pedido
        ).pack(pady=5, fill=tk.X)

        tk.Button(
            parent,
            text="🔌 Apagar Aplicación",
            font=('Helvetica', 12, 'bold'),
            bg=self.colors['warning'],
            fg=self.colors['text'],
            activebackground=self.colors['highlight'],
            activeforeground=self.colors['text'],
            relief="raised",
            bd=3,
            command=self.apagar_aplicacion
        ).pack(pady=5, fill=tk.X)

        tk.Button(
            parent,
            text="🧾 Factura Electrónica🧾",
            font=('Helvetica', 12, 'bold'),
            bg=self.colors.get('info', self.colors['highlight']),
            fg=self.colors['text'],
            activebackground=self.colors['highlight'],
            activeforeground=self.colors['text'],
            relief="raised",
            bd=3,
            command=self.generar_factura_electronica
        ).pack(pady=5, fill=tk.X)

        tk.Button(
            parent,
            text="🛠 Modificar Productos",
            font=('Helvetica', 12, 'bold'),
            bg=self.colors.get('info', self.colors['button']),
            fg=self.colors['text'],
            activebackground=self.colors['highlight'],
            activeforeground=self.colors['text'],
            relief="raised",
            bd=3,
            command=self.abrir_ventana_modificacion
        ).pack(pady=5, fill=tk.X)
       
        tk.Button(
            parent,
            text="📊 Ver Ventas del Día 📊",
            font=('Helvetica', 12, 'bold'),
            bg=self.colors['button'],
            fg=self.colors['text'],
            command=self.analizar_ventas_del_dia
        ).pack(pady=5, fill=tk.X)
 
 
    

 
    def abrir_ventana_modificacion(self):
        ventana_mod = tk.Toplevel(self.root)
        ventana_mod.title("Modificar Productos")
        ventana_mod.geometry("800x600")
        ventana_mod.configure(bg=self.colors['background'])

        # Frame principal
        main_frame = ttk.Frame(ventana_mod, style="Premium.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Selector de categoría
        ttk.Label(
            main_frame,
            text="Seleccionar Categoría:",
            style="Premium.TLabel"
        ).pack(pady=5)

        categoria_var = tk.StringVar()
        combo_categorias = ttk.Combobox(
            main_frame,
            textvariable=categoria_var,
            values=list(self.categorias.keys())
        )
        combo_categorias.pack(pady=5)
        combo_categorias.set(list(self.categorias.keys())[0])

        # Lista de productos
        frame_productos = ttk.Frame(main_frame, style="Premium.TFrame")
        frame_productos.pack(fill=tk.BOTH, expand=True, pady=10)

        # Scrollbar para la lista de productos
        scrollbar = ttk.Scrollbar(frame_productos)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        lista_productos = tk.Listbox(
            frame_productos,
            bg=self.colors['panel'],
            fg=self.colors['text'],
            selectmode=tk.SINGLE,
            yscrollcommand=scrollbar.set,
            font=('Helvetica', 11)
        )
        lista_productos.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=lista_productos.yview)

        def actualizar_lista_productos(*args):
            lista_productos.delete(0, tk.END)
            categoria = categoria_var.get()
            if categoria in self.categorias:
                for producto, precio in self.categorias[categoria].items():
                    lista_productos.insert(tk.END, f"{producto} - ${precio:,}")

        categoria_var.trace('w', actualizar_lista_productos)
        actualizar_lista_productos()

        # Frame para botones de acción
        frame_botones = ttk.Frame(main_frame, style="Premium.TFrame")
        frame_botones.pack(fill=tk.X, pady=10)

        def modificar_producto():
            seleccion = lista_productos.curselection()
            if not seleccion:
                messagebox.showwarning("Aviso", "Por favor seleccione un producto")
                return

            producto_actual = lista_productos.get(seleccion[0]).split(" - ")[0]
            categoria = categoria_var.get()

            # Ventana para modificar
            ventana_edit = tk.Toplevel(ventana_mod)
            ventana_edit.title("Editar Producto")
            ventana_edit.geometry("400x200")
            ventana_edit.configure(bg=self.colors['background'])

            ttk.Label(
                ventana_edit,
                text="Nombre del Producto:",
                style="Premium.TLabel"
            ).pack(pady=5)
            nombre_var = tk.StringVar(value=producto_actual)
            entry_nombre = ttk.Entry(ventana_edit, textvariable=nombre_var)
            entry_nombre.pack(pady=5)

            ttk.Label(
                ventana_edit,
                text="Precio:",
                style="Premium.TLabel"
            ).pack(pady=5)
            precio_var = tk.StringVar(value=str(self.categorias[categoria][producto_actual]))
            entry_precio = ttk.Entry(ventana_edit, textvariable=precio_var)
            entry_precio.pack(pady=5)

            def guardar_cambios():
                try:
                    nuevo_precio = int(precio_var.get())
                    nuevo_nombre = nombre_var.get()

                    if nuevo_nombre != producto_actual:
                        del self.categorias[categoria][producto_actual]
                    self.categorias[categoria][nuevo_nombre] = nuevo_precio
                    
                    self.guardar_productos()
                    actualizar_lista_productos()
                    self.crear_panel_productos(self.inner_frame)
                    ventana_edit.destroy()
                    messagebox.showinfo("Éxito", "Producto modificado correctamente")
                except ValueError:
                    messagebox.showerror("Error", "El precio debe ser un número válido")

            ttk.Button(
                ventana_edit,
                text="Guardar",
                command=guardar_cambios,
                style="Premium.TButton"
            ).pack(pady=10)

        def agregar_producto():
            categoria = categoria_var.get()

            # Ventana para agregar
            ventana_add = tk.Toplevel(ventana_mod)
            ventana_add.title("Agregar Producto")
            ventana_add.geometry("400x200")
            ventana_add.configure(bg=self.colors['background'])

            ttk.Label(
                ventana_add,
                text="Nombre del Producto:",
                style="Premium.TLabel"
            ).pack(pady=5)
            nombre_var = tk.StringVar()
            entry_nombre = ttk.Entry(ventana_add, textvariable=nombre_var)
            entry_nombre.pack(pady=5)

            ttk.Label(
                ventana_add,
                text="Precio:",
                style="Premium.TLabel"
            ).pack(pady=5)
            precio_var = tk.StringVar()
            entry_precio = ttk.Entry(ventana_add, textvariable=precio_var)
            entry_precio.pack(pady=5)

            def guardar_nuevo():
                try:
                    precio = int(precio_var.get())
                    nombre = nombre_var.get()

                    if nombre and precio > 0:
                        self.categorias[categoria][nombre] = precio
                        self.guardar_productos()
                        actualizar_lista_productos()
                        self.crear_panel_productos(self.inner_frame)
                        ventana_add.destroy()
                        messagebox.showinfo("Éxito", "Producto agregado correctamente")
                    else:
                        messagebox.showwarning("Aviso", "Por favor complete todos los campos")
                except ValueError:
                    messagebox.showerror("Error", "El precio debe ser un número válido")

            ttk.Button(
                ventana_add,
                text="Guardar",
                command=guardar_nuevo,
                style="Premium.TButton"
            ).pack(pady=10)

        def eliminar_producto():
            seleccion = lista_productos.curselection()
            if not seleccion:
                messagebox.showwarning("Aviso", "Por favor seleccione un producto")
                return

            if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este producto?"):
                producto = lista_productos.get(seleccion[0]).split(" - ")[0]
                categoria = categoria_var.get()
                del self.categorias[categoria][producto]
                self.guardar_productos()
                actualizar_lista_productos()
                self.crear_panel_productos(self.inner_frame)
                messagebox.showinfo("Éxito", "Producto eliminado correctamente")

        # Botones de acción
        ttk.Button(
            frame_botones,
            text="Modificar Seleccionado",
            command=modificar_producto,
            style="Premium.TButton"
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            frame_botones,
            text="Agregar Nuevo",
            command=agregar_producto,
            style="Premium.TButton"
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            frame_botones,
            text="Eliminar Seleccionado",
            command=eliminar_producto,
            style="Premium.TButton"
        ).pack(side=tk.LEFT, padx=5)

    def guardar_productos(self):
        try:
            with open('productos.json', 'w', encoding='utf-8') as f:
                json.dump(self.categorias, f, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar productos: {str(e)}")

    def cargar_productos(self):
        try:
            if os.path.exists('productos.json'):
                with open('productos.json', 'r', encoding='utf-8') as f:
                    self.categorias = json.load(f)
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar productos: {str(e)}")

    def initialize_data(self): #control de datos mesa 
        self.mesas = {i: {
            "estado": "libre",
            "pedidos": [],
            "total": 0.0,
            "hora_inicio": None
        } for i in range(1, 26)}
        self.mesa_actual = None

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
                "Whisky Media":200000
            },
            " 🍹 trago 🍹 ": {
                "Ron Caldas Trago": 5000,
                "Aguardiente Trago": 4000,
                "tequila": 8000,
                "Whisky trago":15000,
                "sangría copa ":15000,
                
            },
            "🍺 Cervezas🍺": {
                "aguila": 5000,
                "aguila lite ": 5000,
                "pilsen ": 5000,
                "poker": 5000,
                "Coronita": 6000,
                "Club Colombia": 6000,
            },
            " 🍺micheladas🎉 ": {
                "aguila michelada ": 6000,
                "aguila lite michelada ": 6000,
                "clup colombia michelada ": 7000,
                "poker michelada ": 6000,
                "pilsen michelada ": 6000,
                "Coronita michelada ": 7000,
                "gaseosa michelada ":5000,
            },
            
            "🥤 Bebidas🥤": {
                "Gatorade": 5000,
                "Electrolit": 13000,
                "Agua Botella Grande": 4000,
                "Agua Botella Personal": 3000,
                "tutti fruti": 3000,
                "té de limon ": 3000,
                "sprite ": 4000,
                "cuatro": 4000,
                "Coca-Cola": 4000,
                "soda":4000,
            },
            "🍸 Cocteles": {
                "Margarita": 16000,
                "Tequila Sunrise":16000,
            },
            "otros": {
                "Vino botella":50000,
                "chicles": 3000,
                "alka seltzer": 4000,
                "cigarillos ": 1000,

            
            },
            }
            self.guardar_productos()  # Guardar los productos por defecto
    
            
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
        self.mesa_actual = numero
        if self.mesas[numero]["estado"] == "libre":
            self.mesas[numero]["hora_inicio"] = datetime.now()
        self.actualizar_vista_mesa()

    def agregar_producto(self, producto, precio):
        if self.mesa_actual is None:
            messagebox.showwarning("Aviso", "Por favor seleccione una mesa primero")
            return

        self.mesas[self.mesa_actual]["pedidos"].append((producto, precio))
        self.mesas[self.mesa_actual]["total"] += precio
        self.mesas[self.mesa_actual]["estado"] = "ocupada"
        self.actualizar_vista_mesa()

    def eliminar_ultimo_pedido(self):
        if self.mesa_actual is None:
            messagebox.showwarning("Aviso", "Por favor seleccione una mesa primero")
            return

        mesa_data = self.mesas[self.mesa_actual]
        if mesa_data["pedidos"]:
            producto, precio = mesa_data["pedidos"].pop()
            mesa_data["total"] -= precio
            if not mesa_data["pedidos"]:
                mesa_data["estado"] = "libre"
                mesa_data["hora_inicio"] = None
            self.actualizar_vista_mesa()
        else:
            messagebox.showinfo("Información", "No hay pedidos para eliminar")
    
    def actualizar_vista_mesa(self):
        if self.mesa_actual is None:
            return

        mesa_data = self.mesas[self.mesa_actual]
        estado_texto = mesa_data['estado'].upper()
        color_estado = self.colors['success'] if estado_texto == "LIBRE" else self.colors['warning']

        tiempo_transcurrido = ""
        if mesa_data["hora_inicio"]:
            tiempo = datetime.now() - mesa_data["hora_inicio"]
            horas = tiempo.seconds // 3600
            minutos = (tiempo.seconds % 3600) // 60
            tiempo_transcurrido = f"\nTiempo: {horas}h {minutos}m"

        self.info_mesa.config(
            text=f"Mesa {self.mesa_actual} - {estado_texto}{tiempo_transcurrido}",
            fg=color_estado
        )

        self.lista_pedidos.delete(1.0, tk.END)
        for producto, precio in mesa_data["pedidos"]:
            self.lista_pedidos.insert(tk.END, f"➤ {producto}: ${precio:,}\n")

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
        if self.mesa_actual is None or not self.mesas[self.mesa_actual]["pedidos"]:
            messagebox.showwarning("Aviso", "No hay pedidos para pagar")
            return
            
        venta = {
            'fecha': datetime.now().strftime('%d/%m/%Y %H:%M'),
            'mesa': self.mesa_actual,
            'pedidos': self.mesas[self.mesa_actual]['pedidos'],
            'total': self.mesas[self.mesa_actual]['total'],
            'tiempo': str(datetime.now() - self.mesas[self.mesa_actual]['hora_inicio']) if self.mesas[self.mesa_actual]['hora_inicio'] else "N/A"
        }
    
if __name__ == "__main__": 
    root = tk.Tk()
    app = BarPremiumApp(root)
    root.mainloop()
    
    