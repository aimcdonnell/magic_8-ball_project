# Import this module so we can use its functions. Add this line of code to the top of magic8.py:
import random

# Declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball.
name = ""
# print(name)

# Next, declare a variable question, and assign it to a “Yes” or “No” question you’d like to ask the Magic 8-Ball.
question = "Will I win the lottery?"

# We want to store the answer of the Magic 8-Ball in another variable, which we’ll call answer. For now, assign this variable to an empty string.
answer = ""

# Declare a variable called random_number, and assign it to the random.randint(1, 11) function call which will generate a random number between 1 (inclusive) and 9 (inclusive).


# Add a print() statement that outputs the value of random_number, and run the program several times to ensure random values are being generated as expected.
random_number = random.randint(1, 11)

# Once you’re sure this is working as we expected, feel free to comment out this print() statement.
# print(random_number)

# Write an if statement where if the random_number is equal to 1, answer is assigned to the phrase “Yes - definitely”
if random_number == 1: 
  answer = "Yes - definitely"

# Write an elif statement after the if statement where if the random_number is equal to 2, answer is assigned to the phrase “It is decidedly so”.
# Continue writing elif statements for each of the remaining phrases for the values 3 to 9.
#The 9 possible answers of the Magic 8-Ball are:
# 1. Yes - definitely, 2. It is decidedly so, 3. Without a doubt, 4. Reply hazy, try again, 5. Ask again later, 6. Better not tell you now 7. My sources say no 8. Outlook not so good, 9. Very doubtful
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
# Optional tasks: add a few more possible answers to the program
elif random_number == 10:
  answer = "Highly unlikely"
elif random_number == 11:
  answer = "Absolutely not"
#If there is an error with the program, print out the following message:
else:
  answer = "Error! Try again"
  
# Optional task: Amend the code to be an if/else statement
# If the user does not provide a name, output just the user's question instead
if name == "":
  print("Question: " + question)
# Otherwise, write a print() statement to output the asker’s name and their question
else:
  print(name + " asks: " + question)

# Optional task: Amend code to be an if/else statement
# If no question is provided, print out a message
if question == "":
  print("The Magic 8-Ball isn't a mind reader! Add a question")
# Otherwise, if a question is provided, print the Magic 8-Ball's answer
else:
  print("Magic 8-Ball's answer: " + answer)