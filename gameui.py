from tkinter import Tk, Button, Label


# import main
# from main import counter
# from place import *


# from main import drop_cookies, counter, game


class GameUI:
    def __init__(self):
        self.window = Tk()
        self.window.title('Jonty\'s Sweet Cookie Clicker')
        self.window.geometry('650x450+700+300')
        self.window.resizable(False, False)
        self.window.attributes('-topmost', 1)

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.pack_forget()
            widget.place_forget()

    # def display_cookies(self):
    #     self.label_item_count.configure(text=counter.count_info())
    #     place_top_left(self.label_item_count)

    # def update_cookie_info(self):
    #     display_text = f'Number of {counter.item_type}s: {counter.count}'
    #     if 10 < counter.count < 20:
    #         display_text += '           Keep going!'
    #     if 30 < counter.count < 40:
    #         display_text += f'           So many {counter.item_type}s!'
    #     if counter.count == 69:
    #         display_text += '            Nice.'
    #     if 80 < counter.count < 90:
    #         display_text += '           Things seem very peaceful.'
    #     label_cookie_count.configure(text=display_text)
    #     place_top_left(label_cookie_count)




# TODO Buttons:
# from main import gameUI, counter
from main import game

# def drop_10():
#     Button(game.ui.window, text=f'Drop 10 {game.counter.item_type}s', height=3, width=16,
                            # command=lambda: drop_cookies(10))
#     drop_20_button = Button(gameUI.window, text=f'Drop 20 {counter.item_type}s', height=3, width=16,
#                             command=lambda: drop_cookies(20))
#
#     # Death stuff
#     game_over_button = Button(gameUI.window, text='I\'m an idiot', height=3, width=16, command=end_game)
#     # placeCenter(game_over_button)
#
#     # Mugging Stuff
#     mugger_label = Label(gameUI.window, text='Oh no, a mugger!!')
#     oh_fuck_button = Button(gameUI.window, text='balls', height=3, width=10, command=mugger_choice)
#     # surrender_cookies_button = Button(root, text=f'Give him your {confectionary}s', command=surrenderCookies, width=20, height=3)
#
#     # Fight mugger Stuff
#     fight_mugger_button = Button(gameUI.window, text='Fight', command=fight_setup, width=7, height=3)
#     won_fight_label = Label(gameUI.window, text=f'''You managed to fend him off but he stabbed you
#     You're leaking {counter.item_type}s''')
#     bleed_severity = 5
#     bleed_count = 0
#     patch_up_button = Button(gameUI.window, text='Plug the bleed', command=patch_yourself_up)
#     patched_up = False
#
#     # Dog stuff
#     yes_baby_button = Button(text='Yes baby!', width=10, height=3, command=yes_baby)
#     kinky_clicks = 0
#
#     gameUI.window.mainloop()
