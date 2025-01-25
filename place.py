def place_bottom_right(thing, adjust):
    thing.place(x=480 - adjust, y=300)


def place_bottom_left(thing):
    thing.place(x=50, y=300)


def place_center(thing):
    thing.place(x=100, y=150)


def place_top_left(thing):
    thing.place(x=50, y=50)


def place_top_right(thing):
    thing.place(x=270, y=50)

def clear_window(window):
    for widget in window.winfo_children():
        widget.pack_forget()
        widget.place_forget()
