import unicornhat as unicorn
class Board():
      def __init__(self):
	  self.dummy=0;
	  self.board      = self.identity();
	  self.boardColor = self.identityColor();

#      def detect(self,shape):
          
	  	  
      def freeze(self,shape):
          i = 0
	  points = shape.points
          for j in points:
	      self.board[points[i][0]][points[i][1]]      = 1
	      self.boardColor[points[i][0]][points[i][1]] = shape.color
	      i+=1
          self.rowCompleteCheck()
	  unicorn.clear()
	  self.draw()
	  unicorn.show()

      def identity(self):
          return [ [0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0],
             	   [0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0],]

      def identityColor(self):
          return [ [[],[],[],[],[],[],[],[]],
                   [[],[],[],[],[],[],[],[]],
		   [[],[],[],[],[],[],[],[]],
                   [[],[],[],[],[],[],[],[]],
		   [[],[],[],[],[],[],[],[]],
                   [[],[],[],[],[],[],[],[]],
		   [[],[],[],[],[],[],[],[]],
                   [[],[],[],[],[],[],[],[]]]
  	
      def rowCompleteCheck(self):


          while True:
		_i = self.getFirstCompleteIndex()
	        if _i > -1:
	           unicorn.clear()
		   self.shiftAndClear(_i)
	           self.draw()
		   unicorn.show()
	        else:
	           break
	                   	
      def getFirstCompleteIndex(self):
	  _sum = self.sumX()
	  _val = -1
	  for j in range(0,8):
	      if _sum[j][0] > 7:
	         _val = j
                 break

	  print _val
	  return _val
          
      def draw(self):
          for j in range(0,8):
	      for k in range(0,8):
	          _c = self.boardColor[j][k]
	          if _c != []:
	             unicorn.set_pixel(j,k,_c[0],_c[1],_c[2]);
             
      def shiftAndClear(self, _x):
#	   r = len(self.board) 
	   for j in range(0,8):
	       _a = self.board[j]
	       _b = self.boardColor[j]
	       del _a[_x]
	       del _b[_x]
	       _a.insert(6,0)
               _b.insert(6,[])
	       self.board[j]      = _a
	       self.boardColor[j] = _b
#	   unicorn.clear()
#           self.draw()
#	   unicorn.show()		                   
      def getNewRow(self):
          return [0,0,0,0,0,0,0,0]
	
      def getNewRowColor(self):
	  return [[],[],[],[],[],[],[],[]]

      def sumX(self):
	  _b = self.board
          return [ [ _b[0][0] + _b[1][0] + _b[2][0] + _b[3][0] + _b[4][0] + _b[5][0] + _b[6][0] + _b[7][0]],
		   [ _b[0][1] + _b[1][1] + _b[2][1] + _b[3][1] + _b[4][1] + _b[5][1] + _b[6][1] + _b[7][1]],
		   [ _b[0][2] + _b[1][2] + _b[2][2] + _b[3][2] + _b[4][2] + _b[5][2] + _b[6][2] + _b[7][2]],  
		   [ _b[0][3] + _b[1][3] + _b[2][3] + _b[3][3] + _b[4][3] + _b[5][3] + _b[6][3] + _b[7][3]], 
		   [ _b[0][4] + _b[1][4] + _b[2][4] + _b[3][4] + _b[4][4] + _b[5][4] + _b[6][4] + _b[7][4]], 
		   [ _b[0][5] + _b[1][5] + _b[2][5] + _b[3][5] + _b[4][5] + _b[5][5] + _b[6][5] + _b[7][5]], 
	  	   [ _b[0][6] + _b[1][6] + _b[2][6] + _b[3][6] + _b[4][6] + _b[5][6] + _b[6][6] + _b[7][6]], 
		   [ _b[0][7] + _b[1][7] + _b[2][7] + _b[3][7] + _b[4][7] + _b[5][7] + _b[6][7] + _b[7][7]], ]

#      def sumR(self):
#          _b = self.board
#          return [ [ _b[0][0] + _b[0][1] + _b[0][2] + _b[0][3] + _b[0][4] + _b[0][5] + _b[0][6] + _b[0][7]],
#         	   [ _b[1][0] + _b[1][1] + _b[1][2] + _b[1][3] + _b[1][4] + _b[1][5] + _b[1][6] + _b[1][7]],
#       	           [ _b[2][0] + _b[2][1] + _b[2][2] + _b[2][3] + _b[2][4] + _b[2][5] + _b[2][6] + _b[2][7]],
#       	           [ _b[3][0] + _b[3][1] + _b[3][2] + _b[3][3] + _b[3][4] + _b[3][5] + _b[3][6] + _b[3][7]],
#       	           [ _b[4][0] + _b[4][1] + _b[4][2] + _b[4][3] + _b[4][4] + _b[4][5] + _b[4][6] + _b[4][7]],
#        	   [ _b[5][0] + _b[5][1] + _b[5][2] + _b[5][3] + _b[5][4] + _b[5][5] + _b[5][6] + _b[5][7]],
#         	   [ _b[6][0] + _b[6][1] + _b[6][2] + _b[6][3] + _b[6][4] + _b[6][5] + _b[6][6] + _b[6][7]],
#         	   [ _b[7][0] + _b[7][1] + _b[7][2] + _b[7][3] + _b[7][4] + _b[7][5] + _b[7][6] + _b[7][7]], ]	  	
