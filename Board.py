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
  	
      def draw(self):
#          unicorn.clear()
          for j in range(0,7):
	      for k in range(0,7):
	          _c = self.boardColor[j][k]
	          if _c != []:
	             unicorn.set_pixel(j,k,_c[0],_c[1],_c[2]);
#          unicorn.show()
