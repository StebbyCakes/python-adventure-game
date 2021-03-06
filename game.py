import time,sys
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()
  return value

game_still_going = True

def meet_mady(player):
    typingPrint('You collected all pieces of eight! ')
    typingPrint('After a long voyage at sea, you arrive at a small island. Within that island is a deep cave! ')
    typingPrint('Captain Mady emerges from the shadows and shouts that you must present your eight of pieces! ')
    typingPrint(f'You present your pieces of eight and Captain Mady gives you her treasure! Congratulations {player.promotion}! Youve conquered the seas! ')

def battle(player):

    typingPrint("\n")
    typingPrint("""Hurry! A pirate ship approaches! What do we do! """)
    print("\n")
    print("1: Load the cannons, turn the ship North by North East to have our starboard to their angle, prepare for battle!")
    print("2: We're not here to fight! Raise the sails!  Turn the ship opposite their direction! Then lower the sails and put them to the wind, we're out of here!")
    print("3: Climb to the crows nest pronto! Raise the White Flag, we can sail these seas in an alliance!")

    scenario_input = input("Enter your choice:")

    responses_dict = {
        "1": "The enemy ship wanted to be friends, but they raised the white flag too late... or maybe we chose to not see it. Either we sunk their ship and have more treasure in our collection. ",
        "2": "A cowardice play! You survived but with no respect for the Pirate Code! ",
        "3": "You got lucky the enemy ship was new to the seas, a seasoned crew might have wanted your treasures for themselves. They joined the alliance and you will not split loots. "
    }

    if scenario_input == '1':
        typingPrint("\n")
        typingPrint(responses_dict["1"])
        player.add_piece_of_eight()
        typingPrint("\n")
        typingPrint(f"You now have {player.piece_of_eight} of eight pieces")
        typingPrint("\n")
    elif scenario_input == '2':
        typingPrint("\n")
        typingPrint(responses_dict["2"])
    elif scenario_input == '3':
        typingPrint("\n")
        typingPrint(responses_dict["3"])

    global game_still_going
    game_still_going = False

def treasure(player):

    typingPrint("\n")
    typingPrint("""A treasure map was found on the ship! The crew looks a little closer... an 'x' on an island! This seems unrelated to Mady's pieces of eight. What do you do:  """)
    print("\n")
    print("1: Go to the island and plunder it until you find the treasure!")
    print("2: Forget the map, Mady's Treasure is priority!")
    print("3: Continue on your journey, if you pass that island along the way, you can drop anchor then.")

    scenario_input = input("Enter your choice:")

    responses_dict = {
        "1": "You found the treasure! Now you'll have more loot for when your adventure is over! ",
        "2": "A captain can make a wrong decisions sometimes. A pirate would gather more treasure than he could hold no matter the cost.",
        "3": "You continued to follow the wind, unfortunately it never brought you to the island with free loot."
    }

    if scenario_input == '1':
        typingPrint("\n")
        typingPrint(responses_dict["1"])
        player.add_piece_of_eight()
        typingPrint("\n")
        typingPrint(f"You now have {player.piece_of_eight} of eight pieces")
        typingPrint("\n")
    elif scenario_input == '2':
        typingPrint("\n")
        typingPrint(responses_dict["2"])
    elif scenario_input == '3':
        typingPrint("\n")
        typingPrint(responses_dict["3"])

    if player.piece_of_eight == 8:
        global game_still_going
        game_still_going = False
    else: battle(player)


def crash_landing(player):

    typingPrint("\n")
    typingPrint("The ship has crashed! You've scraped a hole into the bottom of the brig! Are you really worthy of being a Captain? The only wood that can be used is from the barrel of rum... but it still half full! Do you: ")
    print("\n")
    print("1: Take apart that scoundrelous barrel and hurry up and fix the ship before we sink to the depths and meet Davy Jones Locker for good.")
    print("2: Pass around that barrel make sure everyone gets their serving, not a drop to spare!")
    print("3: Argue about who gets to drink the most rum, this way maybe you can have a chance to drink most of it yourself!")

    scenario_input = input("Enter your choice:")

    responses_dict = {
        "1": "You CHOSE to spill rum? The life at sea does not call to you. You may have saved the ship but you lost your pirate heart.",
        "2": "You're buzzed and tipping around the ship as you fix her well, you might have barely the hole before she sunk, but you're still on the voyage ahead!",
        "3": "As you argue around someone broke the barrel to fix the ship, now nobody got the taste of a good grog."
    }

    if scenario_input == '1':
        typingPrint("\n")
        typingPrint(responses_dict["1"])
    elif scenario_input == '2':
        typingPrint("\n")
        typingPrint(responses_dict["2"])
        player.add_piece_of_eight()
        typingPrint("\n")
        typingPrint(f"You now have {player.piece_of_eight} of eight pieces")
        typingPrint("\n")
    elif scenario_input == '3':
        typingPrint("\n")
        typingPrint(responses_dict["3"])

    if player.piece_of_eight == 8:
        global game_still_going
        game_still_going = False
    else: treasure(player)

