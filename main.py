import random
import tkinter as tk
from tkinter import Label, messagebox, Tk
from place import *

class Counter:
    def __init__(self):
        self.item_type = 'cookie'

        self.count = 0

    def count_info(self):
        return f'Number of {self.item_type}s: {self.count}'

    def item(self):
        return self.item_type if (self.count == 1) else f'{self.item_type}s'

    def add_item(self, num=1):
        self.count += num

    def remove_item(self, num=1):
        self.count -= num


class Player:
    def __init__(self, game):
        self.game = game
        self.health = 100

    def die(self):
        self.health = 0
        game.ui.clear_window()
        death_message = Label(text=f'''You lost all your {game.counter.item_type}s. You're dead.''')
        place_top_left(death_message)
        b_end_game.place(x=350, y=150)


class GameUI:
    width = 650
    height = 450

    left = 50
    top = 50
    bottom = height - 150
    right = width - 150

    def __init__(self):
        self.window = Tk()
        self.window.title('Jonty\'s Sweet Cookie Clicker')
        self.window.geometry(f'{self.width}x{self.height}+700+300')
        self.window.resizable(False, False)
        self.window.attributes('-topmost', 1)

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.pack_forget()
            widget.place_forget()

    # Buttons
    # def button_change_to_eggs(self):
    #     return tk.Button(self.window, text='I don\'t like cookies', height=3, width=25, command=change_to_eggs)


class Game:
    def __init__(self):
        self.counter = Counter()
        self.ui = GameUI()

class Events:
    def __init__(self, game):
        self.game = game



# FIXES BLURRY TEXT ON WINDOWS -----------------
# from ctypes import windll
# windll.shcore.SetProcessDpiAwareness(1)


def main():
    print("MAIN METHOD")

def display_cookies():
    place_top_left(l_cookie_count())


def add_cookie():
    game.counter.count += 1
    # game.trigger_event()
    global crafty
    if crafty:
        Label(text='You\'re a crafty one aren\'t you').place(x=60, y=240)
    crafty = False
    encouraging_messages()
    check_change_to_eggs()

    global switcheroo_threshold
    if game.counter.count == switcheroo_threshold:
        ol_switcheroo()
    if game.counter.count == 89:
        switch_back()
    if game.counter.count == 100:
        get_mugged()


def encouraging_messages():
    display_text = f'Number of {game.counter.item_type}s: {game.counter.count}'
    if 10 < game.counter.count < 20:
        display_text += '           Keep going!'
    if 30 < game.counter.count < 40:
        display_text += f'           So many {game.counter.item_type}s!'
    if game.counter.count == 69:
        display_text += '            Nice.'
    if 80 < game.counter.count < 90:
        display_text += '           Things seem very peaceful.'
    # l_cookie_count().place(x=game.ui.top, y=game.ui.left)
    place_top_left(l_cookie_count())


def check_change_to_eggs():
    b_change_to_eggs = tk.Button(game.ui.window, text='I don\'t like cookies', height=3, width=25,
                                 command=change_to_eggs)

    if game.counter.count == 5:
        b_change_to_eggs.place(x=100, y=150)

    if game.counter.count > 8 or game.counter.item_type == 'egg':
        b_change_to_eggs.place_forget()


def change_to_eggs():
    game.counter.item_type = 'egg'
    reset_layout()
    place_bottom_right(b_click_me)

def drop_cookies(num):
    game.counter.count -= num
    display_cookies()
    if game.counter.count < 0:
        player_dies()
    global crafty
    crafty = False


def ol_switcheroo():
    global has_switcherood
    if has_switcherood:
        return
    reset_layout()
    place_bottom_left(b_click_me)
    place_bottom_right(b_drop_10(), 50)
    global crafty
    has_switcherood = True
    crafty = True
    Label(game.ui.window, text='gotcha').place(x=50, y=270)


def switch_back():
    reset_layout()
    place_bottom_right(b_click_me, 50)
    place_bottom_left(b_drop_20())


def get_mugged():
    reset_layout()
    Label(game.ui.window, text='Oh no, a mugger!!').place(x=300, y=80)
    tk.Button(game.ui.window, text='balls', height=3, width=10, command=mugger_choice).place(x=300, y=250)


def surrender_cookies():
    game.ui.clear_window()
    game.counter.count = 1
    display_cookies()
    Label(text=f'''The mugger takes pity on you and lets you keep 1 {game.counter.item_type}.
    
    
As he leaves, a stray dog appears and locks eyes
onto your one remaining {game.counter.item_type}.''').place(x=50, y=100)
    place_bottom_left(tk.Button(text='Punt the dog', width=12, height=2, command=punt_dog))
    place_bottom_right(tk.Button(text='Run', width=10, height=2, command=run_from_dog), 0)


