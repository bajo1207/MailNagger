import tkinter as tk

from mailnagger.message_service import create_message, send_message
from mailnagger.quickstart import GoogleAuth


def create_and_send():
    google_service = GoogleAuth()
    message = create_message('ewewewe.com', 'joachimbm96@gmail.com', 'Teeest', 'penis')
    send_message(google_service.service, "me", message)


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
