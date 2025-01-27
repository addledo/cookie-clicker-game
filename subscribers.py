from event import Switcheroo

subscribers = dict()

def subscribe(event_type: str, fn):
    if not event_type in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(fn)
    print(f'Subscribing: {event_type} - {fn}')

def unsubscribe(event_type, fn=None):
    if event_type in subscribers:
        if fn is None:
            subscribers[event_type].clear()
            print(f'Unsubscribing all: {event_type}')
        if fn in subscribers[event_type]:
            subscribers[event_type].remove(fn)
            print(f'Unsubscribing: {event_type} - {fn}')
    else:
        print('No such subscribed function')


def post_event(event_type: str):
    if not event_type in subscribers:
        return "FAIL"
    for fn in subscribers[event_type]:
        fn()
        return "SUCCESS"

