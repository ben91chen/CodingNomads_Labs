'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''


degrees_fahrenheit = float((input("Say a temperature in Fahrenheit and this program will convert it to Celcius: ")))
degrees_celcius = int(((degrees_fahrenheit - 32) * (5/9)))

print(f"{degrees_fahrenheit} degrees fahrenheit = {degrees_celcius} degrees celsius")

