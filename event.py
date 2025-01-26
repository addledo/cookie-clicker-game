from abc import abstractmethod, ABC
from gameui import *


class Event(ABC):
    def __init__(self, game):
        self.game = game

    @abstractmethod
    def trigger(self):
        pass


class Switcheroo(Event):
    def trigger(self):
        self.game.ui.reset_layout()
        place_bottom_left(self.game.ui.b_click_me)
        place_bottom_right(self.game.ui.b_drop_10(), 50)
        self.game.event_manager.occurred_switcheroo = True
        Label(self.game.ui.window, text='gotcha').place(x=50, y=270)


class EggChange(Event):
    def trigger(self):
        button = tk.Button(self.game.ui.window, text='I don\'t like cookies', height=3, width=25, command=self.__change_to_eggs)

        if self.game.counter.count == 5:
            button.place(x=100, y=150)

        if self.game.counter.count > 8 or self.game.counter.item_type == 'egg':
            button.place_forget()

    def __change_to_eggs(self):
        self.game.counter.item_type = 'egg'
        self.game.ui.display_cookies()
