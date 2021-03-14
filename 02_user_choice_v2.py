# Version 2 - error message included when calling function

#functions go here
def choice_checker(question, error_txt):


    valid = False
    while not valid:

        # ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        if response == "r" or response == "rock":
            return "rock"
        elif response == "p" or response == "paper":
            return "paper"
        elif response == "s" or response == "scissors":
            return "scissors"

        # check for exit code...
        elif response == "xxx":
            return response
        else:
            print(error_txt)

# Main routine goes here


# loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # ask user for choice and check its valid
    user_choice = choice_checker("Choose rock / paper / "
                                 "scissors (r/p/s): ",
                                 "Please choose from rock / paper / scisssors "
                                 "(or xxx to quit) ")

    # print out choice for comparison purposes
    print("You chose {}".format(user_choice))
