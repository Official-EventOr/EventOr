from flask import Flask
import psycopg2 as dbapi2
from passlib.hash import pbkdf2_sha256 as hasher
from flask_login import UserMixin
from hobby import Hobby
from member import Member
from group import Group
from past_event import Past_Event
from calendar import Calendar
from public_event import Public_Event
class Database:
  def __init__(self, connection_string):
    self.connection_string = connection_string
  def create_hobby(self):
    with dbapi2.connect(self.connection_string) as connection:
      cursor = connection.cursor()
      sql_command="CREATE TABLE IF NOT EXISTS HOBBY (USER_ID INT REFERENCES USERS(ID), NAME VARCHAR(100) NOT NULL UNIQUE, CONSTRAINT HOBBY PRIMARY KEY (USER_ID,NAME))"
      cursor.execute(sql_command)
      connection.commit()
      cursor.close()
  def add_hobby(self,hobby):
    with dbapi2.connect(self.connection_string) as connection:
      cursor = connection.cursor()
      sql_command="INSERT INTO HOBBY (USER_ID,NAME) VALUES (%(user_id)s, %(name)s)"
      cursor.execute(sql_command,{'user_id':hobby.user_id,'name':hobby.name})
      connection.commit()
      cursor.close()  
  def create_member(self):
    with dbapi2.connect(self.connection_string) as connection:
      cursor = connection.cursor()
      sql_command="CREATE TABLE IF NOT EXISTS MEMBER (USER_ID INT REFERENCES USERS(ID), GROUP_ID INT REFERENCES GROUP(ID) , CONSTRAINT MEMBER PRIMARY KEY (USER_ID,GROUP_ID))"
      cursor.execute(sql_command)
      connection.commit()
      cursor.close()
  def add_member(self,member):
    with dbapi2.connect(self.connection_string) as connection:
      cursor = connection.cursor()
      sql_command="INSERT INTO MEMBER (USER_ID,GROUP_ID) VALUES ( %(user_id)s, %(group_id)s)"
      cursor.execute(sql_command,{'user_id':member.user_id,'group_id':member.group_id})
      connection.commit()
      cursor.close()      
  def create_group(self):
    with dbapi2.connect(self.connection_string) as connection:
      cursor = connection.cursor()
      sql_command="CREATE TABLE IF NOT EXISTS GROUP (ID SERIAL PRIMARY KEY,NAME VARCHAR(100), LEADER_ID INT REFERENCES USERS(ID))"
      cursor.execute(sql_command)
      connection.commit()
      cursor.close() 
   def add_group(self,group):
    with dbapi2.connect(self.connection_string) as connection:
      cursor = connection.cursor()
      sql_command="INSERT INTO GROUP (NAME,LEADER_ID) VALUES ( %(id)s, %(name)s, %(leader_id)s)"
      cursor.execute(sql_command,{'name':group.name,'leader_id':group.leader_id})
      connection.commit()
      cursor.close()
  def create_past_event(self):
    with dbapi2.connect(self.connection_string) as connection:
      cursor = connection.cursor()
      sql_command="CREATE TABLE IF NOT EXISTS PAST_EVENT (ID SERIAL PRIMARY KEY,GROUP_ID INT REFERENCES GROUP(ID), TITLE VARCHAR(100) NOT NULL, TYPE VARCHAR(100) NOT NULL, LOCATION VARCHAR(100), DESCRIPTION VARCHAR(100),START_TIME VARCHAR(100) NOT NULL, END_TIME VARCHAR(100) NOT NULL )"
      cursor.execute(sql_command)
      connection.commit()
      cursor.close()
  def add_past_event(self,past_event):
    with dbapi2.connect(self.connection_string) as connection:
      cursor = connection.cursor()
      sql_command="INSERT INTO EVENT (GROUP_ID,TYPE,LOCATION,TITLE,START_TIME,END_TIME,DESCRIPTION,) VALUES (%(group_id)s, %(location)s,%(title)s,%(start_time)s,%(end_time)s,%(description)s)"
      cursor.execute(sql_command,{'group_id':past_event.user_name,'location':past_event.location,'location':past_event.location,'title':past_event.title,'start_time':past_event.start_time,'end_time':past_event.end_time,'description':past_event.description})
      connection.commit()
      cursor.close()      
  def create_calendar(self):
    with dbapi2.connect(self.connection_string) as connection:
      cursor = connection.cursor()
      sql_command="CREATE TABLE IF NOT EXISTS CALENDAR (USER_ID INT REFERENCES USERS(ID),EVENT_ID INT REFERENCES PUBLIC_EVENT(ID))"
      cursor.execute(sql_command)
      connection.commit()
      cursor.close()  
  def add_calendar(self,calendar):
    with dbapi2.connect(self.connection_string) as connection:
      cursor = connection.cursor()
      sql_command="INSERT INTO CALENDAR (USER_ID,EVENT_ID) VALUES ( %(user_id)s, %(event_id)s)"
      cursor.execute(sql_command,{'user_id':calendar.user_id,'event_id':calendar.event_id})
      connection.commit()
      cursor.close()      
  def create_public_event(self):
    with dbapi2.connect(self.connection_string) as connection:
      cursor = connection.cursor()
      sql_command="CREATE TABLE IF NOT EXISTS PUBLIC_EVENT (ID SERIAL PRIMARY KEY, TITLE VARCHAR(100) NOT NULL, TYPE VARCHAR(100) NOT NULL, LOCATION VARCHAR(100), DESCRIPTION VARCHAR(100),START_TIME VARCHAR(100) NOT NULL, END_TIME VARCHAR(100) NOT NULL)"
      cursor.execute(sql_command)
      connection.commit()
      cursor.close()
  def add_public_event(self,public_event):
    with dbapi2.connect(self.connection_string) as connection:
      cursor = connection.cursor()
      sql_command="INSERT INTO MEMBER (TITLE,TYPES,LOCATION,DESCRIPTION,START_TIME,END_TIME) VALUES ( %(id)s, %(title)s, %(types)s, %(location)s, %(description)s, %(start_time)s, %(end_time)s)"
      cursor.execute(sql_command,{'title':public_event.title,'types':public_event.types,'location':public_event.location,'description':public_event.description,'start_time':public_event.start_time,'end_time':public_event.end_time})
      connection.commit()
      cursor.close()


  def delete_event_from_calendar(self,calendar):
    with dbapi2.connect(self.connection_string) as connection:
      cursor = connection.cursor()
      sql_command="DELETE FROM CALENDAR WHERE (USER_ID = %(user_id)s AND EVENT_ID = %(user_id)s)"
      cursor.execute(sql_command,{'user_id':calendar.user_id,'event_id':calendar.event_id})
      connection.commit()
      cursor.close()
  def delete_group(self,group_id):
    with dbapi2.connect(self.connection_string) as connection:
      cursor = connection.cursor()
      sql_command="DELETE FROM GROUP WHERE (GROUP_ID = %(group_id)s)"
      cursor.execute(sql_command,{'group_id':group_id})
      connection.commit()
      cursor.close()
  def delete_member_from_group(self,member):
    with dbapi2.connect(self.connection_string) as connection:
      cursor = connection.cursor()
      sql_command="DELETE FROM MEMBER WHERE (USER_ID = %(user_id)s AND GROUP_ID = %(group_id)s)"
      cursor.execute(sql_command,{'user_id':member.user_id,'event_id':member.group_id})
      connection.commit()
      cursor.close()
  def delete_member_from_group(self,past_event):
    with dbapi2.connect(self.connection_string) as connection:
      cursor = connection.cursor()
      sql_command="DELETE FROM PAST_EVENT WHERE (ID = %(id)s)"
      cursor.execute(sql_command,{'id':past_event.id})
      connection.commit()
      cursor.close()
