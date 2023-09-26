from pymysql import connect


class DButils():
    def __init__(self):
        self.con = connect(user="root", password="123456", host="localhost", port=3306, db='a2306', charset='utf8')
        self.cursor = self.con.cursor()

    def queryuser(self, name, psd):
        sql = "SELECT * FROM user WHERE name= '%s' AND psd = '%s'" % (name, psd)
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        return res

    def querynews(self, id):
        sql = "select * from news where id='%s'" % id
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    def insertnews(self, id, title, content):
        sql = f"INSERT INTO news values ('{id}','{title}','{content}')"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        self.con.commit()
        return res

    def close(self):
        self.cursor.close()
        self.con.close()
