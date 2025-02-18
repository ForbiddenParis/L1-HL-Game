# functions go here
def yes_no(question):
    """Checks user response to a question is yes / no (y/n). returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check if the user says yes/no/y/n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes/no")


def instructions():
    """Print instructions"""

    print("""
*** Instructions ***

To begin, choose the number of rounds and either customise
the game parameters or go with the default game (where the
secret number with be between 1 and 100).

Then choose how many rounds you'd like to play <enter> for 
infinite mode.

Your goal is to try to guess the secret number without running out of guesses.

Good luck.

    """)


# Main routine
print()
print("⬆️ Welcome to the Higher - Lower Game ⬇️")
print()

# loop for testing purposes.
# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
print("Program continues")
