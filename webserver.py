import json
import sys
import bottle
from database import dbHandler
from bottle import request
sys.path.append('./insta/')
import imagecollector

setup = False #True 
#setup = True
dbHandler.init()
imageCollector = imagecollector.ImageCollector()
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


@bottle.route('/slideshow', method="POST")
def getCalendar():
   #Now begin the process of querying the db
   semester = request.forms.get("hashtag")
   dbHandler.init(True) #Clear the database
   imageCollector.set_hashtag("whydevtest")
   imageCollector.runProcess()

   templ = open('template/slideshow.tmpl','r').read()

   return bottle.template(templ, out="DONE")


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