def far_seas(player):

    typingPrint("\n")
    typingPrint("The sense a sinister beast from below the waves, the crew looks overboard and alas! You're under attack by the Kraken! You raise your sails and prepare for battle..... What is this feeling....? So lost... Davy Jones has stolen your soul! He summoned the beast to distract you! As an empty vessel now do you: ")
    print("\n")
    print("1: If Davy Jones stole my soul it means his hideaout is nearby! Forget the Kraken, an impossible beast to conquer, set sail to the nearest island!")
    print("2: Davy Jones lives with the kraken under the sea, load the cannons, kill the beast and use him to travel beneath the waves")
    print("3: He must have escaped and is sailing away to his ship! Climb to the crow's nest and search for his direction to follow.")

    scenario_input = input("Enter your choice:")

    responses_dict = {
        "1": "You've become a soulless crew, no heart to fight, Davy Jones made way with your soul.",
        "2": "The Kraken had a weakness in its eye! One cannon shot and he lent us his power! It sent us to Davy Jones Locker, retrieved our souls and we freed many others.",
        "3": "You climbed up, scouted the all of your surroundings and found nothing, you barely managed to escape the Kraken too."
    }

    if scenario_input == '1':
        typingPrint("\n")
        typingPrint(responses_dict["1"])
    elif scenario_input == '2':
        typingPrint("\n")
        typingPrint(responses_dict["2"])
        player.add_piece_of_eight()
        typingPrint("\n")
        typingPrint(f"You now have {player.piece_of_eight} of eight pieces")
        typingPrint("\n")
    elif scenario_input == '3':
        typingPrint("\n")
        typingPrint(responses_dict["3"])


    if player.piece_of_eight == 8:
        global game_still_going
        game_still_going = False
    else: crash_landing(player)

def starving_crew(player):

    typingPrint("\n")
    typingPrint("""The crew is starving! With scurvvy on the brink of the horizon, do you: """)
    print("\n")
    print("""1: Sail to the nearest island, we need fruits!""")
    print("""2: Begin to fish in the waters, there's plenty of food in the sea.""")
    print("""3: We dont need food, just more rum! """)

    scenario_input = input("Enter your choice:")

    responses_dict = {
        "1": "A seasoned pirate who knows the dangers of sailing the seas without proper feast.",
        "2": "You've settled your hunger but still too young for the sea, she will soon consume you! Scurvvy only happens when you dont eat fruit in proper time. Now you're slowly dying.",
        "3": "A pirate at heart, you knew what scurvvy could do and doomed your crew with it. Although on purpose to die at seas like a true legend on their last journey."
    }

    if scenario_input == '1':
        typingPrint("\n")
        typingPrint(responses_dict["1"])
        player.add_piece_of_eight()
        typingPrint("\n")
        typingPrint(f"You now have {player.piece_of_eight} of eight pieces")
        typingPrint("\n")
    elif scenario_input == '2':
        typingPrint("\n")
        typingPrint(responses_dict["2"])
    elif scenario_input == '3':
        typingPrint("\n")
        typingPrint(responses_dict["3"])

    if player.piece_of_eight == 8:
        global game_still_going
        game_still_going = False
    else: far_seas(player)

