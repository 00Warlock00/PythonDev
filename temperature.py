"Create a temperature.py program that converts a number from Fahrenheit (°F) to Celsius (°C)."
# Write your code here

class Convertion:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    def fahrenheit_to_celsius(self):
        celsius = (self.fahrenheit - 32) / 1.8
        return celsius

# Test the Convertion class
fahrenheit = 100
convertion = Convertion(fahrenheit)
print(f"{fahrenheit}°F is equal to {convertion.fahrenheit_to_celsius()}°C")