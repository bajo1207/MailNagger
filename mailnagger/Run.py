import tkinter as tk

from mailnagger.message_service import create_message, send_message
from mailnagger.quickstart import create_google_service


def create_and_send():
    google_service = create_google_service()
    message = create_message('ewewewe.com', 'birger@intility.no', 'Teeest', 'Hei')
    send_message(google_service, "me", message)


window = tk.Tk(className='MailNagger')
window.geometry("500x200")
frame = tk.Frame(window)
frame.pack()
greeting = tk.Label(text="Hello Big T")
greeting.pack()
slogan = tk.Button(frame,
                   text="Send Mail",
                   command=create_and_send)
slogan.pack()
window.mainloop()
