import threading
import tty
import sys
import os
from Key import Key
class User(threading.Thread):
      def __init__(self,key):
          threading.Thread.__init__(self)
          self.key = key
      
      def run(self):
          
          tty.setraw(sys.stdin.fileno())
          while True:
#                if  bal.getExit():
#                    bal.setUserExit();
#                    break;
#                else:
                 ch = sys.stdin.read(1)
                 if (ch == 'w'):
                    self.key.put(Key.UP)
                 elif (ch == 's'):
                    self.key.put(Key.DOWN)
                 elif ch == 'a':
                    self.key.put(Key.LEFT)
                 elif ch == 'd':
                    self.key.put(Key.RIGHT)
                 elif ch == 'b':
		    os.system('stty sane');
                    self.key.put(Key.END)	
                    break;
#	  print("size: "+str(ob.snake.size));
#	  ob.end();
#          ob.cleanup(); 
