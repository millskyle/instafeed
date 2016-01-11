import peewee as pw
from playhouse.pool import PooledMySQLDatabase
import MySQLdb
import datetime

dbname = 'instafeed'
dbuser = 'whyouth'
dbpass = 'wh1201youth'

#db = peewee.MySQLDatabase(dbname, user=dbuser, passwd=dbpass)
db = PooledMySQLDatabase(dbname, user=dbuser, passwd=dbpass)

#Base Models for tables to avoid annoying excess code
class BaseModel(pw.Model):
   class Meta:
      database = db

#Base Tables used to store information
#These classes define both the tables and can be used to store row information
#More info on usage can be found in dbHandler
class images(BaseModel):
   autoID = pw.PrimaryKeyField() #pretty much just used for joins don't touch

   caption_created_time = pw.CharField()
   caption_user_userid = pw.CharField()
   caption_user_profile_picture = pw.CharField()
   caption_user_username = pw.CharField()
   caption_text =  pw.CharField(null=True)

   created_time = pw.IntegerField()

   comments = pw.IntegerField()
   id = pw.CharField()

   lowres_url = pw.CharField()
   lowres_height = pw.IntegerField()
   lowres_width = pw.IntegerField()

   stdres_url = pw.CharField()
   stdres_width = pw.IntegerField()
   stdres_height = pw.IntegerField()

   thumb_url = pw.CharField()
   thumb_width = pw.IntegerField()
   thumb_height = pw.IntegerField()

   likes = pw.IntegerField()
   link = pw.CharField()
   location = pw.CharField(null=True)
   tags = pw.CharField(null=True)
   type = pw.CharField()
   number_of_users_in_photo = pw.IntegerField(default=0)
   users_in_photo = pw.CharField(null=True)

   user_userid = pw.CharField()
   user_profile_picture = pw.CharField()
   user_username = pw.CharField()

   hide = pw.IntegerField()


