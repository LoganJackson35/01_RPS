# Version 2 - error message included when calling function

#functions go here
def choice_checker(question):


    valid = False
    while not valid:

        # ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        if response == "r" or response == "rock":
            return response
        elif response == "p" or response == "paper":
            return response
        elif response == "s" or response == "scissors":
            return response

        # check for exit code...
        elif response == "xxx":
            return response
        else:
            print(error)

# Main routine goes here


# loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # ask user for choice and check its valid
    user_choice = choice_checker("Choose rock / paper / "
                                 "scissors (r/p/s): ",
                                 "Please choose fom rock / "
                                 "paper / scisssors "
                                 "(or xxx to quit) ")

    # print out choice for comparison purposes
    print("You chose {}".format(user_choice))
