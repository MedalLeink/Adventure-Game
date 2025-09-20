"""
Program: Text-Based Adventure Game
Author: Madeleine Nkiru

Description: A text-based adventure game where the user is presented
    with a scenario with different options to choose from.
"""


# option_one == question_one.upper():

# question_one.upper() == "MATCH"
question_one = input("\nYou are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? ")
option_one = question_one.upper()

if option_one == "MATCH":
    question_two = input('''\nYou pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? ''')
    
    option_two = question_two.upper()

    if option_two.upper() == "RUN":
        question_three = input(
            "\nYou start running as fast as you can. Do you want to RUN toward the RIVER, or BACK to the CABIN? ")
        
    if question_three.upper() == "RIVER":
        print("\nYou made it to safety by the river. The bear doesn't follow you!😊👏")
    elif question_three.upper() == "CABIN":
        print("\nYou made it back to the cabin, but the bear is right behind you! You aren't safe at all!😱")
    else:
        print("Invalid choice. Kindly choose between the words 'RIVER' OR 'CABIN'")

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