def overboard_sailer(player):
    typingPrint("\n")
    typingPrint("I'm so glad those sirens didn't kill you. Maybe the pizza helped. You're calmly sailing the seas continuing on your adventure when avast! Your crew has spotted a man overboard to the east! Do you: ")
    print("\n")
    print("1: Forget the man, because he's out in the open sea proves he was unable to handle her wrath and will do no good to our crew.")
    print("2: Finish him off, put him out of his misery, he's been sunburned far beyond our help anyway.")
    print("3: Save him! Bring him aboard, take his loot, help him heal.")

    scenario_input = input("Enter your choice:")

    responses_dict = {
        "1": "The Pirate Code says to help your fellow pirates, have you fogotten?",
        "2": "Maybe a good deed, but even a weak body is an able body in combat.",
        "3": "You Truly follow the Pirate Code, or do you just seize opportunity in gaining extra hands on your voyage? It doesnt matter, either way he is the newest addition to the crew."
    }

    if scenario_input == '1':
        typingPrint("\n")
        typingPrint(responses_dict["1"])
    elif scenario_input == '2':
        typingPrint("\n")
        typingPrint(responses_dict["2"])
    elif scenario_input == '3':
        typingPrint("\n")
        typingPrint(responses_dict["3"])
        player.add_piece_of_eight()
        typingPrint("\n")
        typingPrint(f"You now have {player.piece_of_eight} of eight pieces")
        typingPrint("\n")

    if player.piece_of_eight == 8:
        global game_still_going
        game_still_going = False
    else: starving_crew(player)

def boat_voyage(player):
    typingPrint("\n")
    typingPrint(" You've finally made it aboard the thie ship on your first sailing voyage! Just as you begin to relax you begin hearing a lovely sound from the distance. The sound is alluring and seems to beckoning you to sail in that direction.")
    typingPrint("You begin to follow the lovely sound. As you get closer you notice some strange beings in the water. Wait....are those sirens?")
    typingPrint("Three beautiful mermaids are bathing on a rock! They introduce themselves as Kate, Lea, and Trevor.")
    typingPrint("Kate says that she knows the way to Captain Mady's treasure. Lea begins singing about being part of your world. Trevor pulls out a slice of pizza and begins to stare away. Which siren will you ask for help?")
    print("\n")
    print("1: Kate")
    print("2: Lea")
    print("3: Trevor")

    scenario_input = input("Enter your choice:")

    responses_dict = {
        "1": "Smart choice!! Kate gives you two peices of eight and whipsers a hint about how to find Captain Mady!",
        "2": "Lea says that her sister Ariel has what you're looking for and gives you two peices of eight and whipsers a hint to find Captain Mady!",
        "3": "Well...you tried. That counts for something. Trevor gives you some lint from his belly button and swims off."
    }

    if scenario_input == '1':
        typingPrint("\n")
        typingPrint(responses_dict["1"])
        player.add_piece_of_eight()
        typingPrint("\n")
        typingPrint(f"You now have {player.piece_of_eight} of eight pieces")
        typingPrint("\n")
    elif scenario_input == '2':
        typingPrint("\n")
        typingPrint(responses_dict["2"])
    elif scenario_input == '3':
        typingPrint("\n")
        typingPrint(responses_dict["3"])

    if player.piece_of_eight == 8:
        global game_still_going
        game_still_going = False
    else: overboard_sailer(player)

def parting_home(player):

    print("\n")
    typingPrint("You're through with Mady's meddling ruffian. It's time to begin the adventure! You head to the shores and you're met with a man selling Brigantines', perfect size ship for your adventure you think to yourself. So do you: ")
    print("\n")
    print("1: Wait until night to board the ship quietly and set sail away without notice.")
    print("2: Approach the man and tell him standing between you and your calling is a dangerous move.")
    print("3: Go back to the island, work for your gold and pay the man his share for his fair ship.")

    scenario_input = input("Enter your choice:")

    responses_dict = {
        "1": "You're coward of a pirate one who doesnt plunder as he pleases!",
        "2": "A pirate Lord has been born! The seas face a new threat, any pirate out in the water should tremble in their boots before you and your new awakening",
        "3": "A man who earns his fair share has no right to be a pirate, might as well work for the state and begone with this treacherous pirate journey."
    }

    if scenario_input == '1':
        typingPrint("\n")
        typingPrint(responses_dict["1"])
    elif scenario_input == '2':
        typingPrint("\n")
        typingPrint(responses_dict["2"])
        player.add_piece_of_eight()
        typingPrint("\n")
        typingPrint(f"You now have {player.piece_of_eight} of eight pieces")
        typingPrint("\n")
    elif scenario_input == '3':
        typingPrint("\n")
        typingPrint(responses_dict["3"])

    if player.piece_of_eight == 8:
        global game_still_going
        game_still_going = False
    else: boat_voyage(player)