def run_from_dog():
    reset_layout()
    Label(text='''Good choice. As you run, you see the mugger up ahead.
He thinks your chasing him. As you get close he stabs you.
(It's self defence)''').place(y=100, x=50)
    place_bottom_right(b_end_game, 250)


def punt_dog():
    reset_layout()
    # Random boolean?
    punt_successful = random.choice([True, False])
    if not punt_successful:
        Label(text='''First off you're a terrible person. Secondly it's a very big dog.
    It tackles you to the ground and bites on to your throat''').place(x=50, y=100)
        place_bottom_right(tk.Button(text='Oh no', width=10, height=3, command=death_by_dog), 100)
        place_bottom_left(yes_baby_button)
    else:
        Label(text='''Against all odds you successfully punt the dog off a nearby cliff.
You're alive but you just killed a dog. Good job.''').place(x=50, y=100)
    place_bottom_right(tk.Button(text='Oh no', width=10, height=3, command=game.ui.window.destroy), 100)


def death_by_dog():
    reset_layout()
    messagebox.showinfo(message='''Just as the dog is about to finish you off,
the mugger charges in, barreling into the dog
and knocking it unconscious.
Then he disappears into the distance without a word.
Maybe he's not such a bad guy after all''')
    place_bottom_right(tk.Button(text='Go home', height=3, width=8, command=go_home), 200)


def go_home():
    reset_layout()
    messagebox.showinfo(message='You get home and find the mugger with your wife.')
    game.ui.window.destroy()


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
    game.ui.window.destroy()


def mugger_choice():
    reset_layout()
    b_fight_mugger = tk.Button(game.ui.window, text='Fight', command=fight_setup, width=7, height=3)
    surrender_prompt = f'Give him your {game.counter.item_type}s'
    b_surrender = tk.Button(game.ui.window, text=surrender_prompt, command=surrender_cookies, width=20, height=3)

    place_bottom_left(b_fight_mugger)
    place_bottom_right(b_surrender, 100)


def fight_setup():
    reset_layout()
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
    if game.counter.count <= 0:
        player_dies()
        return
    game.counter.count -= 1
    display_cookies()
    if not patched_up:
        game.ui.window.after(70, fight_mugger)
    else:
        messagebox.showinfo(
            message=f'''Congratulations, you've won. You have {game.counter.count} {game.counter.item_type}s.
    Unfortunately the mugger is sleeping with your wife.''')
        game.ui.window.destroy()


def player_dies():
    game.ui.clear_window()
    label = Label(text=f'''You lost all your {game.counter.item_type}s. You're dead.''')
    place_top_left(label)
    b_end_game.place(x=350, y=150)


def reset_layout():
    game.ui.clear_window()
    display_cookies()


def end_game():
    game.ui.window.destroy()


game = Game()
game.counter.count = 15

# Buttons
b_click_me = tk.Button(game.ui.window, text='Click Me', height=3, width=10, command=add_cookie)
b_end_game = tk.Button(game.ui.window, text='I\'m an idiot', height=3, width=16, command=end_game)

def b_drop_10():
    return tk.Button(game.ui.window, text=f'Drop 10 {game.counter.item_type}s', height=3, width=16,
                     command=lambda: drop_cookies(10))

def b_drop_20():
    return tk.Button(game.ui.window, text=f'Drop 20 {game.counter.item_type}s', height=3, width=16,
                     command=lambda: drop_cookies(20))


# Labels
def l_cookie_count():
    return Label(game.ui.window, text=game.counter.count_info())


# START GAME
reset_layout()
place_bottom_right(b_click_me)

# Switcheroo Stuff
switcheroo_threshold = random.randrange(31, 39)
crafty = False
has_switcherood = False

# Fight mugger Stuff
won_fight_label = Label(game.ui.window, text=f'''You managed to fend him off but he stabbed you
You're leaking {game.counter.item_type}s''')
bleed_severity = 5
bleed_count = 0
patch_up_button = tk.Button(game.ui.window, text='Plug the bleed', command=patch_yourself_up)
patched_up = False

# Dog stuff
yes_baby_button = tk.Button(text='Yes baby!', width=10, height=3, command=yes_baby)
kinky_clicks = 0

game.ui.window.mainloop()