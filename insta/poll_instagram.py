from urllib2 import urlopen
import json
from database import dbHandler as database


access_token = "1233256115.4981f76.78c0732a51f542efad780589dc8f5ff5"
client_id = "4981f760f6a444eb964b7219aa13ded3"
client_secret = "2bcfbd53a8174811b7f44c970136521c"

class user:
    def __init__(self,d):
        self.full_name = d['full_name']
        self.userid = d['id']
        self.profile_picture = d['profile_picture']
        self.username = d['username']

class caption:
    def __init__(self,d):
        self.created_time = d['created_time']
        self.creator = user(d['from'])
        self.text = d['text']

class picture:
    def __init__(self,d):
        self.comments = int(d['comments']['count'])
        self.caption = caption(d['caption'])
        self.created_time = d['created_time']
        self.id = d['id']
        self.lowres_url = d['images']['low_resolution']['url']
        self.lowres_size = [ int(d['images']['low_resolution']['width']),int(d['images']['low_resolution']['height'])]
        self.stdres_url = d['images']['standard_resolution']['url']
        self.stdres_size = [ int(d['images']['standard_resolution']['width']),int(d['images']['low_resolution']['height'])]
        self.thumb_url = d['images']['thumbnail']['url']
        self.thumb_size = [ int(d['images']['thumbnail']['width']),int(d['images']['low_resolution']['height'])]
        self.likes = int(d['likes']['count'])
        self.link = d['link']
        self.location = d['location']
        self.tags = d['tags']
        self.type = d['type']
        self.users_in_photo = d['users_in_photo']
        self.user = user(d['user'])

class PictureModel():
    def __init__(self,data):
        self.picture = picture(data)


class Instagram:
    def __init__(self, access_token, client_id, client_secret):
        self.access_token = access_token
        self.client_id = client_id
        self.client_secret = client_secret

    def tag_query(self,tag):
        url = "https://api.instagram.com/v1/tags/{0}/media/recent?access_token={1}".format(tag, self.access_token)
        data = urlopen(url).read()
        data = json.loads(data.decode())
        self.data = data

class InstagramAPI:
   def __init__(self):
      self.api = Instagram(access_token=access_token, client_secret=client_secret, client_id=client_id) 

   def poll(self,query="whydevtest"):
      print "Running query..."
      self.api.tag_query(query)

      for d in self.api.data['data']:
         print "Found image"
         pic = PictureModel(d)
         database.updatePic(pic)

