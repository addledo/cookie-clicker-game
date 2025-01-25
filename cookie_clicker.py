import random
import tkinter as tk
from tkinter import Button
from tkinter import Label
from tkinter import messagebox
from place import *
from item_counter import Counter
from game import Game

# FIXES BLURRY TEXT ON WINDOWS -----------------
# from ctypes import windll
#windll.shcore.SetProcessDpiAwareness(1)

game = Game()

def display_cookies():
    label_cookie_count.configure(text=counter.count_info)
    place_top_left(label_cookie_count)

def add_cookies():
    counter.count += 1
    global crafty
    if crafty:
        Label(text='You\'re a crafty bugger aren\'t you').place(x=60, y=240)
    crafty = False
    encouraging_messages(counter.count)
    no_cookies_fun()
    global switcheroo_number
    if counter.count == switcheroo_number:
        ol_switcheroo()
    if counter.count == 89:
        switch_back()
    if counter.count == 100:
        get_mugged()


def encouraging_messages(display_text):
    display_text = f'Number of {counter.item}s: {counter.count}'
    if 10 < counter.count < 20:
        display_text += '           Keep going!'
    if 30 < counter.count < 40:
        display_text += f'           So many {counter.item}s!'
    if counter.count == 69:
        display_text += '            Nice.'
    if 80 < counter.count < 90:
        display_text += '           Things seem very peaceful.'
    label_cookie_count.configure(text=display_text)
    place_top_left(label_cookie_count)


def no_cookies_fun():
    if counter.count == 5:
        button_change_to_eggs.place(x=100, y=150)

    if counter.count > 8 or counter.item == 'egg':
        button_change_to_eggs.place_forget()


def change_to_eggs():
    counter.item = 'egg'
    global drop_10_button
    global drop_20_button
    drop_10_button = Button(game.window, text=f'Drop 10 {counter.item}s', height=3, width=16, command=lambda: drop_cookies(10))
    drop_20_button = Button(game.window, text=f'Drop 20 {counter.item}s', height=3, width=16, command=lambda: drop_cookies(20))
    display_cookies()


def drop_cookies(num):
    counter.count -= num
    display_cookies()
    if counter.count < 0:
        player_dies()
    global crafty
    crafty = False


def ol_switcheroo():
    global has_switcherood
    if has_switcherood:
        return
    clear_window(game.window)
    display_cookies()
    place_bottom_left(button_add_one)
    place_bottom_right(drop_10_button, 50)
    global crafty
    has_switcherood = True
    crafty = True
    # gotcha_label.place(x=50, y=270)


def switch_back():
    clear_window(game.window)
    display_cookies()
    place_bottom_right(button_add_one, 50)
    place_bottom_left(drop_20_button)


def get_mugged():
    clear_window(game.window)
    display_cookies()
    mugger_label.place(x=300, y=80)
    oh_fuck_button.place(x=300, y=250)


def surrender_cookies():
    clear_window(game.window)
    counter.count = 1
    display_cookies()
    Label(text=f'''The mugger takes pity on you and lets you keep 1 {counter.item}.
    
    
As he leaves, a stray dog appears and locks eyes
onto your one remaining {counter.item}.''').place(x=50, y=100)
    place_bottom_left(Button(text='Punt the dog', width=12, height=2, command=punt_dog))
    place_bottom_right(Button(text='Run', width=10, height=2, command=run_from_dog), 0)


def run_from_dog():
    clear_window(game.window)
    display_cookies()
    Label(text='''Good choice. As you run, you see the mugger up ahead.
He thinks your chasing him. As you get close he stabs you.
(It's self defence)''').place(y=100, x=50)
    place_bottom_right(game_over_button, 250)


def punt_dog():
    clear_window(game.window)
    display_cookies()
    # Random boolean?
    punt_successful = random.choice([True, False])
    if not punt_successful:
        Label(text='''First off you're a terrible person. Secondly it's a very big dog.
    It tackles you to the ground and bites on to your throat''').place(x=50, y=100)
        place_bottom_right(Button(text='Oh no', width=10, height=3, command=death_by_dog), 100)
        place_bottom_left(yes_baby_button)
    else:
        Label(text='''Against all odds you successfully punt the dog off a nearby cliff.
You're alive but you just killed a dog. Good job.''').place(x=50, y=100)
    place_bottom_right(Button(text='Oh no', width=10, height=3, command=game.window.destroy), 100)


