import mysql.connector
import os

class MySQLDB:
    def _init_(self, host, user, password, database):
        self.host = host
        self.user = user
        self.pw = password
        self.db = database
        self.connection = None
    def connect(self):
        try: 
            if(self.connect == None):
                self.connection = mysql.connector.connect(
                    host = self.host, 
                    user  = self.user, 
                    paassword = self.pw, 
                    database = self.db
                )
                os.system("colora2")            
                print("chatel te conectaste")
        except mysql.connector.Error as error:
            print("ERROR MIENTRAS SE ESTABA CONECTANDO LA BASE DE DATOS{}".format(error))

    def disconnected(self):
            try: 
                if self.connection:
                    self.connection.close
                    self.connection = None
            except mysql.connector.Error as error:
                print("ERROR")                




db =MySQLDB("localhost" ,"root", "", "test-lp")
print("conectado")

db.connect()
db.disconnected()
