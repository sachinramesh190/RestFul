import sqlite3
from sqlite3 import Error
import os
import pymysql
def connect():
    db = pymysql.connect(host=os.getenv("MYSQL_SERVICE_HOST"), user='root', 
                         password=os.getenv("db_root_password"), database=os.getenv("db_name"))
    return db

def get_all_users():
    conn = connect()
    if not conn:
        return None
    cur = conn.cursor()
    cur.execute('select id, name from Users')
    users = [dict(id=row[0], user_name=row[1]) for row in cur.fetchall()]
    cur.close()
    return users

def get_user_by_id(user_id):
    conn = connect()
    if not conn:
        return None
    cur = conn.cursor()
    cur.execute('select id, name from Users where id = %s', [user_id])
    users = [dict(id=row[0], user_name=row[1]) for row in cur.fetchall()]
    cur.close()
    if users:
        return users[0]    
    return None

def create_table():
    conn = connect()
    if not conn:
        return None
    sql = """
        CREATE TABLE IF NOT EXISTS `Users` (
        `id` int NOT NULL AUTO_INCREMENT,
        `name` varchar(45) DEFAULT NULL,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;
    """

    conn.cursor().execute(sql) 
    conn.commit()
    conn.close()

def delete_table():
    conn = connect()
    if not conn:
        return None
    conn.cursor().execute("Delete from Users") 
    conn.commit()
    conn.close()

def add_user(name):
    sql = "INSERT INTO Users (name) VALUES(%s);"
    conn = connect()
    if not conn:
        return None
    cur = conn.cursor()
    cur.execute(sql, (name,))
    id = cur.lastrowid
    conn.commit()
    conn.close()
    return id
