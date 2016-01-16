import re
from dbSetup import *
import urllib2
from urllib import urlencode
from datetime import datetime, timedelta
import random

#initializes the database
#Use reinit for debugging purposes
#True or 1 to clear all data in database
def init(reinit=False):
   if reinit:
      __deleteTables()
   __createTables()

def __deleteTables():
   images.drop_table(True)

def __createTables():
   images.create_table(True)


def getPics(count=10):
   query = images.select().where(images.hide==0)
   rows = images()
   if query.exists():
      rows = query.get()

   data = []


   for row in images.select().where(images.hide==0) : #random.shuffle(rows)[0:count]:
      data.append(
        [
          row.stdres_url,
          row.stdres_height,
          row.stdres_width,
          row.user_username,
          row.user_profile_picture,
          row.likes,
          row.caption_text
          ]
      )
   return data



def updatePic(pic):
   query = images.select().where(images.id == pic.picture.id)
   row = images()

   #checks to see if we're inserting or updating
   insert = True
   if query.exists():
      row = query.get()
      insert = False

   row.created_time = pic.picture.created_time

   row.caption_created_time = pic.picture.caption.created_time
   row.caption_user_userid = pic.picture.caption.creator.userid
   row.caption_user_profile_picture = pic.picture.caption.creator.profile_picture
   row.caption_user_username = pic.picture.caption.creator.username
   row.caption_text = pic.picture.caption.text

   row.id = pic.picture.id

   row.comments = pic.picture.comments

   row.lowres_url = pic.picture.lowres_url
   row.lowres_height = pic.picture.lowres_size[1]
   row.lowres_width = pic.picture.lowres_size[0]

   row.stdres_url = pic.picture.stdres_url
   row.stdres_height = pic.picture.stdres_size[1]
   row.stdres_width = pic.picture.stdres_size[0]

   row.thumb_url = pic.picture.thumb_url
   row.thumb_height = pic.picture.thumb_size[1]
   row.thumb_width = pic.picture.thumb_size[0]

   row.likes = pic.picture.likes
   row.link = pic.picture.link
   row.location = pic.picture.location
   row.tags = " ".join(pic.picture.tags)
   row.type = pic.picture.type
   row.users_in_photo = " ".join(pic.picture.users_in_photo)

   row.user_userid = pic.picture.user.userid
   row.user_profile_picture = pic.picture.user.profile_picture
   row.user_username = pic.picture.user.username


   row.hide = 0

   row.save()


