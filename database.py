import mysql.connector
import os

def _init_(self, host, user, password, database):
    self.host = host
    self.user = user
    self.pw = password
    self.db = database

