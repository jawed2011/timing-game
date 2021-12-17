#idea!
#                                *cycles through 1234567890*
#                    |-------------------------|
#                    |         choose          |
#                    |                         |                                     (randomly picked number)
#                    |-------------------------|
import tkinter as tk
import random
import time
isBtnClicked = False
isBtnClick = False
lives = 3
huhu= int(input("Enter easiness (1-10) : "))
root = tk.Tk()
r=random.randrange(0,9,1)
root.geometry("300x300")

rgn=tk.Label(text=r,bg="blue",fg="white",cursor="dot")
rgn.pack()
your_label=tk.Label(text=0,cursor="dot",bg="yellow")
your_label.pack()
# def livecheck():
#
#  while True:
#     if isBtnClicked == True:
#
#
#
#

def pick():
   global lives
   isBtnClicked = True
   lives = lives - 1
   tries["text"] = lives
   root.update()
   if lives == 0:
      print ("You lost :( !!")
      root.destroy()
   if r == your_label["text"]:
      print("You Won!!!")

def update_label():
   isBtnClicked = True
   i = 0
   while True:
      i = i + 1
      if i == 10: i = 0
      your_label["text"] = i
      root.update()
      time.sleep(huhu / 10)
      if isBtnClicked == True:
         star_button["state"] = "active"

start_button=tk.Button(root,text="Start Game",command=update_label,cursor="dot",bg="blue",fg="white",border=1)
start_button.pack()
star_button=tk.Button(root,text="Pick",command=pick,bg="red",fg="white",cursor="dot",state="disabled")
star_button.pack()
tries=tk.Label(root, text=3)
tries.pack()

root.mainloop()