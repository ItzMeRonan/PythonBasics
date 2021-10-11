#--- My Text-Based Adventure Game ---

print("Welcome to my text-based adventure game")

playerName = input("Please enter your name : ")
print("Hello " + playerName)

print("Pick any of the following characters: ", "1. Tony ", "2. Thor ", "3. Hulk", sep='\n')

characterList = ["Tony", "Thor", "Hulk"]
characterNumber = input("Enter the character's number : ")

print("You chose: " + characterList[int(characterNumber) -1])