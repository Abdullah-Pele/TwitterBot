import tkinter as t
from tkinter import *
import tweepy
import Methods_Twitter as mt
import threading

# f=open("keys.txt", "w")
lines =  open("keys.txt").read().split('\n')

consumer_key = lines[0]
consumer_secret = lines[1]

access_token = lines[2]
access_token_secret = lines[3]

#
# f.write(consumer_key+"\n")
# f.write(consumer_secret+"\n")
# f.write(access_token+"\n")
# f.write(access_token_secret+"\n")

# f.write(consumer_key)
# f.write(consumer_secret)
# f.write(access_token)
# f.write(access_token_secret)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)



def act():
    N = nam.get()
    Value = str(var.get())
    Seconds= sec.get()
    fo = str(Followers_or_Following.get())
    s = "Working..."
    labell.config(text=s)
    Seconds_value = int(sec.get())
    numbpp = int(number.get())

    if var.get() == 1:
        if Followers_or_Following.get() == 1:
            mt.follow_followers(api, Seconds_value, numbpp, N)
        else:
            mt.follow_friends(api, Seconds_value, numbpp, N)
    else:
        if Followers_or_Following.get() == 1:
            mt.unfollow_followers(api, Seconds_value, numbpp, N)
        else:
            mt.unfollow_friends(api, Seconds_value, numbpp, N)
    labell.config(text="Working Done!")



def unfollow_badppl():
    s="Working..."
    labell.config(text=s)
    mt.unfollow_enemies(api, int(sec.get()), int(number.get()) )
    labell.config(text="Working Done!")

def thread_act():
    threading.Thread(target=act).start()
def thread_un():
    threading.Thread(target=unfollow_badppl).start()

    # if Followers_or_Following == "1":
    #     if var.get() == 1:
    #         x = mt.follow_followers(api, int(sec.get()), int(number.get())-1, nam.get())
    #         labell.config(text = "the action done to "+ str(x))
    #     else:
    #         x = mt.unfollow_followers(api, int(sec.get()), int(number.get())-1, nam.get())
    #         labell.config(text = "the action done to "+ str(x))
    # else:
    #     if var.get() == 1:
    #         x = mt.follow_friends(api, int(sec.get()), int(number.get())-1, nam.get())
    #         labell.config(text = "the action done to "+ str(x))
    #     else:
    #         x = mt.unfollow_friends(api, int(sec.get()), int(number.get())-1, nam.get())
    #         labell.config(text = "the action done to "+ str(x))

'''
def gettt():
    consumer_key = E1.get()
    consumer_secret = E2.get()
    access_token = E3.get()
    access_token_secret = E4.get()
    global api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    ap = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

    try:
        tweets = ap.user_timeline(screen_name = "NiceGuy84882994",count = 1)
        # MsgBox = t.messagebox.askquestion('Save', 'do you want to save the values',
        #                                   icon='warning')
        enter_window.destroy()
        #make root visible again
        api = ap
        # file = open("Config", "w")
        # file.write(consumer_key)
        # file.write(consumer_secret)
        # file.write(access_token)
        # file.write(access_token_secret)
        # file.close()
        root.iconify()
        root.deiconify()
    except tweepy.error.TweepError as e:
        messagebox.showinfo("Worng values", "Some of the values are falses, Try again", icon='warning')
        E1.delete(0, t.END)
        E2.delete(0, t.END)
        E3.delete(0, t.END)
        E4.delete(0, t.END)
'''


root = t.Tk()
#root.withdraw()
root.geometry("500x500")
root.title("Bot followback")

name  = t.Label(text= "Choose the name ")
name.pack(anchor = W)

nam = Entry(root, bd =5, width=30)
nam.pack(anchor = W)
nam.insert(1,"example")
action = Label(root, text="Choose Action:")
action.pack(anchor=W)

var = IntVar()
R1 = Radiobutton(root, text="Follow", variable=var, value=1)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="UNFollow", variable=var, value=2)
R2.pack( anchor = W )

R1.select()

target = Label(text= "Choose Target:")
target.pack(anchor = W)
Followers_or_Following = IntVar()
followers = Radiobutton(root, text= "Follwers", variable=Followers_or_Following, value=1 )
followers.pack(anchor = W)


following = Radiobutton(root, text= "Following", variable=Followers_or_Following, value=2)
following.pack(anchor = W)
followers.select()
seconds = Label(text= "Choose Seconds:")
seconds.pack(anchor = W)

sec = Entry(root, bd =5)
sec.pack(anchor = W)
sec.insert(1,"30")



num = Label(text= "Choose Number:")
num.pack(anchor = W)
number = Entry(root, bd=5)
number.pack(anchor = W)
number.insert(1,"12")

startbt = Button(root, text='Start', width=30, command=thread_act)
startbt.pack(anchor = W)

unfollow_bad = Button(root,text="UNFollow Enemies", width=30, bg="blue",fg="white", command=thread_un)
unfollow_bad.pack(anchor = W)
#
# stop = Button(root, text='stop', width=30, bg="red")
# stop.pack(anchor = W)

labell= Label(root)
labell.pack(anchor = W)

'''
enter_window = t.Toplevel(root)

enter_window.geometry("500x500")
# enter_window.withdraw()


enter_window.title("Bot followback")

consumer_key = t.Label(enter_window, text= "Consumer Key: ").pack(anchor = t.W)
E1 = t.Entry(enter_window, bd = 5, width=40)
E1.pack(anchor = t.W)

consumer_secret = t.Label(enter_window, text= "Consumer Secret: ").pack(anchor = t.W)
E2 = t.Entry(enter_window, bd =5, width=40)
E2.pack(anchor = t.W)

access_token = t.Label(enter_window, text= "Access Token: ").pack(anchor = t.W)
E3 = t.Entry(enter_window, bd =5, width=40)
E3.pack(anchor = t.W)

access_token_secret = t.Label(enter_window, text= "Access Token Secret: ").pack(anchor = t.W)
E4 = t.Entry(enter_window, bd =5, width=40)
E4.pack(anchor = t.W)

# root = t.Tk()
# E1 = t.Entry(root, bd =5).grid(row = 4, column = 3)


t.Button(enter_window, text='Enter', command= gettt).pack(anchor = t.W)
t.Button(enter_window, text='Quit ', command= enter_window.quit).pack(anchor = t.W)


enter_window.mainloop()

'''
root.mainloop()
