from tkinter import *
# It takes the position of the currently clicked cell and checks whether the gamestaistus  
# True or not (i.e the game is over or not) and if the game is not over yet, it checks for the position and then if the corresponding cell is empty it changes its display value
def click(r,c):
    global usr
    global gamestatus
    #usr: this variable help us to identify the current player (x or o)
    #gamestatus: it is a flag variable which indicates the status of the game ie the game is over or not. Gamestatus= False indicates game is over
    if(usr=='X' and grd[r][c]==0 and gamestatus==True):
        # grd: It is a 3×3 matrix which stores the values of all the cells
        grd[r][c]='X'
        usr='O'
    #curr: It is a list of tkinter buttons which will click() everytime it is clicked
        curr[r][c].configure(text='X',bg="white")

    if(usr=='O' and grd[r][c]==0 and gamestatus==True):
        grd[r][c]='O'
        usr='X'
        curr[r][c].configure(text='O',bg="gray")
    
    checkWin()
 #This function updates gamestatus by checking every row, column and diagonal.
 #If every cell of a particular row, column or diagonal is same, gamestatus is set to false indicating game is over now
def checkWin():
    global gamestatus
    for i in range(3):
        if grd[0][i]==grd[1][i]==grd[2][i]!=0:
            for j in range(3):
                curr[j][i].config(bg="snow4",fg="white")
            gamestatus=False
    for i in range(3):            
        if grd[i][0]==grd[i][1]==grd[i][2]!=0:
            for j in range(3):
                curr[i][j].config(bg="snow4",fg="white")
            gamestatus=False
    if grd[0][2]==grd[1][1]==grd[2][0]!=0:
            curr[0][2].config(bg="snow4",fg="white")
            curr[1][1].config(bg="snow4",fg="white")
            curr[2][0].config(bg="snow4",fg="white")
            gamestatus=False
    if grd[0][0]==grd[1][1]==grd[2][2]!=0:
            for j in range(3):
                curr[j][j].config(bg="snow4",fg="white")
            gamestatus=False
 #to create GUI       
root=Tk()
root.title("Tic Tac Toe")

usr="O"
gamestatus=True
grd=[[0,0,0],
     [0,0,0],
     [0,0,0]]

curr=[[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(3):
    for j in range(3):
        curr[i][j]=Button(font=('arial',30,'bold'),width=4,
        command=lambda r=i, c=j:click(r,c))
        curr[i][j].grid(row=i,column=j)

mainloop()