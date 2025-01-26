import random
from counter import Counter
from event import Switcheroo, EggChange
from gameui import *


class EventManager:
    def __init__(self, game):
        self.game = game

        # self.switcheroo_threshold = random.randrange(31, 39)
        self.switcheroo_threshold = 30
        self.occurred_switcheroo = False

        self.occurred_mugging = False

    def trigger(self):
        if self.game.counter.count == 5:
            EggChange(self.game).trigger()
        if self.game.counter.count == 10:
            self.game.ui.reset_layout()
            self.game.ui.display_click_me_button()
        if self.game.counter.count == self.switcheroo_threshold:
            Switcheroo(self.game).trigger()



    def change_to_eggs(self):
        self.game.counter.item_type = 'egg'
        self.game.ui.reset_layout()
        place_bottom_right(self.game.ui.b_click_me)


class Game:
    def __init__(self):
        self.counter = Counter(self)
        self.ui = GameUI(self)
        self.event_manager = EventManager(self)

    def start(self):
        self.ui.reset_layout()
        place_bottom_right(self.ui.b_click_me)
        self.ui.window.mainloop()

    def end(self):
        self.ui.window.destroy()

    def get_cookie(self):
        self.counter.add_item(1)
        self.event_manager.trigger()

    def lose_cookie(self, num=1):
        self.counter.remove_item(num)
        if self.counter.count < 0:
            self.player_dies()

    def player_dies(self):
        self.ui.clear_window()
        death_message = Label(text=f'''You lost all your {self.counter.item_type}s. You're dead.''')
        place_top_left(death_message)
        self.ui.b_end_game.place(x=350, y=150)



def main():
    game = Game()
    game.counter.count = 0
    game.start()

if __name__ == "__main__": main()