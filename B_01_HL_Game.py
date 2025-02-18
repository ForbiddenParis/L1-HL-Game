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


def int_check(question):
    """Checks user enter an integer more than / equal to 1"""
    while True:
        error = "Please enter an integer more than than / equal to 1."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0

print("⬆️ Welcome to the Higher - Lower Game ⬇️")
print()

# Instructions
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

# Game loop starts here

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop ends here
while rounds_played < num_rounds:

    # rounds headings
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite Mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n 💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# Game history / statistics area
