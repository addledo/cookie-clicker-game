from event import Switcheroo

class SubManager:
    def __init__(self):
        self.subscribers = dict()

    def subscribe(self, event_type: str, fn):
        if not event_type in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(fn)
        print(f'Subscribing: {event_type} - {fn}')

    def unsubscribe(self, event_type, fn=None):
        if event_type in self.subscribers:
            if fn is None:
                self.subscribers[event_type].clear()
                print(f'Unsubscribing all: {event_type}')
            if fn in self.subscribers[event_type]:
                self.subscribers[event_type].remove(fn)
                print(f'Unsubscribing: {event_type} - {fn}')
        else:
            print('No such subscribed function')


    def post_event(self, event_type: str):
        if not event_type in self.subscribers:
            return "FAIL"
        for fn in self.subscribers[event_type]:
            fn()
            return "SUCCESS"

