from database import mydb, mycursor
import webscraping

def addstudent():
    role_id=2
    print("\n")
    username = input(" STUDENT USERNAME : ").title()
    password = input(" PASSWORD : ")
    sql = "INSERT INTO users(username,password,role_id) VALUES (%s,%s,%s)"
    val = (username, password, role_id)
    mycursor.execute(sql, val)
    mydb.commit()
    print("\n")
    

    sql2="insert into student (user_id,name,course,semester,phone) values(%s,%s,%s,%s,%s)"
    userid=mycursor.lastrowid
    name=input("NAME    :").title()
    course=input("COURSE   :").upper()
    semester=int(input("SEMESTER :", ))
    phoneno=int(input("PHONE NO. : "))
    val1=(userid,name,course,semester,phoneno)
    mycursor.execute(sql2,val1)
    mydb.commit()

    print(f"\nSTUDENT-{name.upper()} ADDED SUCCESFULLY.")

def deletestudent():
    print("DELETING")
    username2=input("ENTER STUDENT USERNAME TO DELETE  :")
# Display student details using JOIN
    sql = "SELECT u.user_id, u.username, s.name FROM users u JOIN student s ON u.user_id = s.user_id WHERE u.username = %s"
    mycursor.execute(sql, (username2,))
    result = mycursor.fetchone()

    if result:
       print("\nStudent Found")
       print("-----------------")
       print("User ID      :", result[0])
       print("Username     :", result[1])
       print("Student Name :", result[2])
       print("-----------------")

   

       choice = input("\nDelete this student? (y/n): ")

       if choice.lower() == "y":
          user_id = result[0]

        # Delete from student table
          sql = "DELETE FROM student WHERE user_id = %s"
          mycursor.execute(sql, (user_id,))

        # Delete from users table
          sql = "DELETE FROM users WHERE user_id = %s"
          mycursor.execute(sql, (user_id,))

          mydb.commit()
          print("STUDENT DELETED SUCCESSFULLY..")

       else:
          print("DELETION CANCELLED..")

    else:
        print("STUDENT NOT FOUND..")


def addbook():
    print("\n")
    book_name=input("BOOK NAME :").title()
    author=input("AUTHOR :").title()
    publisher=input("PUBLISHER :").title()
    rating=float(input("RATING (e.g. 2.0):"))
    price=float(input("PRICE(e.g. 399.99):"))
    quantity=int(input("QUANITY :"))

    sql = "SELECT * FROM book1 WHERE book_name = %s"
    mycursor.execute(sql, (book_name,))
    result = mycursor.fetchone()

    if result:
        print("\nBOOK ALREADY EXIST")
    else:

         sql="INSERT INTO book1(book_name, author, publisher,rating,price, quantity) VALUES (%s,%s,%s,%s,%s,%s)"
         val1=(book_name,author,publisher,rating,price,quantity)
         mycursor.execute(sql,val1)
         mydb.commit()
         print(f"\n  BOOK:{book_name} by {author} ADDED SUCCESSFULLY")



def deletebook():
    print("\n")
    print("-----------------")
    book_id = int(input("Enter Book ID to delete : "))

    # Check if the book exists
    sql = "SELECT * FROM book1 WHERE book_id = %s"
    mycursor.execute(sql, (book_id,))
    result = mycursor.fetchone()

    if result:
        print("\nBOOK FOUND")
        print("-----------------")
        print("BOOK ID   :", result[0])
        print("BOOK NAME :", result[1])
        print("AUTHOR    :", result[2])
        print("PUBLISHER :", result[3])
        print("RATING    :", result[4])
        print("PRICE     :", result[5])
        print("QUANTITY  :", result[6])
        print("-----------------")
     

        ch = input("\nDo you want to delete this book? (y/n) : ")

        if ch.lower() == "y":
            sql = "DELETE FROM book1 WHERE book_id = %s"
            mycursor.execute(sql, (book_id,))
            mydb.commit()

            print("\nBOOK DELETED SUCCESSFULLY..")

        else:
            print("DELETION CANCELLED..")

    else:
        print("\nBOOK NOT FOUND..")
        print("-----------------")
    
