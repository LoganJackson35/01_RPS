# RPS Component 3 - Compare user choice and computer choice\
rps_list = ["rock", "paper", "scissors"]
comp_index = 0 
for item in rps_list:
    user_index = 0
    for item in rps_list:
      user_choice = rps_list[user_index]
      comp_choice = rps_list[comp_index]
      user_index += 1

    
    # Compare choices
    if comp_choice == user_choice:
        result = "tie"
        feedback = "It's a tie"
        rounds_drawn += 1
    elif user_choice == "rock" and comp_choice == "scissors":
        result = "won"
        rounds_won += 1
    elif user_choice == "paper" and comp_choice == "rock":
        result = "won"
        rounds_won += 1
    elif user_choice == "scissors" and comp_choice == "paper":
        result = "won"
        rounds_won += 1
    else:
       result = "lost"
       rounds_lost += 1
       
    if result != "tie":
      feedback = "{} vs {}  - you {}".format(user_choice, comp_choice, result)

    print()
    print("Won: {}, lost: {}, drawn: {}".format(rounds_won, rounds_lost, rounds_drawn))

comp_index += 1
print()