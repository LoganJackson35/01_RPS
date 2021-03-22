import random

# functions go here
def check_rounds():
    while True:
       response = input("How many rounds? ")

       round_error = "Please type either <enter> " \
                    "or an integer that is more than 0"
       if response != "":
           try:
              response = int(response)

              if response < 1:
                  print(round_error)
                  continue

           except ValueError:
              print(round_error)
              continue
  
       return response

def choice_checker(question, valid_list, error_txt):


    valid = False
    while not valid:

        # ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through lsit and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
          if response == item[0] or response == item:
              return item

        # output error if item not in list
        print(error_txt)
        print()

# Main routine goes here

# lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# ask user if they have played before
# If 'yes', show instructions

# ask users for # of rounds then loop...
rounds_played = 0
choose_instruction = "please choose rock (r), paper " \
                     "(p) or scissors (s)"

# Ask user for # of rounds. <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play loop

    # Rounds heading
    print()
    if rounds == "":
        heading = "Continuous Mode: " \
                  "Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of " \
                  "{}".format(rounds_played + 1, rounds)

    print(heading)
    print()
    choose_instruction = "Please choose rock (r), paper " \
                         "(p) or scissors (s)" \
                         "or 'xxx to exit: "

    choose_error = "Please choose from rock / " \
                   "paper / scissors ( or xxx to quit)"
  
    # ask user for choice and check its valid
    choose = choice_checker(choose_instruction, rps_list,
                            choose_error)
    
    # Get computer choice

    #Compare choices


    # End game if exit code is typed
    if choose == "xxx":
        break

    # **** rest if loop / game ****
    elif rounds != "" and rounds_played == rounds - 1:
            end_game = "yes"


    # rest of loop / game
    print()
    print("You chose {}".format(choose))
    print()
    rounds_played += 1

print("Thank you for playing")
                