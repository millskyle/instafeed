import json
import sys
import bottle
from multiprocessing import Process
from database import dbHandler
from bottle import request
sys.path.append('./insta/')
import imagecollector

imageCollector = imagecollector.ImageCollector()
setup = False #True 
#setup = True
dbHandler.init()
#imageCollector.start()
#if setup:
#   scraperWorker.start()

@bottle.hook('before_request')
def _connect_db():
   dbHandler.db.connect()

@bottle.hook('after_request')
def _close_db():
   if not dbHandler.db.is_closed():
      dbHandler.db.close()

@bottle.route('/')
def index():
    return bottle.static_file('input.html', root='./')

@bottle.route('/get_photos.json')
def get_photos():
   global imageCollector
   if imageCollector.is_alive():
         imageCollector.end()
         imageCollector = imagecollector.ImageCollector()
         imageCollector.set_hashtag("whydevtest")

   imageCollector.start()

   data = dbHandler.getPics(10)
   templ = open('template/get_photos.json', 'r').read()
   return bottle.template(templ, data=data, watch_tag='whydevtest')

@bottle.route('/get_photos_static.json')
def get_photos_static():
   return bottle.static_file('get_photos_static.json', root='template/')



@bottle.route('/slideshow', method="POST")
def getCalendar():
   #Now begin the process of querying the db
   global imageCollector
   semester = request.forms.get("hashtag")
   dbHandler.init(True) #Clear the database

   #   p = Process(target=imageCollector.run())
#   p.start()

   urls = open("images.txt","r").read().replace('\n','').split(',')
   templ = open('template/slideshow.tmpl','r').read()

#   return bottle.template(templ, urls=urls)
   return bottle.static_file('slideshow.tmpl',root='template/')

@bottle.route('/slideshow.css')
def slideshowcss():
   return bottle.static_file('slideshow.css',root='css/')

@bottle.route('/jquery-slider.js')
def jquery_slider():
   return bottle.static_file('jquery-slider.js', root='js/')

@bottle.route('/heart.svg')
def heart():
   return bottle.static_file('heart.svg', root='img/')

old="""

@bottle.route('/uoit.svg')
def uoitsvg():
    return bottle.static_file('uoit.svg', root='static/')

@bottle.route('/addwatch', method="POST")
def add_watch():
   crn = request.forms.getall("crn")[0]
   semester = request.forms.getall("semester")[0]
   email = request.forms.getall("email")[0]
   dbHandler.add_watch(semester,crn,email)
   return bottle.static_file('thank-you.html', root='static/')

@bottle.route('/getAvailableCourses/<sem>')
def getAvailCourses(sem):
   print request.body.read()
   return json.dumps(dbHandler.getAvailableCourses(sem),
          sort_keys=True, ensure_ascii=True   )

"""

bottle.run(host='', port=80)


