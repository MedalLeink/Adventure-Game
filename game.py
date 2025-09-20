"""
Program: Text-Based Adventure Game
Author: Madeleine Nkiru

Description: A text-based adventure game where the user is presented
    with a scenario with different options to choose from.
"""


# item_A = MATCH
# item_B = FLASHLIGHT

question_one = input('''\nYou are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? ''')
if question_one == "MATCH":
    question_two = input('''\nYou pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? ''')
    if "RUN":
        print("You may have made the very right choice for safety😊")
    elif "HIDE":
        print("You made the right choice for your safety but make sure to find a suitable place of safety")
else: 
    print("Wrong choice of response")