def death_by_dog():
    clear_window(game.window)
    display_cookies()
    messagebox.showinfo(message='''Just as the dog is about to finish you off,
the mugger charges in, barreling into the dog
and knocking it unconscious.
Then he disappears into the distance without a word.
Maybe he's not such a bad guy after all''')
    place_bottom_right(Button(text='Go home', height=3, width=8, command=go_home), 200)


def go_home():
    clear_window(game.window)
    display_cookies()
    messagebox.showinfo(message='You get home and find the mugger with your wife.')
    game.window.destroy()


def yes_baby():
    yes_baby_button.configure(text='???', command=stop_with_the_kinky)
    place_bottom_left(yes_baby_button)


def stop_with_the_kinky():
    yes_baby_button.configure(text='Stop it')
    place_bottom_left(yes_baby_button)
    global kinky_clicks
    kinky_clicks += 1
    if kinky_clicks == 40:
        seduce_the_dog()


def seduce_the_dog():
    messagebox.showinfo(message=
                        '''You've successfully seduced the dog.
                        The mugger may be sleeping with your wife 
                        but you came out on top.''')
    game.window.destroy()


def mugger_choice():
    clear_window(game.window)
    display_cookies()
    # oh_fuck_button.destroy()
    place_bottom_left(fight_mugger_button)
    place_bottom_right(Button(game.window, text=f'Give him your {counter.item}s', command=surrender_cookies, width=20, height=3),
                       100)


def fight_setup():
    clear_window(game.window)
    display_cookies()
    place_center(won_fight_label)
    place_bottom_right(patch_up_button, 200)
    fight_mugger()


def patch_yourself_up():
    global bleed_severity
    global patched_up
    bleed_severity -= 1
    if bleed_severity <= 0:
        patched_up = True


def fight_mugger():
    global patched_up
    if counter.count <= 0:
        player_dies()
        return
    counter.count -= 1
    display_cookies()
    if not patched_up:
        game.window.after(70, fight_mugger)
    else:
        messagebox.showinfo(message=f'''Congratulations, you've won. You have {counter.count} {counter.item}s.
    Unfortunately the mugger is sleeping with your wife.''')
        game.window.destroy()


def player_dies():
    clear_window(game.window)
    label = Label(text=f'''You lost all your {counter.item}s. You're dead.''')
    place_top_left(label)
    game_over_button.place(x=350, y=150)

def draw_base_layout():
    clear_window(game.window)
    display_cookies()

def end_game():
    game.window.destroy()



counter = Counter()

# Buttons
button_change_to_eggs = Button(game.window, text='I don\'t like cookies', height=3, width=25, command=change_to_eggs)
button_add_one = Button(game.window, text='Click Me', height=3, width=10, command=add_cookies)

label_cookie_count = Label(game.window, text=counter.count_info)

# START GAME
draw_base_layout()
place_bottom_right(button_add_one)

# Switcheroo Stuff
gotcha_label = Label(game.window, text='gotcha')
switcheroo_number = random.randrange(31, 39)
crafty = False
has_switcherood = False
drop_10_button = Button(game.window, text=f'Drop 10 {counter.item}s', height=3, width=16, command=lambda: drop_cookies(10))
drop_20_button = Button(game.window, text=f'Drop 20 {counter.item}s', height=3, width=16, command=lambda: drop_cookies(20))

# Death stuff
game_over_button = Button(game.window, text='I\'m an idiot', height=3, width=16, command=end_game)
# placeCenter(game_over_button)

# Mugging Stuff
mugger_label = Label(game.window, text='Oh no, a mugger!!')
oh_fuck_button = Button(game.window, text='balls', height=3, width=10, command=mugger_choice)
# surrender_cookies_button = Button(root, text=f'Give him your {confectionary}s', command=surrenderCookies, width=20, height=3)

# Fight mugger Stuff
fight_mugger_button = Button(game.window, text='Fight', command=fight_setup, width=7, height=3)
won_fight_label = Label(game.window, text=f'''You managed to fend him off but he stabbed you
You're leaking {counter.item}s''')
bleed_severity = 5
bleed_count = 0
patch_up_button = Button(game.window, text='Plug the bleed', command=patch_yourself_up)
patched_up = False

# Dog stuff
yes_baby_button = Button(text='Yes baby!', width=10, height=3, command=yes_baby)
kinky_clicks = 0

game.window.mainloop()
