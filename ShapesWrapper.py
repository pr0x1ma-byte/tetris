from Line import Line
from LRectangle import LRectangleR
from LRectangle import LRectangleL
from Square import Square
from Triangle import Triangle
from ZShape import ZShapeR
from ZShape import ZShapeL
from random import randint
from Board import Board
import threading
import time

class ShapesWrapper(threading.Thread):
      def __init__(self, key):
          threading.Thread.__init__(self)
          self.shiftIndex = 0
          self.shape = []
	  self.board = Board()
          self.getNewObject()
          self.exit = False
	  self.key = key

      def getNewObject(self):
          val = randint(0,6);
          o   = [Line(),LRectangleL(),LRectangleR(),Triangle(),Square(),ZShapeL(),ZShapeR()]
          self.shape = o[val]
          self.shape.setBoard(self.board)

      def shift(self):
          if not self.exit:
             if self.shiftIndex > 7:
                self.shiftIndex = 0
                self.getNewObject()
#             self.board.detect(self.shape);
             self.shape.shiftDown(self)
             threading.Timer(1, self.shift).start()

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
    
