from tkinter import Tk, Label
import tkinter as tk

def start_main_window():
    from main import Game
    root = Tk()
    root.geometry(f'1024x1024+700+300')
    root.resizable(False, False)
    root.attributes('-topmost', 1)

    welcome_image = tk.PhotoImage(file='img/Cookie-Clicker.png')
    img_label = tk.Label(root, image=welcome_image)

    start_frame = tk.Frame(root, background='black')
    start_button = tk.Button(start_frame, width=8, height=3, background='lightgrey', text='START',
                                  font=('Terminal', 20), command=lambda: Game().start())
    start_button.pack(padx=4, pady=4)

    exit_frame = tk.Frame(root, background='black')
    exit_button = tk.Button(exit_frame, width=8, height=3, background='lightgrey', text='EXIT',
                                 font=('Terminal', 20), command=root.destroy)
    exit_button.pack(padx=4, pady=4)

    img_label.pack()
    start_frame.place(x=580, y=850)
    exit_frame.place(x=300, y=850)
    root.mainloop()


class GameUI:
    width = 650
    height = 450

    left = 50
    top = 50
    bottom = height - 150
    right = width - 150

    def __init__(self, game):
        self.game = game
        self.window = tk.Toplevel()
        self.window.title('Jonty\'s Sweet Cookie Clicker')
        self.window.geometry(f'{self.width}x{self.height}+700+300')
        self.window.resizable(False, False)
        self.window.attributes('-topmost', 1)

        self.b_click_me = tk.Button(self.window, text='Click Me', height=3, width=10, command=game.get_cookie)
        self.b_end_game = tk.Button(self.window, text='I\'m an idiot', height=3, width=16, command=game.end)

    def l_cookie_count(self):
        return Label(self.window, text=self.game.counter.count_info())

    def b_drop_10(self):
        return tk.Button(self.game.ui.window, text=f'Drop 10 {self.game.counter.item_type}s', height=3, width=16,
                         command=lambda: self.game.lose_cookie(10))

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.pack_forget()
            widget.place_forget()

    def reset_layout(self):
        self.clear_window()
        self.display_cookies()

    def display_cookies(self):
        place_top_left(self.l_cookie_count())

    def display_click_me_button(self):
        place_bottom_right(self.b_click_me)


def place_bottom_right(ui_element, x_offset = 0):
    ui_element.place(x=480 - x_offset, y=300)


def place_bottom_left(ui_element):
    ui_element.place(x=50, y=300)


def place_center(ui_element):
    ui_element.place(x=100, y=150)


def place_top_left(ui_element):
    ui_element.place(x=50, y=50)


def place_top_right(ui_element):
    ui_element.place(x=270, y=50)

