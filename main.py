#Importar base de datos / import database
from database.db_manager import init_db
init_db()
#Importar custom tinter / import ctk
import customtkinter as ctk
#Importar este archivo como inicio / import this file as home
from ui.dashboard import Dashboard
#Importar manejo de imagen
from PIL import Image
#Cambiar iconos y convertirlos a color / change icons and convert color
def icono_blanco(ruta):
    img = Image.open(ruta).convert("RGBA")
    datas = img.getdata()
    nueva_data = []
    for item in datas:
        # Cambia cualquier píxel no transparente a blanco, manteniendo el canal alfa
        nueva_data.append((255, 255, 255, item[3]))
    img.putdata(nueva_data)
    return img

# Cargar íconos como blancos / Charge white icons
home_icon = ctk.CTkImage(light_image=icono_blanco("assets/icons/home.png"), size=(24, 24))
inventory_icon = ctk.CTkImage(light_image=icono_blanco("assets/icons/inventory.png"), size=(24, 24))
purchases_icon = ctk.CTkImage(light_image=icono_blanco("assets/icons/purchases.png"), size=(24, 24))
sales_icon = ctk.CTkImage(light_image=icono_blanco("assets/icons/sales.png"), size=(24, 24))
workshop_icon = ctk.CTkImage(light_image=icono_blanco("assets/icons/workshop.png"), size=(24, 24))
employees_icon = ctk.CTkImage(light_image=icono_blanco("assets/icons/employees.png"), size=(24, 24))

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
#Configuraciones de la UI / Config UI
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión - Repuestos de Motos")
        # Forzar tamaño pantalla si zoomed no funciona
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")
        self.resizable(True, True)

        self.sidebar = ctk.CTkFrame(self, width=200)
        self.sidebar.pack(side="left", fill="y")

        self.content = ctk.CTkFrame(self)
        self.content.pack(side="right", fill="both", expand=True)

        self.init_sidebar()
        self.show_dashboard()

    def init_sidebar(self):
        ctk.CTkLabel(self.sidebar, text="Menú", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=20)

        buttons = [
            ("Inicio", home_icon, self.show_dashboard),
            ("Inventario", inventory_icon, self.show_inventory),
            ("Compras", purchases_icon, self.show_purchases),
            ("Ventas", sales_icon, self.show_sales),
            ("Taller", workshop_icon, self.show_workshop),
            ("Empleados", employees_icon, self.show_employees),
        ]
        for text, icon, command in buttons:
            ctk.CTkButton(
                self.sidebar,
                text=text,
                image=icon,
                compound="left",  # icono a la izquierda
                anchor="w",       # alinear contenido a la izquierda
                command=command,
                fg_color="transparent",
                hover_color="#151515"
            ).pack(fill="x", padx=10, pady=5)

#Cambio de vista de menú /  change menu       
    def show_dashboard(self):
        self._clear_content()
        Dashboard(self.content).pack(fill="both", expand=True)

    def show_inventory(self):
        from ui.inventory import InventoryView
        self._clear_content()
        InventoryView(self.content).pack(fill="both", expand=True)

    def show_purchases(self):
        from ui.purchases import PurchasesView
        self._clear_content()
        PurchasesView(self.content).pack(fill="both", expand=True)

    def show_sales(self):
        from ui.workshop import SalesView
        self._clear_content()
        SalesView(self.content).pack(fill="both", expand=True)

    def show_workshop(self):
        from ui.workshop import WorkshopView
        self._clear_content()
        WorkshopView(self.content).pack(fill="both", expand=True)

    def show_employees(self):
        from ui.employees import EmployeesView
        self._clear_content()
        EmployeesView(self.content).pack(fill="both", expand=True)

    def _clear_content(self):
            for widget in self.content.winfo_children():
                widget.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
