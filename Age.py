# Write a new program that asks the user for their age, the program should output false if the person is less than 18 years old and true if the person is greater than 17 years old (do not use a conditional if statement)

def AgeCondition():
	age = input("Please enter your age : ")

	print(bool(int(age) > 17))

AgeCondition()