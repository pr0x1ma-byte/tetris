import threading
import tty
import sys

class User(threading.Thread):
      def __init__(self,observer):
          threading.Thread.__init__(self)
          self.observer = observer
	  self.exit = False
      def getObserver(self):
          return self.observer
      def run(self):
          ob = self.getObserver()
          tty.setraw(sys.stdin.fileno())
          while not self.exit:
#                if  bal.getExit():
#                    bal.setUserExit();
#                    break;
#                else:
                 ch = sys.stdin.read(1)
                 if (ch == 'w'):
                    ob.up()
                 elif (ch == 's'):
                    ob.down()
                 elif ch == 'a':
                    ob.left()
                 elif ch == 'd':
                    ob.right()
                 elif ch == 'b':
		    ob.end();	
                    break;
#	  print("size: "+str(ob.snake.size));
#	  ob.end();
#          ob.cleanup(); 
