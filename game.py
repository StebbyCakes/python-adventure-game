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

    def creepy_cave():

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

    def creepy_cave():

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

    def creepy_cave():

        print("""The sense a sinister beast from below the waves, the crew looks overboard and alas! You're under attack by the Kraken! You raise your sails and prepare for battle..... What is this feeling....? So lost... Davy Jones has stolen your soul! He summoned the beast to distract you! As an empty vessel now do you: """)
        print("""1: If Davy Jones stole my soul it means his hideaout is nearby! Forget the Kraken, an impossible beast to conquer Set sail to the near island!""")
        print("""2: Davy Jones lives with the kraken under the sea, load the cannons, kill the beast and use him to travel beneath the waves""")
        print("""3: He must have escaped and is sailing away to his ship! Climb to the crow's nest and search for his direction to follow.""")
        answer = input("Enter your choice:")

        answer = input(>)
        if answer == '1':
            print("""You've become a soulless crew, no heart to fight, Davy Jones made way with your soul.""")
            callfunction()
        elif answer == '2':
            print("""The Kraken had a weakness in its eye! One cannon shot and he gave lent us his power! It sent us to Davy Jones Locker, retrieved our souls and we freed many others. """)
            callfunction()
        elif answer == '3':
            print("""You climbed up, scouted the all of your surroundings and found nothing, you barely managed to escape the Kraken too """)
            callfunction()
        elif answer == '4':
            callfunction()


play()
