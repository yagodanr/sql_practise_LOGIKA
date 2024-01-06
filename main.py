import sqlite3


con = sqlite3.connect("db.db")


class DB:
    def __init__(self, db_name: str):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        
    def create_tables(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                major TEXT,
            );''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS courses(
                course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_name TEXT,
                instructor TEXT,
            );''')
        
        self.cur.execute('''CREATE TABLE IF NOT EXISTS relation(
                relation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INT,
                course_id INT,
                FOREIGN KEY(student_id) REFERENCES students(id),
                FOREIGN KEY(course_id) REFERENCES courses(course_id)
            );''')
        
    
    
    