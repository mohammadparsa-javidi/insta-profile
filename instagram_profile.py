from tkinter import *
import io
from urllib.request import urlopen
from PIL import Image,ImageTk
import instaloader
win = Tk()
win.geometry("500x500")

def show_profiles():
    
        # get user
        user_name = user_entry.get()
        # get insta account
        insta = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(insta.context,user_name)
        # open,read,and close url
        open_url = urlopen(profile.get_profile_pic_url())
        read_url = open_url.read()
        open_url.close() 
        # open image and config in window
        image = Image.open(io.BytesIO(read_url))
        pic = ImageTk.PhotoImage(image)
        pic_label.config(image=pic)
        pic_label.image = pic
    
user_label = Label(win,text="Enter user name:",font=(10))
user_label.pack()

# Entry for write user name
user_entry = Entry(win,width=30,bd=5)
user_entry.pack(pady=10)

# Button for show profiles
btn_profile = Button(win,text="Show profile",font=(5),command=show_profiles)
btn_profile.pack(pady=10)
pic_label = Label(win,text="")
pic_label.pack()
win.mainloop()