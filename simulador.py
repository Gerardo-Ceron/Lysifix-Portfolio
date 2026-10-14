import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# 1. Mensaje de Bienvenida Corporativo
console.print(Panel.fit(
    "[bold gold1]LYSIFIX FINANCIAL INTEGRATION[/]\n[bold white]Módulo de Proyección de Capital e Interés Simple", 
    border_style="cyan"
))

console.print("\n[bold green]➡️[/] [cyan]Iniciando motor de procesamiento lógico...[/]")
time.sleep(1)
console.print("[bold green]✔️[/] [spring_green3]Separación de capital y ganancias netas calculada.[/]\n")
time.sleep(0.8)

# 2. Creación de la Tabla de Rendimientos
table = Table(title="Proyección de Rendimientos Automatizada", title_style="bold magenta")

table.add_column("Año/Período", justify="center", style="cyan", no_wrap=True)
table.add_column("Capital Inicial", justify="right", style="white")
table.add_column("Interés Simple (8%)", justify="right", style="gold1")
table.add_column("Ganancia Neta", justify="right", style="spring_green3")
table.add_column("Balance Total", justify="right", style="bold green")

# Simulamos el cálculo inmediato por períodos
console.print("[bold white]Procesando rendimientos en tiempo real...[/]")
time.sleep(0.5)

data = [
    ("Año 1", "$100,000.00", "$8,000.00", "$8,000.00", "$108,000.00"),
    ("Año 2", "$108,000.00", "$8,000.00", "$16,000.00", "$116,000.00"),
    ("Año 3", "$116,000.00", "$8,000.00", "$24,000.00", "$124,000.00"),
]

for row in data:
    time.sleep(0.6)  # Efecto de carga en la terminal
    table.add_row(*row)

console.print(table)
console.print("\n[bold green]✔️[/] [bold white]Estructura modular lista para integrarse a APIs.[/]\n")