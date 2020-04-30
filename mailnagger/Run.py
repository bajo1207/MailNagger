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


def create_mail_line(mail):
    return


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

            self.label2 = Label(master, text="")
            self.label2.pack()
            for i in xrange(5, -1, -1):
                self.label2['text'] = f"You will be prompted to login to your google account in {i}s"
                waithere()
            self.google_service = create_google_service()
            self.label2.destroy()
            self.label1.destroy()
        self.w = Frame(master, bg="#2F5597", height=200, width=100)
        self.w.pack(side=LEFT, fill=BOTH)
        self.close_button = Button(self.w, text="Close", bg="#2F5597", command=master.quit)
        self.close_button.pack(side=BOTTOM)

        self.mailline = Frame(master, height=50, highlightbackground="black", highlightthickness=1)
        self.mailline.pack(side=TOP)


root = Tk()
my_gui = MailNaggerGUI(root)
root.mainloop()
