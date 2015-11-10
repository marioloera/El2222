from Tkinter import *
import time

marginX = 5
marginY = 200
cellSize = 200

class TicTacToeGUI:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, bg = "lightgreen", height=cellSize*3+marginY+marginX*2, width=cellSize*3+marginX*2)
        self.canvas.pack()
        self.root.canvas = self.canvas
        self.leftButtonAction = self.no_action
        self.rightButtonAction = self.no_action
        self.upButtonAction = self.no_action
        self.downButtonAction = self.no_action
        self.spaceButtonAction = self.no_action
        self.rButtonAction = self.no_action
        self.gui_reset()
    
    ###The interface
    def up_button(self,event):
        self.upButtonAction()
        
    def down_button(self,event):
        self.downButtonAction()
        
    def left_button(self,event):
        self.leftButtonAction()
        
    def right_button(self,event):
        self.rightButtonAction()
        
    def space_button(self,event):
        self.spaceButtonAction()
        
    def r_button(self,event):
        self.rButtonAction()
        
    ###Non-button stuff:
    def gui_select(self,x,y):
        for i in range(3):
        	for j in range(3):
        		self.draw_selection( i, j,"white")
        self.draw_selection(y,x,"red")
        
    def gui_mark(self,x,y,player):
        if player==1:
            self.draw_x(y,x)
        elif player == -1:
            self.draw_o(y,x)

        
    def gui_display_text(self,toDisplay):
    	self.canvas.create_rectangle(0,0,610,199, fill = "lightgreen",outline = "lightgreen")
        self.canvas.create_text(305,100, text = toDisplay, font=("Purisa",30))
        
    def gui_reset(self):
        self.canvas.delete(ALL)
        self.drawTicTacToe()
        
    def no_action(self):
        pass
        
    def start(self):
    	self.init_keys()
        self.root.mainloop()
        
    ###Helper functions
    def init_keys(self):
        self.root.bind("<Up>", self.up_button)
        self.root.bind("<Down>", self.down_button)
        self.root.bind("<Left>", self.left_button)
        self.root.bind("<Right>", self.right_button)
        self.root.bind("<space>", self.space_button)
        self.root.bind("<r>", self.r_button)
        
    def draw_o(self,row,col):
        self.canvas.create_oval(marginX+col*cellSize+10, marginY+row*cellSize+10, marginX+col*cellSize+cellSize-10, marginY+row*cellSize+cellSize-10, fill = "blue", outline="white")
        self.canvas.create_oval(marginX+col*cellSize+20, marginY+row*cellSize+20, marginX+col*cellSize+cellSize-20, marginY+row*cellSize+cellSize-20, fill = "white",outline="blue")

        
    def draw_x(self,row, col):
        self.canvas.create_line(marginX+col*cellSize+15, marginY+row*cellSize+15, marginX+col*cellSize+cellSize-15, marginY+row*cellSize+cellSize-15, fill = "green", width=10)
        self.canvas.create_line(marginX+col*cellSize+15, marginY+row*cellSize+cellSize-15, marginX+col*cellSize+cellSize-15, marginY+row*cellSize+15, fill = "green", width=10)
        
    def draw_selection(self, row, col,color):
        self.canvas.create_line(marginX+col*cellSize+5, marginY+row*cellSize+5, marginX+col*cellSize+cellSize-5, marginY+row*cellSize+5, fill = color, width=5)
        self.canvas.create_line(marginX+col*cellSize+7, marginY+row*cellSize+7,marginX+col*cellSize+7, marginY+row*cellSize+cellSize-7, fill = color, width=5)
        self.canvas.create_line(marginX+col*cellSize+5, marginY+row*cellSize+cellSize-5, marginX+col*cellSize+cellSize-5, marginY+row*cellSize+cellSize-5, fill = color, width=5)
        self.canvas.create_line(marginX+col*cellSize+cellSize-8, marginY+row*cellSize+8, marginX+col*cellSize+cellSize-8, marginY+row*cellSize+cellSize-6, fill = color, width=5)

    def drawTicTacToe(self):
        for i in range(3):
            for j in range(3):
                self.drawTicTacToeCell(j, i)
        return

    def drawTicTacToeCell(self, row, col):
        self.canvas.create_rectangle(marginX+col*cellSize, marginY+row*cellSize, marginX+col*cellSize+cellSize, marginY+row*cellSize+cellSize, fill = "white")

################################################################
## Here's an example of how to use the TicTacToeGUI interface ##
################################################################

if __name__=="__main__": #This line of code makes sure the following code only runs if this module is ran as the main program.

	tg = TicTacToeGUI()
	x = 0
	y = 0
	player = -1
	
	def sel():
		tg.gui_select(x,y)

	def lb():
		global x
		x-=1
		if x<0:
			x = 0
		sel()
		tg.gui_display_text("left")

	def rb():
		global x
		x+=1
		if x>2:
			x = 2
		tg.gui_display_text("right")
		sel()

	def ub():
		global y
		y-=1
		if y<0:
			y = 0
		tg.gui_display_text("up")
		sel()

	def db():
		global y
		y+=1
		if y>2:
			y=2
		tg.gui_display_text("down")
		sel()

	def sb():
		global player
		tg.gui_mark(x,y,player)
		player = -player
		tg.gui_display_text("space")
	
	def rrb():
		tg.gui_reset()
		tg.gui_display_text("r")

	tg.gui_display_text("welcome!")
	tg.leftButtonAction = lb
	tg.rightButtonAction = rb
	tg.upButtonAction = ub
	tg.downButtonAction = db
	tg.spaceButtonAction = sb
	tg.rButtonAction = rrb
	tg.start()