def begin_game(player):
    typingPrint("\n")
    typingPrint(f"Ahoy, {player.name}! You're about to embark on an amazing voyage to obtain Captain Mady's treasure! If you know anything about Captain Mady, then you know this won't be easy. This voyage will be long and tedious. In order to obtain Captain Mady's treasure, you must collect all pieces of eight and present them to her. ")
    typingPrint("Throughout your journey, fun adventures await. Your decisions are important. Choosing the right reponses will ensure that you collect enough pieces to receive her treasure. ")
    typingPrint("Good luck! ")
    print("\n")
    typingPrint("You've just entered Rigi Town! Wow what an exciting place to be! There are wanted posters for Captain Mady all over the town. Rumor is she stole another pirate's booty! Can you believe it? I certainly can. I guess somethings just never change! ")
    typingPrint("Look alive! One of Mady's ruffians just approached you! ")
    typingPrint("What will you do? ")
    print("\n")

    print("1: Greet her with a nice and warm smile")
    print("2: Run away")
    print("3: Kick her butt!")

    scenario_input = input("Enter your choice:")

    responses_dict = {
        "1": "Are you serious? This is one of Captain Mady's goons we're talking about! She just kicked your butt and sent you packing!",
        "2": "How did you become a pirate???",
        "3": "I mean....she did deserve it! Great job beating up Mady's goon. You picked up two pieces of eight from the ground next to the goon's swollen face!"
    }

    if scenario_input == '1':
        typingPrint("\n")
        typingPrint(responses_dict["1"])
    elif scenario_input == '2':
        typingPrint("\n")
        typingPrint(responses_dict["2"])
    elif scenario_input == '3':
        typingPrint("\n")
        typingPrint(responses_dict["3"])
        player.add_piece_of_eight()
        typingPrint("\n")
        typingPrint(f"You now have {player.piece_of_eight} of eight pieces")

    if player.piece_of_eight == 8:
        global game_still_going
        game_still_going = False
    else: parting_home(player)


def play():

    print("""""
                __   ____  ____   ______   ____  ____  ____
               /  ] /    ||    \ |      | /    ||    ||    \
              /  / |  o  ||  o  )|      ||  o  | |  | |  _  |
             /  /  |     ||   _/ |_|  |_||     | |  | |  |  |
            /   \_ |  _  ||  |     |  |  |  _  | |  | |  |  |
            \     ||  |  ||  |     |  |  |  |  | |  | |  |  |
             \____||__|__||__|     |__|  |__|__||____||__|__|
             ___ ___   ____  ___    __ __  __   _____
            |   |   | /    ||   \  |  |  ||  | / ___/
            | _   _ ||  o  ||    \ |  |  ||_ |(   \_
            |  \_/  ||     ||  D  ||  ~  |  \| \__  |
            |   |   ||  _  ||     ||___, |     /  \ |
            |   |   ||  |  ||     ||     |     \    |
            |___|___||__|__||_____||____/       \___|
              ____  ___    __ __    ___  ____   ______  __ __  ____     ___
             /    ||   \  |  |  |  /  _]|    \ |      ||  |  ||    \   /  _]
            |  o  ||    \ |  |  | /  [_ |  _  ||      ||  |  ||  D  ) /  [_
            |     ||  D  ||  |  ||    _]|  |  ||_|  |_||  |  ||    / |    _]
            |  _  ||     ||  :  ||   [_ |  |  |  |  |  |  :  ||    \ |   [_
            |  |  ||     | \   / |     ||  |  |  |  |  |     ||  .  \|     |
            |__|__||_____|  \_/  |_____||__|__|  |__|   \__,_||__|\_||_____|

    """"")

    while game_still_going:
        player_name = input('Hurry up and enter your scallywags name: ').capitalize()
        guideList = ['Sayeda', 'Esteban', 'Eric'];
        guide_List = ['Sayeda', 'Esteban', 'Eric'];
        for item in guide_List:
            print(item)
        input('Who will be your guide?')

        class Pirate:
            def __init__(self):
                self.name = 'Bootleg ' + player_name
                self.promotion = 'Captain ' + player_name
                self.piece_of_eight = 0

            def add_piece_of_eight(self):
                self.piece_of_eight = self.piece_of_eight + 2

        player = Pirate()
        begin_game(player)

    if player.piece_of_eight == 8:
        meet_mady(player)
    else:
        typingPrint("\n")
        typingPrint('After a long voyage at sea, you arrive at a small island. Within that island is a deep cave! ')
        typingPrint('Captain Mady emerges from the shadows and shouts that you must present your eight of pieces! ')
        typingPrint(f"You only have {player.piece_of_eight} pieces. You don't have enough!" )
        typingPrint("Captain Mady takes you a prisoner and you are never seen again!")
        typingPrint('The End!')

play()
