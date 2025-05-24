import math

# Función para calcular el volumen de una lata
def compute_volume(radius, height):
    return math.pi * (radius ** 2) * height

# Función para calcular el área superficial de una lata
def compute_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

# Función para calcular la eficiencia de almacenamiento
def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    return volume / surface_area

# Función para calcular la eficiencia de costo
def compute_cost_efficiency(radius, height, cost):
    volume = compute_volume(radius, height)
    return volume / cost

# Datos de las latas
can_sizes = [
    {"name": "#1 Picnic", "radius": 6.83, "height": 10.16, "cost": 0.28},
    {"name": "#1 Tall", "radius": 7.78, "height": 11.91, "cost": 0.43},
    {"name": "#2", "radius": 8.73, "height": 11.59, "cost": 0.45},
    {"name": "#2.5", "radius": 10.32, "height": 11.91, "cost": 0.61},
    {"name": "#3 Cylinder", "radius": 10.79, "height": 17.78, "cost": 0.86},
    {"name": "#5", "radius": 13.02, "height": 14.29, "cost": 0.83},
    {"name": "#6Z", "radius": 5.40, "height": 8.89, "cost": 0.22},
    {"name": "#8Z short", "radius": 6.83, "height": 7.62, "cost": 0.26},
    {"name": "#10", "radius": 15.72, "height": 17.78, "cost": 1.53},
    {"name": "#211", "radius": 6.83, "height": 12.38, "cost": 0.34},
    {"name": "#300", "radius": 7.62, "height": 11.27, "cost": 0.38},
    {"name": "#303", "radius": 8.10, "height": 11.11, "cost": 0.42}
]

# Función para mostrar todos los datos
def display_all_data():
    print("\nDatos de todas las latas:")
    print(f"{'Nombre':<12} {'Radio':>6} {'Altura':>6} {'Costo':>6} {'Efic. Almac.':>12} {'Efic. Costo':>12}")
    print("-" * 60)
    
    for can in can_sizes:
        storage_eff = compute_storage_efficiency(can["radius"], can["height"])
        cost_eff = compute_cost_efficiency(can["radius"], can["height"], can["cost"])
        print(f"{can['name']:<12} {can['radius']:>6.2f} {can['height']:>6.2f} {can['cost']:>6.2f} {storage_eff:>12.2f} {cost_eff:>12.2f}")

# Función para encontrar la lata con mejor eficiencia de almacenamiento
def find_best_storage():
    best_storage = None
    max_efficiency = 0
    
    for can in can_sizes:
        efficiency = compute_storage_efficiency(can["radius"], can["height"])
        if efficiency > max_efficiency:
            max_efficiency = efficiency
            best_storage = can
    
    print(f"\nLa lata con mejor eficiencia de almacenamiento es: {best_storage['name']}")
    print(f"Eficiencia: {max_efficiency:.2f}")
    print(f"Radio: {best_storage['radius']} cm, Altura: {best_storage['height']} cm")

# Función para encontrar la lata con mejor eficiencia de costo
def find_best_cost():
    best_cost = None
    max_efficiency = 0
    
    for can in can_sizes:
        efficiency = compute_cost_efficiency(can["radius"], can["height"], can["cost"])
        if efficiency > max_efficiency:
            max_efficiency = efficiency
            best_cost = can
    
    print(f"\nLa lata con mejor eficiencia de costo es: {best_cost['name']}")
    print(f"Eficiencia: {max_efficiency:.2f}")
    print(f"Costo: ${best_cost['cost']:.2f}, Radio: {best_cost['radius']} cm, Altura: {best_cost['height']} cm")

# Menú principal
def main_menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Mostrar todos los datos de las latas")
        print("2. Encontrar la lata con mejor eficiencia de almacenamiento")
        print("3. Encontrar la lata con mejor eficiencia de costo")
        print("4. Salir")
        
        choice = input("Seleccione una opción (1-4): ")
        
        if choice == "1":
            display_all_data()
        elif choice == "2":
            find_best_storage()
        elif choice == "3":
            find_best_cost()
        elif choice == "4":
            print("¡Gracias por usar el programa!")
            break
        else:
            print("Opción no válida. Por favor seleccione 1-4.")

# Ejecutar el programa
if __name__ == "__main__":
    print("Bienvenido al programa de análisis de eficiencia de latas")
    main_menu()