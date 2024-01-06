import sqlite3




class DB:
    def __init__(self, db_name: str):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        
    def __del__(self):
        self.cur.close()
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
        
    
    def add_student(self, name: str, age: int, major: str) -> tuple:
        self.cur.execute(f'''INSERT INTO students(name, age, major) 
        VALUES
            (?, ?, ?);''', 
        (name, age, major))
        
        self.con.commit()
        
        self.cur.execute('''SELECT * FROM students
            ORDER BY id DESC
            LIMIT 1;''')
        response = self.cur.fetchone()
        return response
    
    def add_course(self, course_name: str, instructor: str) -> tuple:
        self.cur.execute(f'''INSERT INTO courses(course_name, instructor) 
        VALUES
            (?, ?);''', 
        (course_name, instructor))
    
        self.con.commit()
        
        self.cur.execute('''SELECT * FROM courses
            ORDER BY course_id DESC
            LIMIT 1;''')
        response = self.cur.fetchone()
        return response    
        
    # def update_student(self, student_id: int, ):
    
    

if __name__ == "__main__":
    db = DB("db.db")
    db.create_tables()
    print(db.add_student(name="Maya", age=3000, major="calendar"))
    print(db.add_course("Math", "Starch"))
    