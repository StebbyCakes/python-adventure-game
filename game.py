class Pirate:
    def __init__(self):
        self.name = input('Hurry up and enter your scallywags name: ')
        self.first_name = 'Bootleg'
        self.piece_of_eight = 0

    def show_full_name(self):
        print(self.first_name + ' ' + self.name.capitalize())

    def add_piece_of_eight(self):
        self.piece_of_eight = self.piece_of_eight + 2


def play():

    player = Pirate()
    player.show_full_name()

    print("""Ahoy, Matey! You're about to embark on an amazing voyage to obtain Captain Mady's treasure. If you know Captain Mady, then you know this won't be easy. As a seasoned pirate, you know that this voyage will be long and
    tedious; however, no one knows the seaven seas quite like you! In order to obtain Captain Mady's treasure, you must collect all pieces of eight and present them to her. Captain Mady has minions in each destination on your map.
    The pirates will give you a riddle, if answered correctly, then will give you some pieces of eight. Answer incorrectly.....let's just say Captain Mady's pirates aren't too forgiving. Following your map, you must first travel
    through Rigi Town. Once you've conquered goons of the city, there is a ship that awaits you that carry you across the seas where the sirens await you! Finally you'll arrive at the creeyp cave where Captain Mady awaits you!
    Good luck! """)

    rigi_town()
    boat_voyage()
    creepy_cave()

    def rigi_town():
        print('Ahoy! you ')
        print('(1) ')
        print('2:')
        print('3:')
        print('4:')

        answer = input("Enter your choice:")

        if answer == '1':
            callfunction()
        elif answer == '2':
            callfunction()
        elif answer == '3':
            callfunction()
        elif answer == '4':
            callfunction()

    def boat_voyage():

        print('narrative')

        answer = input("Enter your choice:")

        answer = input(>)
        if answer == '1':
            callfunction()
        elif answer == '2':
            callfunction()
        elif answer == '3':
            callfunction()
        elif answer == '4':
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


play()
