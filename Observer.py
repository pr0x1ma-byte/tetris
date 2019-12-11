from User import user
from Main import Generator
import unicornhat as unicorn
from pyfiglet import figlet_format
import os
import sys
import queue

from Key import Key

k=-1
unicorn.brightness(.5)
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
width,height=unicorn.get_shape()
unicorn.rotation(0)
class observer():
      def __init__(self):
	  self.exit = False;
          self.input = Queue()
	  self.generator = Generator();
          self.user = user(self.input);
	  self.bodyCollision=False
      def end(self):
	  self.exit = True;
          self.generator.exit = True;
      def up(self):
	  self.generator.shape.rotate();
      def down(self):
	  self.generator.shape.rotate();
      def right(self):
	  self.generator.shape.shiftRight();
      def left(self):
	  self.generator.shape.shiftLeft();
      def cleanup(self):
	  unicorn.clear();
	  unicorn.rotation(90);
	  for i in range(100):
	      self.showScore();
	  os.system('stty sane');
	  sys.exit();	

      def begin(self):
#	  self.user.start();		
#	  self.generator.begin()	
#	  self.snake.addNode();
	  try:
	   self.user.start();
	   self.generator.start();

           while True:
               key = self.input.get()
               
	  except KeyboardInterrupt:
	   self.end();
	   self.cleanup();
observer().begin()
