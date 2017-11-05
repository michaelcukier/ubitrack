import MySQLdb


def connection():
    conn = MySQLdb.connect(host="localhost", user="root", passwd="cukier", db="pythonprogramming")
    c = conn.cursor()
    return c, conn