def searchbook():
    print("-----------------")
    book_name=input("ENTER BOOK NAME :")
    sql="select * from book1 where book_name=%s"
    mycursor.execute(sql, (book_name,))
    result=mycursor.fetchone()

    if result:
        print("\nBOOK FOUND")
        print("-----------------")
        print("BOOK ID   :", result[0])
        print("BOOK NAME :", result[1])
        print("AUTHOR    :", result[2])
        print("PUBLISHER :", result[3])
        print("RATING    :", result[4])
        print("PRICE     :", result[5])
        print("QUANTITY  :", result[6])
        print("-----------------")
    else:
        print("BOOK NOT FOUND..")
        print("-----------------")
     
    mydb.commit()
 
def updatebook():
    print("-----------------")
    book_id = int(input("ENTER BOOK ID TO UPDATE: "))

    # Check if the book exists
    sql = "SELECT * FROM book1 WHERE book_id = %s"
    mycursor.execute(sql, (book_id,))
    result = mycursor.fetchone()

    if result:
        print("\nBOOK FOUND")
        print("-----------------")
        print("CURRENT BOOK NAME :", result[1])
        print("CURRENT AUTHOR    :", result[2])
        print("CURRENT PUBLISHER :", result[3])
        print("CURRENT RATING    :", result[4])
        print("CURRENT PRICE     :", result[5])
        print("CURRENT QUANTITY  :", result[6])
        print("-----------------")

        # Enter new details
        print("\n")
        print("---------------------")
        book_name = input("ENTER NEW BOOK NAME           : ").title()
        author = input("ENTER NEW AUTHOR                : ").title()
        publisher = input("ENTER NEW PUBLISHER          : ").title()
        rating=float(input(" ENTER NEW RATING (e.g. 2.0):"))
        price=float(input("ENTER NEW PRICE(e.g. 399.99) :"))
        quantity = int(input("ENTER NEW QUANTITY        : "))

        print("-----------------------")

        # Update query
        sql = "UPDATE book1 SET book_name=%s, author=%s, publisher=%s,rating=%s,price=%s, quantity=%s WHERE book_id=%s"
        values = (book_name, author, publisher,rating,price, quantity, book_id)
        mycursor.execute(sql, values)
        mydb.commit()

        print("\nBOOK UPDATED SUCCESSFULLY..")
    else:
        print("\nBOOK NOT FOUND..")
        print("-----------------")

def issuebook():
    print("-----------------")
    username = input("USERNAME : ")
    book_name = input("BOOK NAME : ")

    sql = " INSERT INTO issue_book (student_id, book_id, issue_date, due_date, status) SELECT s.student_id, b.book_id, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 15 DAY), 'Issued' FROM student s JOIN users u ON s.user_id = u.user_id JOIN book1 b ON b.book_name = %s WHERE u.username = %s"

    mycursor.execute(sql, (book_name, username))
    mydb.commit()

    sql1 = " SELECT u.username, b.book_name, ib.issue_date, ib.due_date FROM issue_book ib JOIN student s ON ib.student_id = s.student_id JOIN users u ON s.user_id = u.user_id JOIN book1 b ON ib.book_id = b.book_id WHERE u.username = %s AND b.book_name = %s"
    mycursor.execute(sql1, (username, book_name))
    result = mycursor.fetchone()

    if result:
        print("\nBOOK ISSUED")
        print("-----------------")
        print("STUDENT NAME :", result[0])
        print("BOOK NAME    :", result[1])
        print("ISSUE DATE   :", result[2])
        print("DUE DATE     :", result[3])
        print("-----------------")
        sql2="UPDATE book1 SET quantity = quantity - 1 WHERE book_name = %s"
        mycursor.execute(sql2, (book_name,))
        mydb.commit()
    else:
        print("\nBOOK ISSUE FAILED EITHER USERNAME OR BOOK IS NOT AVAILABLE..")
        print("-----------------")

