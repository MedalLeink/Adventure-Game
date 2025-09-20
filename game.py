"""
Program: Text-Based Adventure Game
Author: Madeleine Nkiru

Description: A text-based adventure game where the user is presented
    with a scenario with different options to choose from.
"""



question_one = input('''\nYou are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? ''')
if question_one == "MATCH":
    question_two = input('''\nYou pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? ''')
    if question_two == "RUN":
        print("You may have made the very right choice for safety😊")
    elif question_two == "HIDE":
        print("You made the right choice for your safety but make sure to find a suitable place of safety")
    else:
        print("Kindly choose between the words 'RUN' OR 'HIDE'")

elif question_one == "FLASHLIGHT":
    next_question = input('''\nYou pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ''')
    if next_question == "FOLLOW":
        print("\nYou'll sure find the thing you're looking for!🤣")
    elif next_question == "LOOK":
        print("I advise you find a suitable place to hide for your safety!👻")
    else:
        print("Kindly choose between the words 'FOLLOW' OR 'LOOK'")
else: 
    print("Wrong choice of response. Kindly choose between the words 'MATCH' OR 'FLASHLIGHT'")