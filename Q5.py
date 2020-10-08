# Name : Ida Bagus Ryogassa Avatara
# ID   : 2440100323

def convert_temp():
    fahrenheit = int(input("Enter a temperature in Fahrenheit: "))
    print("The Temperature in Celsius: ", convert_celsius(fahrenheit))
    print("The Temperature in Fahrenheit: ", convert_kelvin(convert_celsius(fahrenheit)))


def convert_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin


convert_temp()
