from tkinter import *
from tkinter import messagebox
import random


class GUI(Frame):
    min = 0
    max = 1
    number = 0
    attempts = []
    root = ''
    frame = ''

    def __init__(self, _frame):
        """
        Initialize GUI
        :param _frame: window
        """
        Frame.__init__(self, _frame)
        self.root = _frame
        self.build_GUI()

    def make_a_number(self):
        """
        Make a number for guessing
        min and max limits sets as class variables
        :return: none
        """
        self.number = random.randint(self.min, self.max)

    def reset(self):
        """
        Reset guessing num and attempts
        :return: none
        """

        self.number = 0
        self.attempts = []
        self.text_form.pack_forget()
        self.submit_button.pack_forget()
        self.build_GUI()

    def check_answer(self):
        """
        Check what user type in the form
        :return:
        """
        text = self.text_form.get()
        try:
            if int(text) != self.number:
                messagebox.showinfo("", "Not guess:)")
                self.attempts.append(int(text))
            else:
                answer = messagebox.askokcancel("", f"Hurray! You won!. Attempts: {self.attempts}")
                if answer == 'yes':
                    self.root.destroy()
                else:
                    self.reset()

        except ValueError:
            messagebox.showerror("", "Invalid string. Please correct")

    def build_GUI(self):
        self.make_a_number()
        self.frame = Frame()
        frame = self.frame
        title = Label(frame, text='Guessing game', font=16)
        subtitle = Label(frame,
                         text=f"I made a number from {self.min} to {self.max}. Your goal is to guess it. Let's Go!", )

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        title.pack()
        subtitle.pack()

        self.build_start_button(frame)

    def start_play_gui(self):
        self.start_button.pack_forget()
        text_form = Entry(self.frame, justify=CENTER)
        self.text_form = text_form
        submit_button = Button(self.frame, text="Submit!", width=15, height=1, bg='grey', fg='white')
        self.submit_button = submit_button
        submit_button.config(command=self.check_answer)
        padding = Label(self.frame, height=1, width=1)

        text_form.pack()
        padding.pack()
        submit_button.pack()

    def build_start_button(self, frame):

        button = Button(frame, text="Start!", width=15, height=3, bg='grey', fg='white')
        self.start_button = button
        button.config(command=self.start_play_gui)
        padding = Label(frame, height=3, width=10)
        padding.pack()
        button.pack()


def main():
    root = Tk()
    root.geometry('500x400')
    root.title = "Guessing game"
    app = GUI(root)
    root.mainloop()


main()
