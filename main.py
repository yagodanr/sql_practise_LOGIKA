import sqlite3
import models




class DB:
    def __init__(self, db_name: str):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        
    def __del__(self):
        self.con.close()
    
    
    def create_tables(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                major TEXT
            );''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS courses(
                course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_name TEXT,
                instructor TEXT
            );''')
        
        self.cur.execute('''CREATE TABLE IF NOT EXISTS relation(
                relation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INT,
                course_id INT,
                FOREIGN KEY(student_id) REFERENCES students(id),
                FOREIGN KEY(course_id) REFERENCES courses(course_id)
            );''')
        
    
    def add_student(self, name: str, age: int, major: str):
        self.cur.execute(f'''INSERT INTO students(name, age, major) 
        VALUES
            (?, ?, ?);''', 
        (name, age, major))
        
        self.con.commit()
    
    def add_course(self, course_name: str, instructor: str):
        self.cur.execute(f'''INSERT INTO courses(course_name, instructor) 
        VALUES
            (?, ?);''', 
        (course_name, instructor))
        
        self.con.commit()
    
    

if __name__ == "__main__":
    db = DB("db.db")
    db.create_tables()
    db.add_student(models.StudentCreate(name="Maya", age=3000, major="calendar"))
    