from counter import Counter
from gameui import *
from event_manager import EventManager


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