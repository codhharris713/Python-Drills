import sqlite3

conn = sqlite3.connect('test.db')
#creat table called filename
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_filename(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT)")
    conn.commit()

conn = sqlite3.connect('test.db')
#list of file names
file_list = ('information.docx', 'Hello.txt', 'myImage.png', \
             'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#loop through each object to find files that end in .txt
for x in file_list:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            #insert .txt files into table_filename
            cur.execute("INSERT INTO tbl_filename(col_fname) VALUES (?)",(x,))
            print(x)

conn.close()
