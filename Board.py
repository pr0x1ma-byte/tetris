class Board():
      def __init__(self):
	  self.dummy=0;
	  self.board = self.identity();

#      def detect(self,shape):
          
	  	  
      def freeze(self,shape):
          i = 0
	  points = shape.points
          for j in points:
	      self.board[points[i][0],points[i][1]] = shape.color
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
	
      def draw(self):
	  print '-------Board-------'
	  print self.board
	  print '-------------------'

#	  i = 0
#          for j in self.board
#	      _x = self.board[i][0]
#	      _y = self.board[i][1]
#	      if _x != 0 and _y != 0:
#	      unicorn.set_pixel(_x,_y,self.color[0],self.color[1],self.color[2]);
