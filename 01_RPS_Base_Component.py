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

def instructions():

    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


# Main routine goes here
played_before = yes_no("Have you played before? ")
print()
def statement_generator(statement, decoration):

   sides= decoration * 3

   statement = "{} {} {}".format(sides, statement, sides)
   top_bottom = decoration * len(statement)

   print(top_bottom)
   print(statement)
   print(top_bottom)

   return ""

if played_before == "no":
    instructions()
# lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# ask user if they have played before
# If 'yes', show instructions

# ask users for # of rounds then loop...
rounds_played = 0

# initialise lost / drawn counters
rounds_lost = 0
rounds_drawn = 0

# Quick Calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# Ask user for # of rounds. <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play loop
    if rounds != "" and rounds_played == rounds - 1:
        end_game = "yes"

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
    print()
    print("You chose {}".format(choose))
    print()
      # End game if exit code is typed
    if choose == "xxx":
        break
    else:
      rounds_played += 1


        
    # Get computer choice

    comp_choice = random.choice(rps_list[:-1])
    print("Comp Choice: ", comp_choice)
    
    # Compare choices
    if comp_choice == choose:
        result = "tie"
        feedback = "It's a tie"
        rounds_drawn += 1
    elif choose == "rock" and comp_choice == "scissors":
        result = "won"
        rounds_won += 1
    elif choose == "paper" and comp_choice == "rock":
        result = "won"
        rounds_won += 1
    elif choose == "scissors" and comp_choice == "paper":
        result = "won"
        rounds_won += 1
    else:
       result = "lost"
       rounds_lost += 1
       
    if result != "tie":
      feedback = "{} vs {}  - you {}".format(choose, comp_choice, result)

    print()
    print("Won: {}, lost: {}, drawn: {}".format(rounds_won, rounds_lost, rounds_drawn))

    # output results...
    print(feedback)


# end of game statements 
print()
print('***** End Game Summary *****')
print("Won: {} \t|\t Lost: {} \t|\t Draw:"
"{}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thank you for playing")