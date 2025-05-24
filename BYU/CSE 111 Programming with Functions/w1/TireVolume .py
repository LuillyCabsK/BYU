import math
from datetime import datetime
import os
import platform

def get_tire():
    # Obtiene las dimensiones del neumático del usuario con validación
    while True:
        try:
            width = float(input("Enter the tire width in millimeters (e.g., 205): "))
            aspect_ratio = float(input("Enter the aspect ratio (e.g., 60): "))
            diameter = float(input("Enter the wheel diameter in inches (e.g., 15): "))
            return width, aspect_ratio, diameter
        except ValueError:
            print("Error: Please enter valid numbers for all dimensions.")

def calculate_volume(width, aspect_ratio, diameter):
    """Calcula el volumen interior del neumático en litros"""
    part1 = math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)
    vol_tire = part1 / 10000000000
    return round(vol_tire, 2)  # Redondeamos a 2 decimales

def save_to_file(width, aspect_ratio, diameter, volume):
    """Guarda los datos en el archivo volumes.txt"""
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    with open("volumes.txt", "a") as file:
        file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}\n")
    return "volumes.txt"  # Retornamos el nombre del archivo

def offer_option(width, aspect_ratio, diameter):
    """Ofrece al usuario la opción de comprar neumáticos"""
    buy = input("\nWould you like to buy tires with these dimensions? (yes/no): ").lower()
    if buy == "yes":
        phone = input("Enter your phone number: ")
        with open("volumes.txt", "a") as file:
            file.write(f"Phone inquiry for {width}/{aspect_ratio}R{diameter}: {phone}\n")
        print("Thank you! A sales representative will contact you soon.")

def open_file(filename):
    """Abre el archivo con el programa predeterminado según el sistema operativo"""
    try:
        if platform.system() == "Windows":
            os.startfile(filename)
        elif platform.system() == "Darwin":  # macOS
            os.system(f"open {filename}")
        else:  # Linux y otros
            os.system(f"xdg-open {filename}")
    except Exception as e:
        print(f"Could not open file automatically: {e}")
        print(f"You can manually open the file at: {os.path.abspath(filename)}")

def main():
    """Función principal que orquesta todo el programa"""
    # Información y instrucciones
    print("\n\tTIRE VOLUME CALCULATOR")
    print("The tire size is represented with three numbers like: 205/60R15")
    print("Where:")
    print("- First number: width in millimeters (e.g., 205)")
    print("- Second number: aspect ratio (e.g., 60)")
    print("- Third number: wheel diameter in inches (e.g., 15)\n")
    
    # Obtener datos del usuario
    width, aspect_ratio, diameter = get_tire()
    
    # Calcular volumen
    vol_tire = calculate_volume(width, aspect_ratio, diameter)
    print(f"\nThe approximate volume is: {vol_tire:.2f} liters")
    
    # Guardar datos
    filename = save_to_file(width, aspect_ratio, diameter, vol_tire)
    print(f"Data saved to {filename}")
    
    # Oferta de compra
    offer_option(width, aspect_ratio, diameter)
    
    # Opción de abrir archivo
    open_choice = input("\nWould you like to open the data file now? (yes/no): ").lower()
    if open_choice == "yes":
        open_file(filename)
    else:
        print(f"File location: {os.path.abspath(filename)}")

if __name__ == "__main__":
    main()