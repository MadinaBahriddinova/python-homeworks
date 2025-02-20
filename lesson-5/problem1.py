def convert_cel_to_far(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9/5 + 32

def convert_far_to_cel(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    # Convert Fahrenheit to Celsius
    fahrenheit = float(input("Enter a temperature in degrees F: "))
    celsius = convert_far_to_cel(fahrenheit)
    print(f"{fahrenheit} degrees F = {round(celsius, 2)} degrees C")

    # Convert Celsius to Fahrenheit
    celsius = float(input("\nEnter a temperature in degrees C: "))
    fahrenheit = convert_cel_to_far(celsius)
    print(f"{celsius} degrees C = {round(fahrenheit, 2)} degrees F")

if __name__ == "__main__":
    main()
