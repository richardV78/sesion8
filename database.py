import mysql.connector
import os

class MySQLDB:
    def _init_(self, host, user, password, database):
        self.host = host
        self.user = user
        self.pw = password
        self.db = database

def conect(self):
    try: 
        if(self.connect == None):
            self.connection = mysql.connector.connect(
            host = self.host, 
            user  = self.user, 
            paassword = self.pw, 
            database = self.db
        )

    except mysql.connector.Error as error:
        print("ERROR MIENTRAS SE ESTABA CONECTANDO LA BASE DE DATOS")


db = MySQLDB("localhost","root","","dateslp")
