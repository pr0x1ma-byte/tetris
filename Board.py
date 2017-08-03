height = 32
width  = 32
class Board():
      def __init__(self):
	  self.dummy=0;
	  self.board      = self.identity();
	  self.boardColor = self.identityColor();
	  	  
      def freeze(self,shape,canvas,matrix):
          i = 0
	  points = shape.points
          for j in points:
	      self.board[points[i][0]][points[i][1]]      = 1
	      self.boardColor[points[i][0]][points[i][1]] = shape.color
	      i+=1
          self.rowCompleteCheck(canvas,matrix)
	  matrix.Clear()
	  self.draw(canvas)
	  canvas = matrix.SwapOnVSync(canvas)

''' //todo expand identity matricies to 32x32, may have to adjust the various size numbers 8,7, and 6...'''
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
  	
      def rowCompleteCheck(self,canvas,matrix):


          while True:
		_i = self.getFirstCompleteIndex()
	        if _i > -1:
	           matrix.Clear()
		   self.shiftAndClear(_i)
	           self.draw(canvas)
		   canvas = matrix.SwapOnVSync(canvas)
	        else:
	           break
	                   	
      def getFirstCompleteIndex(self):
	  _sum = self.sumX()
	  _val = -1
	  for j in range(0,height):
	      if _sum[j][0] > height - 1:
	         _val = j
                 break

	  return _val
          
      def draw(self,canvas):
          for j in range(0,height):
	      for k in range(0,height):
	          _c = self.boardColor[j][k]
	          if _c != []:
	             canvas.SetPixel(j,k,_c[0],_c[1],_c[2]);
             
      def shiftAndClear(self, _x):
	   for j in range(0,height):
	       _a = self.board[j]
	       _b = self.boardColor[j]
	       del _a[_x]
	       del _b[_x]
	       _a.insert(height - 2,0)
               _b.insert(height - 2,[])
	       self.board[j]      = _a
	       self.boardColor[j] = _b

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

      def checkPointsCollision(self,_x,_y):
	  _failed = {'top':False,'bottom':False,'side':False,'other':False}
	  if _y < 0:
	     _failed['bottom'] = True
	  else:
	     if _y > height - 1:
	        _failed['top'] = True
	    #    if _v > 0:
	    #       _failed['other'] = True
	     elif _x > width - 1 or _x < 0:
	        _failed['side'] = True
	     else:
	        _v = self.board[_x][_y]
	        if _v > 0:
                   _failed['other'] = True
	  return _failed          	

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
