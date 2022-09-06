from tkinter import *
from main import tw_post_text, tw_post_media_text, tw_reply

root = Tk()

# starting window size;
root.geometry('350x300+250+250')
root.title('Social Bot')

# social bot, main label; #static
Label(root, text="Social Bot", bg="#2b536a", fg="#a9beca").place(x=140, y=0)
Label(root, text="All rights reserved.", bg="#2b536a", fg="#a9beca").place(x=115, y=260)
Label(root, text="Powered by anaconda1337", bg="#2b536a", fg="#a9beca").place(x=90, y=280)

text = 'rere'

button = Button(root,
                text='Post text',)
                # command=tw_post_text(text))
button.pack()

root.mainloop()