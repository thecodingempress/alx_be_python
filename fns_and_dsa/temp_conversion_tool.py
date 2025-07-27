
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


userinput = input("Enter the temperature to convert:").strip()
degree = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()

if degree == 'C':
    celcius = float(userinput)
    fahrenheit = convert_to_fahrenheit(celcius)
    print(f"{celcius}°C is {fahrenheit:}°F")
elif degree == 'F':
    fahrenheit = float(userinput)
    celsius = convert_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is {celsius:}°C")