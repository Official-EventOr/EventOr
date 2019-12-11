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
  def create_group(self):
    with dbapi2.connect(self.connection_string) as connection:
      cursor = connection.cursor()
      sql_command="CREATE TABLE IF NOT EXISTS GROUP (ID SERIAL PRIMARY KEY,NAME VARCHAR(100), LEADER_ID INT REFERENCES USERS(ID))"
      cursor.execute(sql_command)
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
  def create_public_event(self):
    with dbapi2.connect(self.connection_string) as connection:
      cursor = connection.cursor()
      sql_command="CREATE TABLE IF NOT EXISTS PUBLIC_EVENT (ID SERIAL PRIMARY KEY, TITLE VARCHAR(100) NOT NULL, TYPE VARCHAR(100) NOT NULL, LOCATION VARCHAR(100), DESCRIPTION VARCHAR(100),START_TIME VARCHAR(100) NOT NULL, END_TIME VARCHAR(100) NOT NULL)"
      cursor.execute(sql_command)
      connection.commit()
      cursor.close()