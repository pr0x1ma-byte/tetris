from ShapesQue import ShapesQue
from Board import Board
import threading
import time

height = 32
class ShapesWrapper(threading.Thread):
      def __init__(self, key):
          threading.Thread.__init__(self)

          self.shiftIndex = 0
	  self.board = Board()

          self.exit = False
	  
	  self.speed = .15
	  self.que  = ShapesQue()
	  self.shape = self.que.getNext()
	  self.shape.setBoard(self.board)

	  self.key = key

      def getNewObject(self):
	  self.shape = self.que.getNext()
	  print self.shape.color
          self.shape.setBoard(self.board)

      def shift(self):
          if not self.exit:
             if self.shiftIndex > height - 1:
                self.shiftIndex = 0
                self.getNewObject()
#		self.speed = self.speed - .005
#             self.board.detect(self.shape);
#	     self.shape.drawBorder();
             self.shape.shiftDown(self)
#	     self.speed = self.speed - .01
             threading.Timer(self.speed, self.shift).start()

      def run(self):
          self.shift()
          
          while not self.exit:
              key = self.key.get()

              if key == Key.UP:
                  self.shape.rotate()
              elif key == Key.DOWN:
                  self.shape.shiftDown(self)
              elif key == Key.LEFT:
                  self.shape.shiftLeft(self)
              elif key == Key.RIGHT:
                  self.shape.shiftRight(self)
              elif key == Key.END:
                  self.exit = True
                  break;
    
