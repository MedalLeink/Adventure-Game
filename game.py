"""
Program: Text-Based Adventure Game
Author: Madeleine Nkiru

Description: A text-based adventure game where the user is presented
    with a scenario with different options to choose from.
"""

# First question
question_one = input(
    "\nYou are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. "
    "Which one do you want to pick up? "
)

# Normalize the user input
choice_one = question_one.upper()

if choice_one == "MATCH":
    # Level 2
    question_two = input(
        "\nYou pick up the match and strike it, and for an instant, the forest around you is illuminated. "
        "You see a large grizzly bear, and then the match burns out. "
        "Do you want to RUN, HIDE behind a tree, or CLIMB a tree? "
    )
    choice_two = question_two.upper()

    if choice_two == "RUN":
        # Level 3
        question_three = input(
            "\nYou start running as fast as you can. Do you want to RUN toward the RIVER, or BACK to the CABIN? "
        )
        if question_three.upper() == "RIVER":
            print("\nYou made it to safety by the river. The bear doesn’t follow you!🥳")
        elif question_three.upper() == "CABIN":
            print("\nYou make it back to the cabin, but the bear is right behind you. It's not safe at all!👻")
        else:
            print("Invalid choice. Choose 'RIVER' or 'CABIN'.❌")

    elif choice_two == "HIDE":

        # Level 3
        question_three = input(
            "\nYou hide behind a tree. The bear is sniffing around. Do you want to STAY still, or THROW a rock? "
        )
        if question_three.upper() == "STAY":
            print("\nThe bear eventually loses interest and wanders away. You’re safe!😅")
        elif question_three.upper() == "THROW":
            print("\nThe bear hears the noise and charges at the rock. You barely escape!😨")
        else:
            print("Invalid choice. Choose 'STAY' or 'THROW'.❌")

    elif choice_two == "CLIMB":
        # Level 3
        question_three = input(
            "\nYou climb up a tree quickly. Do you want to WAIT quietly or SHOUT for help? "
        )
        if question_three.upper() == "WAIT":
            print("\nYou wait it out, and the bear eventually leaves. Smart move!✅")
        elif question_three.upper() == "SHOUT":
            print("\nYou shout loudly. Unfortunately, this attracts the bear's attention and that's not good at all!😔")
        else:
            print("Invalid choice. Choose 'WAIT' or 'SHOUT'.❌")

    else:
        print("Invalid choice. Kindly choose RUN, HIDE, or CLIMB.❌")

elif choice_one == "FLASHLIGHT":
    
    # Level 2
    question_two = input(
        "\nYou pick up the flashlight and turn it on. You see the pathway lit up in front of you, "
        "but you also hear something off to the side. "
        "Do you want to FOLLOW the path or LOOK in the trees? "
    )
    choice_two = question_two.upper()

    if choice_two == "FOLLOW":
        # Level 3
        question_three = input(
            "\nYou follow the path deeper into the forest. You come across an old BRIDGE, a CAVE, or a RIVER. "
            "Where do you want to go? "
        )
        if question_three.upper() == "BRIDGE":
            print("\nThe bridge is old and creaky, but you manage to cross safely.💃")
        elif question_three.upper() == "CAVE":
            print("\nYou enter the cave and disturb a colony of bats! You run out quickly.🏃‍♀️")
        elif question_three.upper() == "RIVER":
            print("\nYou reach the river, and the sound of the water makes you feel calm and safe.🥳")
        else:
            print("Invalid choice. Choose 'BRIDGE', 'CAVE', or 'RIVER'.❌")

    elif choice_two == "LOOK":
        # Level 3
        question_three = input(
            "\nYou shine your flashlight into the trees. You see glowing EYES, a FOX, or nothing but DARKNESS. "
            "Which do you investigate? "
        )
        if question_three.upper() == "EYES":
            print("\nYou walk closer and realize it’s just a harmless deer. What a relief!")
        elif question_three.upper() == "FOX":
            print("\nThe fox scurries away into the bushes. That was close!")
        elif question_three.upper() == "DARKNESS":
            print("\nYou step into the darkness and suddenly feel very lost...")
        else:
            print("Invalid choice. Choose 'EYES', 'FOX', or 'DARKNESS'.")

    else:
        print("Invalid choice. Kindly choose FOLLOW or LOOK.")

else:
    print("Wrong choice of response. Kindly choose 'MATCH' or 'FLASHLIGHT'.")
