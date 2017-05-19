
from ShapesWrapper import ShapesWrapper
from User import User
import os
import sys
class Observer():
      def __init__(self):
	  self.exit = False;
	  self.shapesWrapper = ShapesWrapper();
          self.user = User(self);
	  self.bodyCollision=False
      def end(self):
	  self.user.exit = True;
          self.shapesWrapper.exit = True;
	  os.system('stty sane');
	  sys.exit();
      def up(self):
	  self.shapesWrapper.shape.rotate();
      def down(self):
	  self.shapesWrapper.shape.shiftDown(self.shapesWrapper);
#	  self.shapesWrapper.shiftIndex+=1
      def right(self):
	  self.shapesWrapper.shape.shiftRight();
      def left(self):
	  self.shapesWrapper.shape.shiftLeft();
      def begin(self):
#	  try:
	  self.user.start();
	  self.shapesWrapper.start();
#	  except KeyboardInterrupt:
#	   self.end();
#	   self.cleanup();


obj = Observer()
try:
   obj.begin()
except KeyboardInterrupt:
   obj.end()
