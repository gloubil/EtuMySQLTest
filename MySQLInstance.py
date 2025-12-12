import mysql.connector

class MySQLInstance:

    INSTANCE = None

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    def getInstance(self):
        if MySQLInstance.INSTANCE == None:
            MySQLInstance.INSTANCE = mysql.connector.connect(host=self.host, user=self.user, password=self.password)
        return MySQLInstance.INSTANCE
    
if __name__ == "__main__":
    sql = MySQLInstance("", "admin", "Papipooo456!")

    print(sql.getInstance())