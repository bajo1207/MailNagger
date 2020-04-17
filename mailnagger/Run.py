import os.path
from tkinter import *
from tkinter.font import Font

from urllib3.connectionpool import xrange

from mailnagger.message_service import create_message, send_message
from mailnagger.quickstart import create_google_service


def create_and_send():
    google_service = create_google_service()
    message = create_message('ewewewe.com', 'joachimbm96@gmail.com', 'Teeest', 'Hei')
    send_message(google_service, "me", message)


def waithere():
    var = IntVar()
    root.after(1000, var.set, 1)
    root.wait_variable(var)


class MailNaggerGUI:
    def __init__(self, master):
        self.fontStyle = Font(family="Lucida Grande", size=20)
        self.master = master
        master.geometry("370x200")
        master.title("MailNagger")

        if not os.path.exists('token.pickle'):
            self.label1 = Label(master, text="Welcome to MailNagger", font=self.fontStyle)

            self.label1.pack()
            self.label = Label(master, text="")
            self.label.pack()
            for i in xrange(5, -1, -1):
                self.label['text'] = f"You will be prompted to login to your google account in {i}s"
                waithere()
            self.google_service = create_google_service()
            self.label.destroy()
            self.label1.destroy()

        self.greet_button = Button(master, text="Greet")
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()


root = Tk()
my_gui = MailNaggerGUI(root)
root.mainloop()
