from ShapesQue import ShapesQue
import threading
import time
height = 32
class ShapesWrapper():
      def __init__(self, observer):
          self.shiftIndex = 0
          self.shape = []
	  self.board = Board()
          self.getNewObject()
          self.exit = False
	  self.observer = observer
	  self.speed = .15
	  self.shapesQue  = ShapesQue()

      def getNewObject(self):
          #val = randint(0,6);
          #o   = [Line(),LRectangleL(),LRectangleR(),Triangle(),Square(),ZShapeL(),ZShapeR()]
          #self.shape = o[val]
	  self.shape = self.shapesQue.getNext()
          self.shape.setBoard(self.board)

      def shift(self):
          if not self.exit:
             if self.shiftIndex > height - 1:
                self.shiftIndex = 0
                self.getNewObject()
#		self.speed = self.speed - .005
#             self.board.detect(self.shape);
             self.shape.shiftDown(self)
#	     self.speed = self.speed - .01
             threading.Timer(self.speed, self.shift).start()

      def start(self):
          self.shift()

