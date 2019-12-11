from flask import Flask
import psycopg2 as dbapi2
from passlib.hash import pbkdf2_sha256 as hasher
from flask_login import UserMixin
from balance import Balance

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
      sql_command="INSERT INTO GROUP (ID,NAME,LEADER_ID) VALUES ( %(id)s, %(name)s, %(leader_id)s)"
      cursor.execute(sql_command,{'id':group.id,'name':group.name,'leader_id':group.leader_id})
      connection.commit()
      cursor.close()
  def create_past_event(self):
    with dbapi2.connect(self.connection_string) as connection:
      cursor = connection.cursor()
      sql_command="CREATE TABLE IF NOT EXISTS PAST_EVENT (ID SERIAL PRIMARY KEY,GROUP_ID INT REFERENCES GROUP(ID), TITLE VARCHAR(100) NOT NULL, TYPE VARCHAR(100) NOT NULL, LOCATION VARCHAR(100), DESCRIPTION VARCHAR(100),START_TIME VARCHAR(100) NOT NULL, END_TIME VARCHAR(100) NOT NULL )"
      cursor.execute(sql_command)
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
      sql_command="INSERT INTO MEMBER (ID,TITLE,TYPES,LOCATION,DESCRIPTION,START_TIME,END_TIME) VALUES ( %(id)s, %(title)s, %(types)s, %(location)s, %(description)s, %(start_time)s, %(end_time)s)"
      cursor.execute(sql_command,{'id':public_event.id,'title':public_event.title,'types':public_event.types,'location':public_event.location,'description':public_event.description,'start_time':public_event.start_time,'end_time':public_event.end_time})
      connection.commit()
      cursor.close()