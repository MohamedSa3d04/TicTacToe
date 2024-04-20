from tkinter import * #Intializing all the components of the library
from time import sleep
from playsound import playsound
#---------------------------Game Code--------------------------------

root = Tk() 

#player calss
class Player:
    def __init__(self, name, char,  Turn = True, color = 'red'):
        self.name = name
        self.char = char
        self.score = IntVar(root, value=0)
        self.score.set(0)
        self.Turn = Turn
        self.color = color
        self.winner = False

#game class
class Game:
    def __init__(self):
        self.gamebtns = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        self.counter = 3
        self.draw = False

    def statue_changed(self):        
        if player1.Turn:
            #Player 2 win
            board.statue.config(text=f'{player2.name} Wins..{self.counter}')            
            
        else:
            #Player 1 win
            board.statue.config(text=f'{player1.name} Wins..{self.counter}')
        if self.draw :
            board.statue.config(text=f'Draw..{self.counter}')            
        self.counter -= 1

        if self.counter >= 0 :
            root.after(1000, self.statue_changed)

        elif self.counter == -1:
            self.counter = 3
            board.prepare_board()
    def player_Plays(self, row, col):
        if self.gamebtns[row][col].cget('text') =='' and self.counter == 3:
            if player1.Turn:
                self.gamebtns[row][col].config(text = f'{player1.char}', fg = f'{player1.color}')
                player1.Turn = False
                player2.Turn = True
            elif player2.Turn:
                self.gamebtns[row][col].config(text = f'{player2.char}', fg = f'{player2.color}')
                player2.Turn = False
                player1.Turn = True  

            #Game checker:
            if self.game_end():
                if player1.Turn:#player 2 win
                  player2.score.set(player2.score.get() + 1)
                else:
                  player1.score.set(player1.score.get() + 1)  
                self.statue_changed()
            elif self.is_draw(): #Checking for draw
                self.draw = True
                self.statue_changed() 

                    

    def game_end(self):
        #Checking for horizental cells
        for i in range(3):
            if self.gamebtns[i][0].cget('text') == self.gamebtns[i][1].cget('text') == self.gamebtns[i][2].cget('text'):
                if self.gamebtns[i][0].cget('text') != '' and self.gamebtns[i][1].cget('text') != '' and self.gamebtns[i][2].cget('text') != '':
                    self.gamebtns[i][0].config(bg = '#EBFF7B')
                    self.gamebtns[i][1].config(bg = '#EBFF7B')
                    self.gamebtns[i][2].config(bg = '#EBFF7B')
                    return True
        #Checking for vertical cells:
        for i in range(3):
            if self.gamebtns[0][i].cget('text') == self.gamebtns[1][i].cget('text') == self.gamebtns[2][i].cget('text'):
                if self.gamebtns[0][i].cget('text') != '' and self.gamebtns[1][i].cget('text') != '' and self.gamebtns[2][i].cget('text') != '':
                    self.gamebtns[0][i].config(bg = '#EBFF7B')
                    self.gamebtns[1][i].config(bg = '#EBFF7B')
                    self.gamebtns[2][i].config(bg = '#EBFF7B')                    
                    return True
        #Checking for dialogs:
        if self.gamebtns[0][0].cget('text') == self.gamebtns[1][1].cget('text') == self.gamebtns[2][2].cget('text'):
            if self.gamebtns[0][0].cget('text') != '' and self.gamebtns[1][1].cget('text') != '' and self.gamebtns[2][2].cget('text') != '':
                    self.gamebtns[0][0].config(bg = '#EBFF7B')
                    self.gamebtns[1][1].config(bg = '#EBFF7B')
                    self.gamebtns[2][2].config(bg = '#EBFF7B')      
                    return True        
        elif self.gamebtns[0][2].cget('text') == self.gamebtns[1][1].cget('text') == self.gamebtns[2][0].cget('text'):
            if self.gamebtns[0][2].cget('text') != '' and self.gamebtns[1][1].cget('text') != '' and self.gamebtns[2][0].cget('text') != '':
                    self.gamebtns[0][2].config(bg = '#EBFF7B')
                    self.gamebtns[1][1].config(bg = '#EBFF7B')
                    self.gamebtns[2][0].config(bg = '#EBFF7B')               
                    return True    

        return False
    
    def is_draw(self):
        for row in self.gamebtns:
            for btn in row:
                if btn.cget('text') == '':
                    return False        
        return True
class Board :
    def __init__(self, root):
        self.root = root
        self.root.geometry('700x550+250+50') 
        self.root.resizable(False,False) 
        self.root.title("Tic Tac Toe") 
        self.root.config(background='white') 

        #Results Frame:
        self.resFrame = Frame(self.root, bg='#E9CF88',width=800 ,height=45)
        self.resFrame.pack()
        self.lblres1 = Label(self.resFrame, fg=f'{player1.color}', font=('consolas',15),text=f'{player1.name}({player1.char}) Score : ')
        self.lblres1.place(x=2,y=10)
        self.lblval1 = Label(self.resFrame, fg=f'{player1.color}', font=('consolas',15), textvariable=player1.score)
        self.lblval1.place(x=200,y=10)

        self.lblres2 = Label(self.resFrame, fg=f'{player2.color}', font=('consolas',15),text=f'{player2.name}({player2.char}) Score : ')
        self.lblres2.place(x=475,y=10)
        self.lblval2 = Label(self.resFrame, fg=f'{player2.color}', font=('consolas',15), textvariable=player2.score)
        self.lblval2.place(x=680,y=10)
        self.statue = Label(self.root, fg='red', font=('consolas',20), text=f'{player1.name} Vs {player2.name}')
        self.statue.pack()

        self.prepare_board()

        # Buttons:
    def prepare_board(self):
        #Buttons Frame:
        self.statue.config(text=f'{player1.name} Vs {player2.name}') 
        self.btnFrame = Frame(self.root, bg='white',width=800 ,height=510)
        self.btnFrame.place(x=100,y=100)
        game = Game()
        for row in range(3):
            for col in range(3):
                game.gamebtns[row][col] = Button(self.btnFrame,text='', font=('consolas',50), width=4, height=1
                ,command=lambda row = row, col = col:game.player_Plays(row,col))
                game.gamebtns[row][col].grid(row = row, column = col)


#Players Attributes 
player1 = Player('MoSaad', 'O', color='red')
player2 = Player('MoKamal', 'X', Turn=False, color='blue')



board = Board(root)
root.mainloop()
