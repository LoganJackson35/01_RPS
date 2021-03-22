# Version 3 - checks that response is in a given list

#functions go here
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


# lists for checking purposes
rps_list = ["rock", "paper", "scissors", "xxx"]

# loop for testing purposes
choose = ""
while choose != "xxx":

    # ask user for choice and check its valid
    choose = choice_checker("Choose from rock / paper / scissors (r/p/s) ",
    rps_list, "Please choose from rock / paper / scissors (or xxx to  quit) ") 

    # print out choice for comparison purposes
    print("You chose {}".format(choose))
