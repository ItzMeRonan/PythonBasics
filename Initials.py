# Write a new program that asks the user for their first name and then their surname. The program should then display the person’s initials.

def initials():
	firstName = input("Please enter your first name : ")
	lastName = input("Please enter your surname : ")

	initials = firstName[0] + lastName[0]

	print("Your initials are : " + initials)

initials()