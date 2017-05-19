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
	  i = 0
          for j in self.boardColor:
	      _x = self.board[i][0]
	      _y = self.board[i][1]
		
 	      if _x != [] and _y != []:
	         unicorn.set_pixel(_x,_y,255,255,255);
	      #unicorn.set_pixel(_x,_y,self.color[0],self.color[1],self.color[2]);
