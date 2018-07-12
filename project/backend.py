import sqlite3

def connect():
    con= sqlite3.connect("ruth.db")
    cu = con.cursor()
    cu.execute("CREATE TABLE IF NOT EXISTS "
                    "book (id integer PRIMARY KEY, "
                            "title text, "
                            "author text, "
                            "year integer, "
                            "isbn integer)")
    con.commit()
    con.close()

def insert(title, author, year, isbn):
    con = sqlite3.connect("ruth.db")
    cu = con.cursor()
    cu.execute("INSERT INTO book "
                    "VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("ruth.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    con.close()
    return rows

def update(id, title, author, year, isbn):
    con = sqlite3.connect("ruth.db")
    cur = con.cursor()
    cur.execute("UPDATE book "
                    "SET title = ?, "
                    "author = ?, "
                    "year = ?, "
                    "isbn = ? "
                    "WHERE id = ?", 
                    (title, author, year, isbn, id))
    con.commit()
    con.close()

def delete(id):
    con = sqlite3.connect("ruth.db")
    cur = con.cursor()
    cur.execute("DELETE FROM book "
                    "WHERE id = ?", (id,))
    con.commit()
    con.close()

def search(title = "", author = "", year = "", isbn = ""):
    con = sqlite3.connect("ruth.db")
    cur = con.cursor()
    cur.execute("SELECT * "
                    "FROM book "
                    "WHERE title = ? OR author = ? OR year = ? OR isbn = ?", 
                    (title, author, year, isbn))
    rows = cur_obj.fetchall()
    con.close()
    return rows
def exit():
	result=messagebox.askyesno("alert,""are you sure")
	if result==true:
		sys.exit()
	else:
		pass
    
connect()