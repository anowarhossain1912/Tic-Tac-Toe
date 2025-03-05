from tkinter import *
import random 
def newgame():
    global player
    player=random.choice(players)
    label.config(text=player +" ""turn")

    for row in range(3):
        for col in range(3):
            button[row][col].config(text="")  
   
def next_turn(row,col):
    global player
    if button[row][col]["text"]=="" and check_winer() is False:
       if player==players[0]:
          button[row][col]["text"]=player

          if check_winer() is False:
             player=players[1]
             label.config(text=player+ " " "turn")
          elif check_winer() is True:
             label.config(text=players[0]+" ""wins!!") 
          elif check_winer()=="Tie":
             label.config(text="TIE")
       else:
          button[row][col]["text"]=player

          if check_winer() is False:
             player=players[0]
             label.config(text=player+ " " "turn")
          elif check_winer() is True:
             label.config(text=players[1]+" " "wins!!") 
          elif check_winer()=="Tie":
             label.config(text="TIE")

def check_winer():
   for row in range(3):
      if button[row][0]["text"]==button[row][1]["text"]==button[row][2]["text"]!="":
         return True
   for col in range(3):
      if button[0][col]["text"]==button[1][col]["text"]==button[2][col]["text"]!="":
         return True 
   if button[0][0]["text"]==button[1][1]["text"]==button[2][2]["text"]!="":
      return True
   if button[0][2]["text"]==button[1][1]["text"]==button[2][0]["text"]!="":
      return True
   elif fillup() is False:
      return "Tie"
   else:
      return False  
def fillup():
   space=9
   for row in range(3):
      for col in range(3):
         if button[row][col]["text"]!="":
            space-=1

   if space== 0:
      return False
   else:
      return True  
# Initialization
if __name__ == "__main__":
  
  screen=Tk()
  screen.title("Tic-Tac-Toe")
  players=["x","o"]    # player name create
  player=random.choice(players)  # player choice
  button=[[0,0,0],
        [0,0,0],    # 
        [0,0,0]]
  label=Label(text=player +" " "turn",font=("consolas",40)) #display te ki6u lekhar jnno
  label.pack(side=TOP)  # pack na korle tk function ar kono ki6u e display te show korbe na
  restartButton=Button(text="Restart",font=("arial",15),command=newgame)  # button create ar jnno use hoi
  restartButton.pack(side="top")

  frame=Frame(screen) # frame creaate na korle button gula 6itea jete pare.
  frame.pack()

  for row in range(3):
    for col in range(3):
        button[row][col]=Button(frame,font=("arial",30),width=5,height=2,command=lambda row=row,column=col:next_turn(row,column))
        button[row][col].grid(row=row,column=col) 
        
  screen.mainloop()
