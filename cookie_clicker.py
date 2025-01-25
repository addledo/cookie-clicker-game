import random
import tkinter as tk
from tkinter import Button
from tkinter import Label
from tkinter import messagebox
from place import *

# FIXES BLURRY TEXT ON WINDOWS -----------------
# from ctypes import windll
#windll.shcore.SetProcessDpiAwareness(1)

# Window Settings
root = tk.Tk()
root.title('Jonty\'s Sweet Cookie Clicker')
root.geometry('650x450+700+300')
root.resizable(False, False)
root.attributes('-topmost', 1)




def display_cookies():
    global number_of_cookies
    cookie_count_label.configure(text=f'Number of {confectionary}s: {number_of_cookies}')
    place_top_left(cookie_count_label)


def add_cookies():
    global number_of_cookies
    number_of_cookies += 1
    global crafty
    if crafty:
        Label(text='You\'re a crafty bugger aren\'t you').place(x=60, y=240)
    crafty = False
    encouraging_messages(number_of_cookies)
    no_cookies_fun()
    global switcheroo_number
    if number_of_cookies == switcheroo_number:
        ol_switcheroo()
    if number_of_cookies == 89:
        switch_back()
    if number_of_cookies == 100:
        get_mugged()


def encouraging_messages(display_text):
    global number_of_cookies
    display_text = f'Number of {confectionary}s: {number_of_cookies}'
    if 10 < number_of_cookies < 20:
        display_text += '           Keep going!'
    if 30 < number_of_cookies < 40:
        display_text += f'           So many {confectionary}s!'
    if number_of_cookies == 69:
        display_text += '            Nice.'
    if 80 < number_of_cookies < 90:
        display_text += '           Things seem very peaceful.'
    cookie_count_label.configure(text=display_text)
    place_top_left(cookie_count_label)


def no_cookies_fun():
    global number_of_cookies
    global confectionary
    if number_of_cookies == 5:
        no_cookies_button.place(x=100, y=150)

    if number_of_cookies > 8 or confectionary == 'egg':
        no_cookies_button.place_forget()


def dont_like_cookies():
    global confectionary
    confectionary = 'egg'
    global drop_10_button
    global drop_20_button
    drop_10_button = Button(root, text=f'Drop 10 {confectionary}s', height=3, width=16, command=drop_10_cookies)
    drop_20_button = Button(root, text=f'Drop 20 {confectionary}s', height=3, width=16, command=drop_20_cookies)
    display_cookies()


def drop_cookies(num):
    global number_of_cookies
    number_of_cookies -= num
    display_cookies()
    if number_of_cookies < 0:
        you_die()
    global crafty
    crafty = False


def drop_10_cookies():
    global number_of_cookies
    drop_cookies(10)
    if number_of_cookies > 0:
        gotcha_label.place(x=450, y=270)


def drop_20_cookies():
    drop_cookies(20)


def ol_switcheroo():
    global has_switcherood
    if has_switcherood:
        return
    clear_window()
    display_cookies()
    place_bottom_left(get_cookie_button)
    place_bottom_right(drop_10_button, 50)
    global crafty
    has_switcherood = True
    crafty = True
    # gotcha_label.place(x=50, y=270)


def switch_back():
    clear_window()
    display_cookies()
    place_bottom_right(get_cookie_button, 50)
    place_bottom_left(drop_20_button)


def get_mugged():
    clear_window()
    display_cookies()
    mugger_label.place(x=300, y=80)
    oh_fuck_button.place(x=300, y=250)


def surrender_cookies():
    clear_window()
    global number_of_cookies
    number_of_cookies = 1
    display_cookies()
    Label(text=f'''The mugger takes pity on you and lets you keep 1 {confectionary}.
    
    
As he leaves, a stray dog appears and locks eyes
onto your one remaining {confectionary}.''').place(x=50, y=100)
    place_bottom_left(Button(text='Punt the dog', width=12, height=2, command=punt_dog))
    place_bottom_right(Button(text='Run', width=10, height=2, command=run_from_dog), 0)


def run_from_dog():
    clear_window()
    display_cookies()
    Label(text='''Good choice. As you run, you see the mugger up ahead.
He thinks your chasing him. As you get close he stabs you.
(It's self defence)''').place(y=100, x=50)
    place_bottom_right(game_over_button, 250)


