class Node  (object) : 
	def __init__(self,x,y,val):
		self.x=x
		self.y=y
		if (val==0):
			val=" "
		self.val=val
	def getVal(self):
		return(self.val)
	def setVal(self,val):
		self.val=val