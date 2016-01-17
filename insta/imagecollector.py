import time
import threading
from twisted.internet import reactor
from multiprocessing import Process
from database import dbHandler
import poll_instagram

class ImageCollector(threading.Thread):
   def __init__(self):
      super(ImageCollector, self).__init__()
      self.exit = False
      self.interval_time = 100 #every 20 minutes
      self.callbackInt = [0]
      self.hashtag = "whydevtest"

   def set_hashtag(self,hashtag):
      self.hashtag = hashtag
      return 0

   def run(self):
       while not self.exit:
         start_time = time.time()

         if (1):
            p = Process(target=self.runProcess)
            p.start()
            p.join()

         duration = time.time() - start_time
         for i in range(int(self.interval_time - duration)):
            if not self.exit:
               time.sleep(1)
            else:
               break;

   def end(self):
      self.exit = True


   def runProcess(self):
      api = poll_instagram.InstagramAPI()
      api.poll(self.hashtag)
      #reactor.run()

