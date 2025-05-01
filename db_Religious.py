import sqlite3
class libraryr:
    def __init__ (self,db_Religious):
        self.con=sqlite3.connect(db_Religious)
        self.cr=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS booksReligious (
        id Integer primary key,
        name text,
         Release_date text,
         Autor text,
         Publishing_house text,
         number_of_pages text,
         discraption text
        )"""
        
        self.cr.execute(sql)
        self.con.commit()

    def insert(self,name, Release_date,Autor,Publishing_house, number_of_pages,discraption) :
        self.cr.execute("insert into booksReligious values(NULL,?,?,?,?,?,?)",
                       (name, Release_date,Autor,Publishing_house, number_of_pages,discraption))
        self.con.commit()  

    def fetch(self):
        self.cr.execute("select *  from booksReligious")
        rows=self.cr.fetchall()
        return rows
    
    def remove(self,id):
        self.cr.execute("delete from booksReligious where id=?",(id,))
        self.con.commit()

    def update(self,name, Release_date,Autor,Publishing_house, number_of_pages,discraption,id) :
        self.cr.execute("update booksReligious set name=?,Release_date=?,Autor=?,Publishing_house=?,number_of_pages=?,discraption=? where id=?",
                        (name, Release_date,Autor,Publishing_house, number_of_pages,discraption,id))
        self.con.commit()