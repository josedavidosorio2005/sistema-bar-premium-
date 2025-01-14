import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import locale
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os
from pathlib import Path

class BarPremiumApp:
    def __init__(self, root):
        self.root = root
        self.root.title("★ Vieja Guardia - Sistema Premium de Bar ★")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 700)

        # Colores personalizados
        self.colors = {
            'background': '#1a1a2e',
            'accent': '#e94560',
            'text': '#ffffff',
            'button': '#0f3460',
            'button_hover': '#16498c',
            'highlight': '#ff4d4d',
            'success': '#2ecc71',
            'warning': '#f39c12',
            'panel': '#212142'
        }

        # Configurar el tema general
        self.root.configure(bg=self.colors['background'])

        # Configuración regional
        self.configure_locale()

        # Inicialización de datos
        self.initialize_data()

        # Configurar estilos y crear interfaz
        self.configurar_estilos()
        self.crear_interfaz_premium()

    def configure_locale(self):
        locales_to_try = ['es_CO.UTF-8', 'es_CO', 'es-CO', '']
        for loc in locales_to_try:
            try:
                locale.setlocale(locale.LC_ALL, loc)
                break
            except locale.Error:
                continue

    def initialize_data(self):
        self.mesas = {i: {
            "estado": "libre",
            "pedidos": [],
            "total": 0.0,
            "hora_inicio": None
        } for i in range(1, 16)}
        self.mesa_actual = None

        # Categorías y productos
        self.categorias = {
            "🥃 Aguardiente": {
                "Aguardiente Litro Azul": 100000,
                "Aguardiente Verde/Rojo Litro": 98000,
                "Aguardiente Media Azul": 50000,
                "Aguardiente Verde/Rojo Media": 48000,
                "Aguardiente Trago": 5000,
            },
            "🥃 Ron": {
                "Ron Caldas Litro": 130000,
                "Ron Caldas Media": 56000,
                "Ron Caldas Trago": 5000,
                "Ron Medellín Litro": 120000,
                "Ron Medellín Media": 52000,
            },
            "🍺 Cervezas": {
                "Cerveza Nacional": 5000,
                "Cerveza Premium": 7000,
                "Cerveza Michelada": 6000,
                "Coronita": 6000,
                "Club Colombia": 6000,
            },
            "🥤 Bebidas": {
                "Gaseosa": 4000,
                "Gaseosa Michelada": 5000,
                "Gatorade": 5000,
                "Electrolit": 13000,
                "Agua Botella Grande": 4000,
                "Agua Botella Personal": 3000,
            },
            "🍸 Cocteles": {
                "Margarita": 16000,
                "Mojito": 16000,
                "Cuba Libre": 14000,
                "Gin Tonic": 18000,
                "Piña Colada": 16000,
            }
        }

    def configurar_estilos(self):
        style = ttk.Style()
        style.theme_use('clam')

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
            font=('Helvetica', 12, 'bold'),
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
            text="💰 Cuenta Actual",
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
            text="💳 Pagar y Dar Recibo",
            font=('Helvetica', 12, 'bold'),
            bg=self.colors['success'],
            fg=self.colors['text'],
            activebackground=self.colors['highlight'],
            activeforeground=self.colors['text'],
            relief="raised",
            bd=3,
            command=self.pagar_y_dar_recibo
        ).pack(pady=5, fill=tk.X)

        tk.Button(
            parent,
            text="❌ Eliminar Último Pedido",
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

    def pagar_y_dar_recibo(self):
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

        # Guardar historial y generar recibo
        self.guardar_historial(venta)
        self.imprimir_recibo(venta)

        # Resetear mesa
        self.mesas[self.mesa_actual] = {
            "estado": "libre",
            "pedidos": [],
            "total": 0.0,
            "hora_inicio": None
        }
        self.actualizar_vista_mesa()
        messagebox.showinfo("Éxito", "Pago procesado correctamente")

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

    def guardar_historial(self, venta):
        try:
            # Guardar en formato texto
            with open("historial_ventas.txt", "a", encoding='utf-8') as f:
                f.write("=" * 50 + "\n")
                f.write(f"Fecha: {venta['fecha']}\n")
                f.write(f"Mesa: {venta['mesa']}\n")
                f.write(f"Tiempo total: {venta['tiempo']}\n")
                f.write("Pedidos:\n")
                for producto, precio in venta['pedidos']:
                    f.write(f"  - {producto}: ${precio:,}\n")
                f.write(f"Total: ${venta['total']:,}\n")
                f.write("=" * 50 + "\n\n")

            # Guardar en formato JSON
            try:
                historial = []
                if os.path.exists("historial_ventas.json"):
                    with open("historial_ventas.json", "r") as f:
                        historial = json.load(f)
                historial.append(venta)
                with open("historial_ventas.json", "w") as f:
                    json.dump(historial, f, indent=4)
            except Exception as e:
                print(f"Error al guardar JSON: {e}")

        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar historial: {str(e)}")

    def apagar_aplicacion(self):
        if messagebox.askokcancel("Salir", "¿Desea cerrar la aplicación?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BarPremiumApp(root)
    root.mainloop()
