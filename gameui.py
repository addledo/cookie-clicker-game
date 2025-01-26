from tkinter import Tk, Button, Label
# import main
# from main import counter
# from place import *


# from main import drop_cookies, counter, game


class GameUI:

    def __init__(self):
        self.window = Tk()
        self.window.title('Jonty\'s Sweet Cookie Clicker')
        self.window.geometry('650x450+700+300')
        self.window.resizable(False, False)
        self.window.attributes('-topmost', 1)

        # self.label_item_count = Label(self.window, text=counter.count_info())

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.pack_forget()
            widget.place_forget()

    # def display_cookies(self):
    #     self.label_item_count.configure(text=counter.count_info())
    #     place_top_left(self.label_item_count)

    # def update_cookie_info(self):
    #     display_text = f'Number of {counter.item_type}s: {counter.count}'
    #     if 10 < counter.count < 20:
    #         display_text += '           Keep going!'
    #     if 30 < counter.count < 40:
    #         display_text += f'           So many {counter.item_type}s!'
    #     if counter.count == 69:
    #         display_text += '            Nice.'
    #     if 80 < counter.count < 90:
    #         display_text += '           Things seem very peaceful.'
    #     label_cookie_count.configure(text=display_text)
    #     place_top_left(label_cookie_count)



# from main import counter, gameUI
# #TODO Implement
# class Buttons:
#     drop_10 = Button(gameUI.window, text=f'Drop 10 {counter.item_type}s', height=3, width=16, command="drop_cookies(10)")
#     drop_20 = Button(gameUI.window, text=f'Drop 20 {counter.item_type}s', height=3, width=16, command="drop_cookies(20)")