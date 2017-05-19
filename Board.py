class Board():
      def __init__(self):
	  self.dummy=0;
	  self.board = self.identity();

#      def detect(self,shape):
          
	  	  
      def freeze(self,points):
          i = 0
          for j in points:
	      self.board[points[i][0],points[i][1]] = 1
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
