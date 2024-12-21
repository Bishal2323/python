print(" It's the 1st code that i will upload to git hub :")

# So I am just cooking something 
# Let's make a webpage or  a game choosing a randon number and a qoute pop out

quotes = {
  "1": "The only limit to our realization of tomorrow is our doubts of today.",
  "2": "Success is not final, failure is not fatal: It is the courage to continue that counts.",
  "3": "In the middle of every difficulty lies opportunity."
}
random_number=input("Enter a number(1-3) and I will give you a random quote:")
if random_number in quotes:
    print(quotes[random_number])
else:
    print("\n")
    print("You didn't enter the number between 1-3");
