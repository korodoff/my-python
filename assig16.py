# Q1- Create a database. Create the following tables:
# 1. Book
# 2. Titles
# 3. Publishers
# 4. Zipcodes
# 5. AuthorsTitles
# 6. Authors
# Refer to the diagram below

import pymysql as py

db=py.connect("localhost","root","amit9729231169","library")

book='create table book(book_id char(50),title_id char(50),location char(50),grene char(50))'
titles='create table titles(title_id int,title char(50),ISBN char(50),publisher_id int,publication_year int)'
publishers='create table publishers(publishers_id int,name char(50),street_address char(40),suite_number int,zip_code_id int)'
zip_codes='create table zip_codes(zip_codes_id int,city char(50),zip_codes int)'
authors_titles='create table authors_titles(authors_titles char(40),author_titles_id int,title_id int)'
authors='create table authors(authors_id int,first_name char(50),middle_name char(50),last_name char(50))'

cursor=db.cursor()

cursor.execute("drop table book")
cursor.execute("drop table zip_codes")
cursor.execute("drop table authors_titles")
cursor.execute("drop table authors")
cursor.execute("drop table publishers")
cursor.execute("drop table titles")
print(cursor.execute("show tables"))

cursor.execute(book)
cursor.execute(titles)
cursor.execute(publishers)
cursor.execute(zip_codes)
cursor.execute(authors_titles)
cursor.execute(authors)

print(cursor.execute("show tables"))

db.close()


#Q2- Insert values in the tables.

import pymysql as py

db=py.connect("localhost","root","****","library")
cursor=db.cursor()
cursor.execute("insert into book values(01,'adobe of cloud','meghalaya','india')")
cursor.execute("insert into titles values(2,'adventure in meghalaya','1005',201,2005)")
cursor.execute("insert into publishers values(203214,'nepoleon','nepal',132,2016)")
cursor.execute("insert into zip_codes values(793150,'shillong',793151)")
cursor.execute("insert into authors_titles values('150',13343,453435)")
cursor.execute("insert into authors values(6316050,'nongpohli','none','rymbai')")
cursor.execute("select * from book")
print(cursor.fetchall())
db.commit()
db.close()


#Q3- Update any values in any of the tables. Print the original and updated values.

import pymysql as py

db=py.connect("localhost","root","***","library")

cursor=db.cursor()
cursor.execute("select * from book")
show=cursor.fetchall()
print(show)
cursor.execute("update book set grene='helpful' where book_id=001 ")
cursor.execute("select * from book")
show=cursor.fetchall()
print(show)
db.commit()
db.close()