class Counter:
    def __init__(self, game):
        self.game = game
        self.item_type = 'cookie'
        self.count = 0

    def count_info(self):
        #TODO Spaces added here to stop overlapping. Fix?
        return f'Number of {self.item_type}s: {self.count}         '

    def item(self):
        return self.item_type if (self.count == 1) else f'{self.item_type}s'

    def add_item(self, num=1):
        self.count += num
        self.game.ui.display_cookies()

    def remove_item(self, num=1):
        self.count -= num
        self.game.ui.display_cookies()
