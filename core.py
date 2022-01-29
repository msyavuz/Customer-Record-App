import sqlite3 as sql
import pandas as pd

def create_connect():
    db = sql.connect("customers.db")



    with db:
        db.execute("""
                CREATE TABLE IF NOT EXISTS CUSTOMERS (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    address TEXT,
                    item TEXT,
                    amount INTEGER,
                    uprice REAL,
                    tprice REAL
                    ); 
                """)
    
    return db


def insert_data(db,id,name,address,item,amount,unitp,totalp):
    command = 'INSERT INTO CUSTOMERS (id, name, address, item, amount, uprice, tprice) values(?,?,?,?,?,?,?)'
    cust = (id,name,address,item,amount,unitp,totalp)
    with db:
        db.execute(command,cust)
    

def delete_data(db,id):
    command = f"DELETE from CUSTOMERS where id={id} "
    with db:
        db.execute(command)
    

def get_posts(db):
    table = pd.read_sql_query(f"SELECT *FROM CUSTOMERS", db)
    return table




