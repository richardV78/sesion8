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
            if(self.connection == None):
                self.connection = mysql.connector.connect(
                    host = self.host, 
                    user = self.user, 
                    password = self.pw, 
                    database = self.db
                )
                os.system("color a2")            
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
    
    def execute_query(self, query, params=None):
        try: 
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as eror:
            print(f"error:{eror}")

            

db =MySQLDB("localhost" ,"root", "", "testlp")
print("conectado")

db.connect()
db.disconnected()

# i need the practice 