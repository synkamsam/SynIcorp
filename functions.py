import sqlite3 as sql3
def hello():
    print('you pressed me')

def call_dtb():
    conn = sql3.Connection('trans.db')
    csr = conn.cursor()

    




  