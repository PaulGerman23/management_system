import customtkinter as ctk

class Dashboard(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        

        # -------- Summary Cards --------
        summary_frame = ctk.CTkFrame(self)
        summary_frame.pack(fill="x", pady=(0,20))

        cards = [
            ("Productos en stock", "145 ítems disponibles"),
            ("Ventas del día", "$32.000 hoy"),
            ("Ventas semana", "$210.000 esta semana"),
            ("Compras recientes", "5 órdenes de proveedores"),
            ("Servicios en taller", "3 en curso / 12 completados"),
            ("Empleados activos", "4 empleados"),
        ]
        for i, (title, value) in enumerate(cards):
            card = ctk.CTkFrame(summary_frame, width=200, height=90, corner_radius=15)
            card.grid(row=0, column=i, padx=15, pady=15)
            ctk.CTkLabel(card, text=title, font=ctk.CTkFont(size=12, weight="bold")).pack(anchor="w", padx=20, pady=(20,0))
            ctk.CTkLabel(card, text=value, font=ctk.CTkFont(size=16)).pack(anchor="w", padx=20, pady=(0,20))

        # -------- Access Buttons & Chart Panel --------
        middle_frame = ctk.CTkFrame(self)
        middle_frame.pack(fill="x", pady=(0, 20))

       

        # Chart Panel
        chart_panel = ctk.CTkFrame(middle_frame, height=200)
        chart_panel.pack(side="left", fill="both", expand=True)
        ctk.CTkLabel(chart_panel, text="Panel de Gráficos", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=10)
        # Aquí puedes integrar un gráfico con matplotlib o similar

        # -------- Last Sales / Services List --------
        bottom_frame = ctk.CTkFrame(self)
        bottom_frame.pack(fill="both", expand=True)

        ctk.CTkLabel(bottom_frame, text="Últimas ventas registradas", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=10, pady=(10,0))
        ventas_list = ctk.CTkTextbox(bottom_frame, height=80)
        ventas_list.pack(fill="x", padx=10, pady=5)
        ventas_list.insert("end", "Venta #1: $5.000 - 30/05/2025\nVenta #2: $12.000 - 30/05/2025\n...")

        ctk.CTkLabel(bottom_frame, text="Últimas compras a proveedores", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=10, pady=(10,0))
        compras_list = ctk.CTkTextbox(bottom_frame, height=60)
        compras_list.pack(fill="x", padx=10, pady=5)
        compras_list.insert("end", "Compra #1: $8.000 - 29/05/2025\nCompra #2: $15.000 - 28/05/2025\n...")

        ctk.CTkLabel(bottom_frame, text="Últimos servicios realizados en el taller", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=10, pady=(10,0))
        servicios_list = ctk.CTkTextbox(bottom_frame, height=60)
        servicios_list.pack(fill="x", padx=10, pady=5)
        servicios_list.insert("end", "Servicio #1: Cambio de aceite - 30/05/2025\nServicio #2: Reparación frenos - 29/05/2025\n...")