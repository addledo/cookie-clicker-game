from event import *
from sub_manager import *

class EventManager:
    def __init__(self, game):
        self.game = game
        self.sub_manager = SubManager()

        # Events
        self.switcheroo = Switcheroo(self.game)
        self.egg_change = EggChange(self.game)

        # Event subscribers
        self.sub_manager.subscribe('switcheroo_threshold_reached', self.switcheroo.trigger)
        self.sub_manager.subscribe('egg_change_threshold_reached', self.egg_change.trigger)

        # Event trigger thresholds
        self.egg_change_threshold = 5
        self.switcheroo_threshold = 30

    def trigger(self):
        if self.game.counter.count == self.switcheroo_threshold:
            if self.sub_manager.post_event('switcheroo_threshold_reached') == 'SUCCESS':
                self.sub_manager.unsubscribe('switcheroo_threshold_reached')

        if self.game.counter.count == self.egg_change_threshold:
            if self.sub_manager.post_event('egg_change_threshold_reached') == 'SUCCESS':
                self.sub_manager.unsubscribe('egg_change_threshold_reached')
