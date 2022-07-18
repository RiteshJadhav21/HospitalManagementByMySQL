import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.conn=connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='root',
                                    database='pythontest')
        query="create table if not exists user(patientId int primary key,patientName varchar(200), phone varchar(12))"
        cur=self.conn.cursor()
        cur.execute(query)
        print("created")

    #insert
    def insert_patient(self,patientid,patientname,phone):
        query="insert into user(patientId,patientName,phone) values({},'{}','{}')".format(patientid,patientname,phone)
        # print(query)
        cur=self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("user saved")



    #fetching

    def fetch_all(self):
        query="select * from user"
        cur = self.conn.cursor()
        cur.execute(query)
        for row in cur:
            print(row)

    #delete
    def delete_patient(self,userId):
        query="delete from user where patientId={}".format(userId)
        print(query)
        c=self.conn.cursor()
        c.execute(query)
        self.conn.commit()
        print("patient delete")



    #update
    def update_patient(self,patientId,patientName,newPhone):
        query="update user set patientName='{}',phone='{}' where patientId={}".format(patientName,newPhone,patientId)
        print(query)
        cur=self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("updated")
