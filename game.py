class Pirate:
    def __init__(self):
        self.name = input('Hurry up and enter your scallywags name: ')
        self.first_name = 'Bootleg'
        self.piece_of_eight = 0

    def show_full_name(self):
        print(self.first_name + ' ' + self.name.capitalize())

    def add_piece_of_eight(self):
        self.piece_of_eight = self.piece_of_eight + 2

def far_seas():

    print("""The sense a sinister beast from below the waves, the crew looks overboard and alas! You're under attack by the Kraken! You raise your sails and prepare for battle..... What is this feeling....? So lost... Davy Jones has stolen your soul! He summoned the beast to distract you! As an empty vessel now do you: """)
    print("""1: If Davy Jones stole my soul it means his hideaout is nearby! Forget the Kraken, an impossible beast to conquer, set sail to the nearest island!""")
    print("""2: Davy Jones lives with the kraken under the sea, load the cannons, kill the beast and use him to travel beneath the waves""")
    print("""3: He must have escaped and is sailing away to his ship! Climb to the crow's nest and search for his direction to follow.""")
    answer = input("Enter your choice:")

    answer = input(>)
    if answer == '1':
        print("""You've become a soulless crew, no heart to fight, Davy Jones made way with your soul.""")
        callfunction()
    elif answer == '2':
        print("""The Kraken had a weakness in its eye! One cannon shot and he lent us his power! It sent us to Davy Jones Locker, retrieved our souls and we freed many others.""")
        callfunction()
    elif answer == '3':
        print("""You climbed up, scouted the all of your surroundings and found nothing, you barely managed to escape the Kraken too""")
        callfunction()

def starving_crew():

    print("""The crew is starving! With scurvvy on the brink of the horizon, do you: """)
    print("""1: Sail to the nearest island, we need fruits!""")
    print("""2: Begin to fish in the waters, there's plenty of food in the sea.""")
    print("""3: We dont need food, just more rum! """)

    answer = input("Enter your choice:")

    answer = input(>)
    if answer == '1':
        print("""A seasoned pirate who knows the dangers of sailing the seas without proper feast.""")
        callfunction()
    elif answer == '2':
        print("""You've settled your hunger but still too young for the sea, she will soon consume you! Scurvvy only happens when you dont eat fruit in proper time. Now you're slowly dying.""")
        callfunction()
    elif answer == '3':
        print("""A pirate at heart, you knew what scurvvy could do and doomed your crew with it. Although on purpose to die at seas like a true legend on their last journey.""")
        callfunction()

def overboard_sailer():

    print("""You're calmly sailing the seas continuing on your adventure when avast! Your crew has spotted a man overboard to the east! Do you: """)
    print("""1: Forget the man, because he's out in the open sea proves he was unable to handle her wrath and will do no good to our crew.""")
    print("""2: Finish him off, put him out of his misery, he's been sunburned far beyond our help anyway.""")
    print("""3: Save him! Bring him aboard, take his loot, help him heal.""")
    answer = input("Enter your choice:")

    answer = input(>)
    if answer == '1':
        print("""The Pirate Code says to help your fellow pirates, have you fogotten?""")
        callfunction()
    elif answer == '2':
        print("""Maybe a good deed, but even a weak body is an able body in combat.""")
        callfunction()
    elif answer == '3':
        print("""You Truly follow the Pirate Code, or do you just seize opportunity in gaining extra hands on your voyage? It doesnt matter, either way he is the newest addition to the crew.""")
        callfunction()

def boat_voyage(player):

    print('Whew! That was scary! Just as you begin to relax you begin hearing a lovely sound from the distance. The sound is alluring and seems to beckoning you to sail in that direction.')
    print("""You direct your crew that whevever that beauitful sound is coming from. As you get closer you notice some strange in the water....are those sirens? Three beautiful meermaids are nested
    beautifuly on a rock! They introduce themselves as Kate, Lea, and Trevor. Kate is smart and knows the way to Captain Mady. Lea is wise and knows Captains Mady's tricks!. Which siren will you ask for help?
    (1) Kate, (2) Lea, (3) Trevor """)

    scenario_input = input("Enter your choice:")

    if scenario_input == '1':
        print("Smart choice!! Kate gives you two peices of eight and whipsers a hint to find Captain Mady")
        player.add_piece_of_eight()
        print(f"You now have {player.piece_of_eight} pieces")
    elif scenario_input == '2':
        print("Wise choice!! Lea gives you two peices of eight and whipsers a hint to find Captain Mady ")
    elif scenario_input == '3':
        print("Well...you tried. That counts for something. Trevor gives you some lint from his belly button and swims off.")

    creepy_cave(player)

def parting_home():

    print("""You're through with Mady's meddling ruffian. It's time to begin the adventure! You head to the shores and you're met with a man selling Brigantines', perfect size ship for your adventure you think to yourself. So do you: """)
    print(""""1: Wait until night to board the ship quietly and set sail away without notice.""")
    print("""2: Approach the man and tell him standing between you and your calling is a dangerous move.""")
    print("""3: Go back to the island, work for your gold and pay the man his share for his fair ship.""")

    answer = input("Enter your choice:")

    answer = input(>)
    if answer == '1':
        print("""You're coward of a pirate one who doesnt plunder as he pleases!""")
        callfunction()
    elif answer == '2':
        print("""A pirate Lord has been born! The seas face a new threat, any pirate out in the water should tremble in their boots before you and your new awakening""")
        callfunction()
    elif answer == '3':
        print("""A man who earns his fair share has no right to be a pirate, might as well work for the state and begone with this treacherous pirate journey.""")
        callfunction()

def begin_game(player):

    print("""Ahoy, Matey! You're about to embark on an amazing voyage to obtain Captain Mady's treasure. If you know Captain Mady, then you know this won't be easy. As a seasoned pirate, you know that this voyage will be long and
    tedious; however, no one knows the seaven seas quite like you! In order to obtain Captain Mady's treasure, you must collect all pieces of eight and present them to her. Captain Mady has minions in each destination on your map.
    The pirates will give you a riddle, if answered correctly, then will give you some pieces of eight. Answer incorrectly.....let's just say Captain Mady's pirates aren't too forgiving. Following your map, you must first travel
    through Rigi Town. Once you've conquered goons of the city, there is a ship that awaits you that carry you across the seas where the sirens await you! Finally you'll arrive at the creeyp cave where Captain Mady awaits you!
    Good luck! """)

    print("""You've just entered Rigi Town! Wow what an exciting place to be! There are wanted posters all over for Captain Mady, rumor is she stole another booty! Can you believe it?
    I certainly can. I guess somethings just never change! Look alive! One of Mady's ruffians just approached you!
    What will you do? (1): Greet her with a nice and warm smile, (2): Run away, or (3): Kick her butt!""")

    scenario_input = input("Enter your choice:")
    if scenario_input == '1':
        print("Are you serious? This is one of Captain Mady's goons we're talking about. She just kicked you butt and sent you packing!")
    elif scenario_input == '2':
        print("How did you become a pirate??? ")
    elif scenario_input == '3':
        print("I mean....she did deserve it! Great job beating up Mady's goon. You picked up two pieces of eight from the ground nex to the goon's swollen face!")
        player.add_piece_of_eight()
        print(f"You now have {player.piece_of_eight} pieces")
        

def play():

    player = Pirate()
    player.show_full_name()
    begin_game(player)

play()
