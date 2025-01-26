from gameui import GameUI
from counter import Counter
import gameui, counter

class Game:
    def __init__(self):
        self.counter = Counter()
        self.ui = GameUI()