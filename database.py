import sqlite3
from  datetime import datetime

def create_gymdata():

    conn = sqlite3.connect('gym_data.db')  
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS gym_data (
        id INTEGER PRIMARY KEY, 
        day TEXT ,
        arms_lift INTEGER,
        arms_series INTEGER,
        running_time INTEGER,
        num_pushups INTEGER , 
        legs_lift INTEGER, 
        legs_series INTEGER
        
    )
    ''')
    return conn, cursor


def arms_data_insert(conn,cursor,arms_lift,arms_series):
    date=datetime.now().strftime("%d-%m-%Y")
    cursor.execute('''INSERT INTO gym_data (day,arms_lift,arms_series) VALUES (?,?,?)''', (date,arms_lift,arms_series))
    conn.commit()


def running_data_insert(conn,cursor,running_time):
    date=datetime.now().strftime("%d-%m-%Y")
    cursor.execute('''INSERT INTO gym_data (day,running_time) VALUES (?,?)''', (date,running_time))
    conn.commit()
    

def pushups_data_insert(conn,cursor,num_pushups):
    date=datetime.now().strftime("%d-%m-%Y")
    cursor.execute('''INSERT INTO gym_data (day,num_pushups) VALUES (?,?)''', (date,num_pushups))
    conn.commit()


def legs_data_insert(conn,cursor,legs_lift,legs_series):
    date=datetime.now().strftime("%d-%m-%Y")
    cursor.execute('''INSERT INTO gym_data (day,legs_lift,legs_series) VALUES (?,?,?)''', (date,legs_lift,legs_series))
    conn.commit()

def get_arms_data(cursor):
    cursor.execute('''SELECT arms_lift,arms_series FROM gym_data''')
    arms_data=cursor.fetchall()
    unziped=list(zip(*arms_data))
    return unziped[0],unziped[1]

def get_running_data(cursor):
    cursor.execute('''SELECT running_time FROM gym_data''')
    arms_data=cursor.fetchall()
    unziped=list(zip(*arms_data))
    return unziped[0]

def get_pushups_data(cursor):
    cursor.execute('''SELECT num_pushups FROM gym_data''')
    arms_data=cursor.fetchall()
    unziped=list(zip(*arms_data))
    return unziped[0]

def get_legs_data(cursor):
    cursor.execute('''SELECT legs_lift,legs_series FROM gym_data''')
    arms_data=cursor.fetchall()
    unziped=list(zip(*arms_data))
    return unziped[0],unziped[1]

def get_date(cursor):
    cursor.execute('''SELECT day FROM gym_data''')
    arms_data=cursor.fetchall()
    unziped=list(zip(*arms_data))
    return unziped[0]