def punt_dog():
    clear_window()
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
    place_bottom_right(Button(text='Oh no', width=10, height=3, command=root.destroy), 100)


def death_by_dog():
    clear_window()
    display_cookies()
    messagebox.showinfo(message='''Just as the dog is about to finish you off,
the mugger charges in, barreling into the dog
and knocking it unconscious.
Then he disappears into the distance without a word.
Maybe he's not such a bad guy after all''')
    place_bottom_right(Button(text='Go home', height=3, width=8, command=go_home), 200)


def go_home():
    clear_window()
    display_cookies()
    messagebox.showinfo(message='You get home and see the mugger sleeping with your wife.')
    root.destroy()


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
                        but you have a better lover.''')
    root.destroy()


def mugger_choice():
    clear_window()
    display_cookies()
    # oh_fuck_button.destroy()
    place_bottom_left(fight_mugger_button)
    place_bottom_right(Button(root, text=f'Give him your {confectionary}s', command=surrender_cookies, width=20, height=3),
                       100)


def fight_setup():
    clear_window()
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
    global number_of_cookies
    global patched_up
    if number_of_cookies <= 0:
        you_die()
        return
    number_of_cookies -= 1
    display_cookies()
    if not patched_up:
        root.after(70, fight_mugger)
    else:
        messagebox.showinfo(message=f'''Congratulations, you've won. You have {number_of_cookies} {confectionary}s.
    Unfortunately the mugger is sleeping with your wife.''')
        root.destroy()


def clear_window():
    for widget in root.winfo_children():
        widget.pack_forget()
        widget.place_forget()


def you_die():
    clear_window()
    place_top_left(Label(text=f'''You lost all your {confectionary}s. You're dead.
    Yes it makes sense.'''))
    game_over_button.place(x=350, y=150)


def start_game(start_cookies):
    global number_of_cookies
    number_of_cookies = start_cookies
    clear_window()
    display_cookies()
    place_bottom_right(get_cookie_button, 0)
    place_top_left(cookie_count_label)
    # cookie_count_label.place(x=50, y=50)


def no_cookie():
    clear_window()
    place_center(Label(text='''Sucks 2 b u lol'''))


def end_game():
    root.destroy()


# I don't like cookies
no_cookies_button = Button(root, text='I don\'t like cookies', height=3, width=25, command=dont_like_cookies)
confectionary = 'cookie'
likes_cookies = True

# Setup
number_of_cookies = 0
get_cookie_button = Button(root, text='Click Me', height=3, width=10, command=add_cookies)
cookie_count_label = Label(root, text=f'Number of {confectionary}: {number_of_cookies}')
start_game(0)  # <---- Number of cookies to start with

# Switcheroo Stuff
gotcha_label = Label(root, text='gotcha')
switcheroo_number = random.randrange(31, 39)
crafty = False
has_switcherood = False
drop_10_button = Button(root, text=f'Drop 10 {confectionary}s', height=3, width=16, command=drop_10_cookies)
drop_20_button = Button(root, text=f'Drop 20 {confectionary}s', height=3, width=16, command=drop_20_cookies)

# Death stuff
game_over_button = Button(root, text='I\'m an idiot', height=3, width=16, command=end_game)
# placeCenter(game_over_button)

# Mugging Stuff
mugger_label = Label(root, text='Oh no, a mugger!!')
oh_fuck_button = Button(root, text='balls', height=3, width=10, command=mugger_choice)
# surrender_cookies_button = Button(root, text=f'Give him your {confectionary}s', command=surrenderCookies, width=20, height=3)

# Fight mugger Stuff
fight_mugger_button = Button(root, text='Fight', command=fight_setup, width=7, height=3)
won_fight_label = Label(root, text=f'''You managed to fend him off but he stabbed you
You're leaking {confectionary}s''')
bleed_severity = 5
bleed_count = 0
patch_up_button = Button(root, text='Plug the bleed', command=patch_yourself_up)
patched_up = False

# Dog stuff
yes_baby_button = Button(text='Yes baby!', width=10, height=3, command=yes_baby)
kinky_clicks = 0

root.mainloop()
