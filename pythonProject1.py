#python crash course
#course helper project


import sqlite3 as lite


# functionality goes here

class DatabaseManage(object):
    
    def __init__(self):
        global con
        try:
            con = lite.connect('courses.db')
            with con: 
                cur = con.cursor()    #cursor talk with db
                cur.execute("Create Table if NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 0)")

        except Exception:
            print("oops!!! Unable to create a Database!!")
    
    #TODO: create data
    def insert_data(self, data):
        #wrap your code in try and catch
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO course(name, description, price, is_private) VALUES (?,?,?,?)", data
                    )
                return True
        except Exception:
            return False

    #TODO: read data
    def fetch_data(self):
        try: 
            with con:
                cur = con.cursor()
                sql = "SELECT * FROM course"
                cur.execute(sql)
                return cur.fetchall()
        except Exception:
            return False

    #TODO: delete data
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = " DELETE FROM course WHERE id = ?"
                cur.execute(sql, [id])
                return True
                
        except Exception:
            return False
        
        
# TODO: provide interface to user

def main():
    print("*"*50)
    print("\n: COURSE MANAGEMENT::\n")
    print("*"*50)
    print("\n")
    
    db = DatabaseManage()
    
    print("$"*50)
    print("\n :: User Manual :: \n")
    print("$"*50)
    
    print("\n1. Insert a new Course\n")    
    print("2. Show all Course\n")
    print("3. Delete a course(NEED ID of COURSE)\n")
    print("$"*50)
    print("\n")
    
    choice = input("\n ENter a choice: ")
    if choice == "1":
        name = input("\n Enter course name: ")
        description = input("\n Enter description of course: ")
        price = input("\n Enter the price : ")
        private = input("\n Is this course private(0/1): ")
        
        if db.insert_data([name, description, price, private]):
            print("Course added Successfully! ")
        else:
            print("OOPS!! Something is wrong")
    
    elif choice == "2":
        print("\n:: Course List ::")
        
        for index, item in enumerate(db.fetch_data()):
            print("\nSr NO : " + str(index + 1))
            print("Course ID : " + str(item[0]))
            print("Course Name : " + str(item[1]))
            print("Course Description : " + str(item[2]))
            print("Course Price : " + str(item[3]))
            private = 'Yes' if item[4] else 'NO'
            print("Is Private : " + private)
            print("\n")
            
    elif choice == "3":
        course_id = input("Enter the course Id: ")
        
        if db.delete_data(course_id):
            print("Delete Successful!!!")
        else: 
            print("OOPS!!! Something is wrong")
            
            
    else:
        print("\n WRONG CHOICE!!")
        
        
if __name__ == '__main__':
    main() 