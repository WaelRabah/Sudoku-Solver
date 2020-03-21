from node import Node
import numpy as np


class board (object):
	def __init__(self):
		self.history=[]
		self.board = [
        	[7, 8, 0, 4, 0, 0, 1, 2, 0],
        	[6, 0, 0, 0, 7, 5, 0, 0, 9],
        	[0, 0, 0, 6, 0, 1, 0, 7, 8],
        	[0, 0, 7, 0, 4, 0, 2, 6, 0],
        	[0, 0, 1, 0, 5, 0, 9, 3, 0],
        	[9, 0, 4, 0, 6, 0, 0, 0, 5],
        	[0, 7, 0, 3, 0, 0, 0, 1, 2],
        	[1, 2, 0, 0, 0, 7, 4, 0, 0],
        	[0, 4, 9, 2, 0, 6, 0, 0, 7]
    				]		
    	
	#def generateBoard(self):
	#	for j in range(9):
	#		self.board.append([])
	#	for j in range(9):
	#		for i in range(9):
	#			x=np.random.randint(0,10)
	#			if check(x,self.board):
	#				self.board[j].append(Node(j,i,x))
	def print(self):
		for i in range(9):
			print(end=' ')
			for j in range(9):
				print(self.board[i][j],end="  ")
				if(j==2 or j==5):
					print('||', end=' ')
					print(end=" ")																							
			print()
			if (i==2 or i==5 ):
				print(end=' ')
				print('—',end='  ') 
				print('—',end='  ') 
				for x in range(9):
					print('—',end='  ') 
				print()

	def find_empty(self):
		for i in range(9):
			for j in range(9):
				if(self.board[i][j]==0):
					return i,j
		return None
	def valid (self,x,y,val):
		xs=[]
		ys=[]
		mat=[]
		y1=y//3
		x1=x//3
		for i in range(9):
			xs.append(self.board[x][i])
			ys.append(self.board[i][y])
		for i in range(x1*3,x1*3+3):
			for j in range(y1*3,y1*3+3):
				mat.append(self.board[i][j])
		if (val not in xs) and (val not in ys) and (val not in mat):
				return(True)
		return(False)
			
	def count_empty(self):
		x=0
		for i in range(len(self.board)):
			for j in range(len(self.board)):
				if(self.board[i][j]==0):
					x=x+1
		return(x)
	def backtrack(self):
		for i in range(len(self.history)):
			x,y=self.history[-i-1]
			self.fill_cell(x,y)

	def solve (self) :
		find=self.find_empty()
		if (not find) : 
			return(True)
		else :
			row,col=find
		for i in range(1,10):
			if(self.valid(row,col,i)):
				self.board[row][col]=i
				if (self.solve() is True):
					return(True)
			self.board[row][col]=0
		return(False)

		


b=board()

.print()
b.solve()
print('___________________________________')
b.print()