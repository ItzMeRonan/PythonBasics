#Celsius to Fahrenheit

def CelToFar():

	celsius = input("Please enter the temperature in celsius : ")

	far = (float(celsius) * 1.8) + 32       # celsius may be input as a string so convert it to float

	print("The temperature in fahrenheit is : " + str(far))   # covert the float value to string to concatenate to the string

CelToFar()