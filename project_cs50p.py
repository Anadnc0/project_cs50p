import sys
import webbrowser
import time
import os

def main():
    display_intro()
    player_inventory = []

    while True:
        choice = get_player_choice()
        process_choice(choice, player_inventory)
        if choice == 'quit':
            print("Well, maybe goodluck next time!")
            break

def display_intro():
    ##Introduction.##
    print("It's prom night! You're feeling a little nervous, specially because you're going solo, but your family insists you to go.")
    print("As you enter the school gym, you see a DJ spinning tunes and a sea of faces. Suddenly...")
    print("You bump into someone! It's...")
    print("1. The popular football captain, who gives you a charming smile.")
    print("2. The quiet guy from your English class, who looks a little shy.")
    print("3. The funny guy from your history class, who's cracking jokes.")
    print("4. Quit")

def get_player_choice():
    ##Gets the player's choice.##
    while True:
        try:
            choice = input("Who do you talk to first? Enter your choice (1-4 or 'quit'): ")
            if choice in ['1', '2', '3', '4', 'quit']:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, or 'quit'.")
        except ValueError:
            print("Invalid input. Please enter a number or 'quit'.")

def process_choice(choice, player_inventory):
    ##Handles the consequences of the player's choice.##
    if choice == '1':
        print("The football captain is confident and charming. He asks you to dance. ")
        dance_choice = input("Do you dance with him? (yes/no): ").lower()
        if dance_choice == 'yes':
            print("You enjoy a fun dance with the captain. You both have a great time, but he's a little too busy flirting with other girls.")
            print("Do you...")
            print("1. Try to get him to pay attention to you.")
            print("2. Leave him and find someone else.")
            choice = input("Enter your choice (1 or 2): ")
            if choice == '1':
                print("You try to talk to him more, but he seems distracted. You realize he's not really into you.")
            else:
                print("You decide to move on. He's not really your type.")
        else:
            print("You decline politely, but he doesn't seem to take it well. You're glad you said no.")
    elif choice == '2':
        print("The quiet guy is sweet and a bit awkward. He seems nervous but interested.")
        talk_choice = input("Do you talk to him? (yes/no): ").lower()
        if talk_choice == 'yes':
            print("You have a nice conversation. He's a great listener and you feel comfortable with him.")
            print("He asks if you want to slow dance.")
            dance_choice = input("Do you dance with him? (yes/no): ").lower()
            if dance_choice == 'yes':
                print("You share a slow dance. He's a little awkward, but his sincerity melts your heart. He leans in for a kiss.")
                player_inventory.append("kiss")
                webbrowser.open_new_tab("prom_kiss.jpg")
                input("Press Enter to exit.")
                time.sleep(1)
                sys.exit(0)

            else:
                print("You decline politely. He's nice, but you're not really feeling it.")
        else:
            print("You decide to talk to someone else. He's just too shy for you.")
    elif choice == '3':
        print("The funny guy tells you jokes that make you laugh out loud. He's relaxed and easygoing.")
        laugh_choice = input("Do you laugh with him? (yes/no): ").lower()
        if laugh_choice == 'yes':
            print("You have a great time laughing with him. He's so funny and charming. He asks if you want to dance.")
            dance_choice = input("Do you dance with him? (yes/no): ").lower()
            if dance_choice == 'yes':
                print("You have a blast dancing with him. He's so fun and you feel a spark between you. He leans in for a kiss.")
                player_inventory.append("kiss")
                webbrowser.open_new_tab("prom_kiss.jpg")
                input("Press Enter to exit.")
                time.sleep(2)
                sys.exit(0)
            else:
                print("You decline politely, but you can tell he's a little disappointed.")
        else:
            print("You're not in the mood for jokes right now. You decide to talk to someone else.")
    elif choice == '4':
        print("You decide to call it a night. Maybe next time!")
        webbrowser.open_new_tab("prom_alone.jpg")
        input("Press Enter to exit.")
        time.sleep(2)
        sys.exit(0)


if __name__ == "__main__":
    main()
