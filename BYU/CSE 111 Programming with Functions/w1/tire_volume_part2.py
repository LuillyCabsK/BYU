import math
from datetime import datetime

def calculate_tire_volume(width, aspect_ratio, diameter):
    """
    Calculates the volume of space inside a tire.
    Args:
        width: Tire width in millimeters
        aspect_ratio: Aspect ratio of the tire
        diameter: Wheel diameter in inches
    Returns:
        Volume in liters rounded to 2 decimal places
    """
    volume = (math.pi * width**2 * aspect_ratio * 
             (width * aspect_ratio + 2540 * diameter)) / 10000000000
    return round(volume, 2)

def get_tire_dimensions():
    """
    Gets tire dimensions from user input with validation
    Returns:
        Tuple of (width, aspect_ratio, diameter)
    """
    while True:
        try:
            width = float(input("Enter the width of the tire in mm (ex 205): "))
            aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
            diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
            return width, aspect_ratio, diameter
        except ValueError:
            print("Please enter valid numbers. Try again.")

def save_to_file(width, aspect_ratio, diameter, volume):
    """
    Saves tire data to volumes.txt file
    Args:
        width: Tire width in mm
        aspect_ratio: Aspect ratio
        diameter: Wheel diameter in inches
        volume: Calculated tire volume
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    with open("volumes.txt", "a") as file:
        file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume}\n")

def offer_purchase_option(width, aspect_ratio, diameter):
    """
    Offers purchase option and saves phone number if requested
    """
    buy = input("\nWould you like to buy tires with these dimensions? (yes/no): ").lower()
    if buy == "yes":
        phone = input("Enter your phone number: ")
        with open("volumes.txt", "a") as file:
            file.write(f"Phone inquiry for {width}/{aspect_ratio}R{diameter}: {phone}\n")
        print("Thank you! A sales representative will contact you soon.")

def main():
    print("=== Tire Volume Calculator ===")
    
    # Get tire dimensions from user
    width, aspect_ratio, diameter = get_tire_dimensions()
    
    # Calculate and display volume
    volume = calculate_tire_volume(width, aspect_ratio, diameter)
    print(f"\nThe approximate volume is {volume} liters")
    
    # Save data to file
    save_to_file(width, aspect_ratio, diameter, volume)
    print("Data has been saved to volumes.txt")
    
    # Optional purchase offer
    offer_purchase_option(width, aspect_ratio, diameter)

if __name__ == "__main__":
    main()