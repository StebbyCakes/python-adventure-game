class Pirate:
    def __init__(self):
        self.name = input('Hurry up and enter your scallywags name: ')
        self.first_name = 'Bootleg'

    def show_full_name(self):
        print(self.first_name + ' ' + self.name.capitalize())

def play():

    player = Pirate()
    player.show_full_name()
#
#
# #     def room_name():
# #         print('narrative')
# #         answer = input(>)
# # if answer == '1':
# #     callfunction()
# # if answer == '2':
# #     callfunction()
# # if answer == '3':
# #     callfunction()
# # if answer == '4':
# #     callfunction()
# #
# #
play()
