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
        self.cur.execute('''INSERT INTO students(name, age, major) 
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
        self.cur.execute('''INSERT INTO courses(course_name, instructor) 
        VALUES
            (?, ?);''', 
        (course_name, instructor))
    
        self.con.commit()
        
        self.cur.execute('''SELECT * FROM courses
            ORDER BY course_id DESC
            LIMIT 1;''')
        response = self.cur.fetchone()
        return response    
        
    def connect_student_to_course(self, student_id: int, course_id: int):
        self.cur.execute('''INSERT INTO relation(student_id, course_id)
                         VALUES
                            (?, ?)''', 
                        (student_id, course_id))

        self.con.commit()
    
    def get_all_students(self) -> tuple[tuple]:
        self.cur.execute('''SELECT * FROM students''')
        return self.cur.fetchall()
    
    def get_all_courses(self) -> tuple[tuple]:
        self.cur.execute('''SELECT * FROM courses''')
        return self.cur.fetchall()
    
    def get_course_id_by_name(self, course_name: str) -> int:
        self.cur.execute('''SELECT id FROM courses WHERE course_name=?''', (course_name,))
        return self.cur.fetchone()
    
    def get_students_on_course(self, course_id: int):
        self.cur.execute('''SELECT * FROM students WHERE id IN (SELECT student_id FROM relation WHERE course_id=?)''', (course_id,))
        return self.cur.fetchall()

if __name__ == "__main__":
    db = DB("db.db")
    db.create_tables()
    # print(db.add_student(name="Maya", age=3000, major="calendar"))
    # print(db.add_course("Math", "Starch"))
    # db.connect_student_to_course(1, 1)
    
    print()
    print(db.get_all_students())
    print(db.get_all_courses())
    print(db.get_students_on_course(1))
    