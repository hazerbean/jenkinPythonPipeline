import mysql.connector
class Person:
    def openconnection(self):
         connection = mysql.connector.connect(host='mysql-13607f80-harrybcardew-3774.a.aivencloud.com',
                                         database='defaultdb',
                                         user='avnadmin',
                                         password='AVNS_KTg3YdWhhFpsOXm5l9V',
                                         port='15673')
         return connection
    def createTables(self):
        connection = self.openconnection()
        returnstatement = ""
        try:
            mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL,
                             PRIMARY KEY (Id)) """
            cursor = connection.cursor()
            result = cursor.execute(mySql_Create_Table_Query)
            returnstatement = returnstatement + "Laptop Table created successfully "
        except mysql.connector.Error as error:
             returnstatement = returnstatement + ("Failed to create table in MySQL: {}".format(error))+ " "
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                returnstatement = returnstatement + (" MySQL connection is closed ")
        return returnstatement
    
    def selectData(self):
        connection = self.openconnection()
        mycursor = connection.cursor()
        mycursor.execute("SELECT * FROM Laptop")
        
        myresult = mycursor.fetchall()

        for x in myresult:
          print(x)
        return myresult
    
if __name__ == "__main__":
    random = Person()
    result= random.createTables()
    print(result)
    selectedData= random.selectData()
    print(selectedData)