def returnbook():
    print("-----------------")
    username = input("USERNAME  : ")
    book_name = input("BOOK NAME : ")

    # Find issue_id
    sql = " SELECT ib.issue_id FROM issue_book ib JOIN student s ON ib.student_id = s.student_id JOIN users u ON s.user_id = u.user_id JOIN book1 b ON ib.book_id = b.book_id  WHERE u.username = %s AND b.book_name = %s  AND ib.status = 'Issued'"

    mycursor.execute(sql, (username, book_name))
    result = mycursor.fetchone()

    if result:
        issue_id = result[0]

        # Insert into return table
        # alternative sql1 = "INSERT INTO return_book (issue_id, return_date, fine) SELECT issue_id, CURDATE(),CASE  WHEN CURDATE() > due_date THEN (DATEDIFF(CURDATE(), due_date) * 5) ELSE 0 END FROM issue_book WHERE issue_id = %s" mycursor.execute(sql1, (issue_id,))
        
        sql = "SELECT issue_id, due_date, book_id FROM issue_book WHERE issue_id = %s"
        mycursor.execute(sql, (issue_id,))  #result[0]=issue_id  return[1]=due date
        result = mycursor.fetchone()
        sql1 = "INSERT INTO return_book (issue_id, return_date, fine)VALUES (%s, CURDATE(),CASE WHEN CURDATE() > %s THEN DATEDIFF(CURDATE(), %s) * 5    ELSE 0 END)"
        mycursor.execute(sql1, (result[0], result[1], result[1]))
        mydb.commit()
        

        # Update issue status
        sql2 = " UPDATE issue_book SET status = 'Returned' WHERE issue_id = %s"
        mycursor.execute(sql2, (issue_id,))

        sql3="UPDATE book1 SET quantity = quantity + 1 WHERE book_name = %s"
        mycursor.execute(sql3, (book_name,))
        mydb.commit()

        print("\nBOOK RETURNED SUCCESSFULLY...")

    else:
        print("\nN0 ISSUED BOOK FOUND . EITHER STUDENT OR BOOK IS NOT AVAILABLE ..")
        print("-----------------")

def search():
    print("\n")
    print("-----------------")
    print("1.SEARCH BOOK BY STUDENT.")
    print("2.SEARCH STUDENT BY BOOK.")
    x=int(input("\nENTER SEARCH PROCEDURE:"))
    if(x==1):
        username=input("USERNAME :")
        sql="select b.book_name ,u.username,ib.due_date from book1 b join issue_book  ib on b.book_id=ib.book_id join student s ON ib.student_id = s.student_id join users u on u.user_id=s.user_id where u.username=%s"
        mycursor.execute(sql, (username,))
        result = mycursor.fetchall()
        if result:
            print(f"\nBOOKS FOUND : {len(result)}  ")
           

            for row in result:
                
                print("-----------------")
                print("BOOK NAME :", row[0])
                print("USER NAME :", row[1])
                print("DUE DATE  :", row[2])
                print("-----------------")
            
        else:
            print("\nBOOK NOT FOUND..")
            print("-----------------")
        
        
    elif(x==2):
        book_name=input("BOOK NAME :")
        sql1="select b.book_name ,u.username,ib.due_date from book1 b join issue_book  ib on b.book_id=ib.book_id join student s ON ib.student_id = s.student_id join users u on u.user_id=s.user_id where b.book_name=%s"
        mycursor.execute(sql1, (book_name,))
        result = mycursor.fetchall()
        if result:

           for row in result:
                print("\nSTUDENT FOUND ")
                print("-----------------")
                print("BOOK NAME :", row[0])
                print("USER NAME :", row[1])
                print("DUE DATE  :", row[2])
                print("-----------------")
        else:
            print("\nSTUDENT NOT FOUND..")
            print("-----------------")
    else:
        print("\nINVALID CHOICE..")  
        print("-----------------")  
        



def webscraping1():
    webscraping.webscraping()

    
