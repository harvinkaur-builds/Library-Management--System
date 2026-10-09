from database import mydb, mycursor

def viewbooks(username):
    
    sql1 = " SELECT u.username, b.book_name, ib.issue_date, ib.due_date ,r.fine FROM issue_book ib  JOIN student s ON ib.student_id = s.student_id  JOIN users u ON s.user_id = u.user_id JOIN book1 b ON ib.book_id = b.book_id LEFT  JOIN return_book r ON ib.issue_id= r.issue_id WHERE    u.username = %s AND ib.status='Issued'"

    mycursor.execute(sql1, (username, ))
    result = mycursor.fetchall()

    if result:
        print(f"\nBOOK ISSUED {len(result)}")
        print("STUDENT NAME :", username.title())
        for row in result:
            
            print("-----------------")
            print("BOOK NAME    :", row[1])
            print("ISSUE DATE   :", row[2])
            print("DUE DATE     :", row[3])
            print("FINE         :",row[4])
            print("-----------------")
    else:
            print("\nNO BOOK FOUND..")
            print("-----------------")

def searchbook():
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
        print("\nBOOK NOT FOUND..")
        print("-----------------")
     
    mydb.commit()
