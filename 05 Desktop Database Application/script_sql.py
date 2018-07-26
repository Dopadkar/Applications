import sqlite3

def create_table():
    # loading or creating a database-file
    conn = sqlite3.connect('lite.db')
    # create a cursor for connect with datavase
    cur = conn.cursor()
    
    # creating a table 'store' if it not exist
    cur.execute("CREATE TABLE IF NOT EXIST store (item TEXT, quantity INTEGER, price REAL)")

    # commit a datavase
    conn.commit()
    # closing a database
    conn.close()

def insert(item, quantity, price):
    # loading or creating a database-file
    conn = sqlite3.connect('lite.db')
    # create a cursor for connect with datavase
    cur = conn.cursor()
    
    # insert a new item and its data
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
    
    # commit a datavase
    conn.commit()
    # closing a database
    conn.close()

def view():
    # loading or creating a database-file
    conn = sqlite3.connect('lite.db')
    # create a cursor for connect with datavase
    cur = conn.cursor()

    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    
    # closing a database
    conn.close()
    return rows

def delete(item):
    # loading or creating a database-file
    conn = sqlite3.connect('lite.db')
    # create a cursor for connect with datavase
    cur = conn.cursor()
    
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    
    conn.commit()
    # closing a database
    conn.close()

def update(item, quantity):
    # loading or creating a database-file
    conn = sqlite3.connect('lite.db')
    # create a cursor for connect with datavase
    cur = conn.cursor()
    
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity,price,item))
    
    conn.commit()
    # closing a database
    conn.close()

delete('Juice Glass')
insert('Wine Glass', 12, 12.0)
rows = view()
print(rows)
insert('Wine Glass', 12, 12.0)


