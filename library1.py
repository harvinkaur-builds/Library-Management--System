#new    with database,adminmodule ,studentmodule,webscraping modules(python files)
import adminmodule
import studentmodule
from database import mydb, mycursor
from datetime import date

def admin1():  
    while(True):
        #print("1.LOGIN")
        print("\n")
        print("==ADMIN MENU==")
        print("1. ADD STUDENT")
        print("2. DELETE STUDENT")
        print("3. ADD BOOK(MANUALLY)")
        print("4. UPDATE BOOK")
        print("5. SEARCH BOOK") 
        print("6. DELETE BOOK")
        print("7. ISSUE BOOK")
        print("8. RETURN BOOKS")
        print("9. SEARCH  STUDENT  BY BOOK OR BOOK BY STUDENT")
        print("10. IMPORT BOOK FROM WEBSITE")
        print("11. EXIT")
        print("=========")
        print("\n")
        a=int(input(" ENTER CHOICE :"))
        if a==1:
            
           adminmodule.addstudent()
        elif a==2:
           adminmodule.deletestudent()
        elif a==3:
            adminmodule.addbook()
        elif a==4:
            adminmodule.updatebook()       
        elif a==5:
            adminmodule.searchbook()
        elif a==6:
            adminmodule.deletebook()
        elif a==7:
            adminmodule.issuebook()
        elif a==8:
            adminmodule.returnbook()
        elif a==9:
            adminmodule.search()
        elif a==10:
            adminmodule.webscraping1()    
        elif a==11:
            print("\nLOGGING OUT...")
            print("-----------------")
            break
        
        else:
            print("\nINAVLID CHOICE..")
            print("-----------------")



def student():
    
        print("\n==STUDENT MENU==\n")

        username = input("STUDENT USERNAME  : ")
        sql="select * from users where username=%s "
        # password = input("STUDENT PASSWORD  : ")
        
        #sql="select * from users where username=%s AND password=%s"
        
        mycursor.execute(sql, (username,))
        result=mycursor.fetchone()

        if result:
            print("\n YES,THIS USERNAME EXISTS\n")
            password = input("STUDENT PASSWORD  : ")
            print("===============")
            #sql="select * from users where username=%s AND password=%s"
            #mycursor.execute(sql, (username, password))
            
            print("\nLOGIN SUCCESSFUL..")
            while(True):
                print("\n")
                print("-----------------")
                print("1. VIEW ISSUED BOOKS ")
                print("2. SEARCH BOOK")
                print("3. EXIT") 
                print("-----------------")
                print("\n")
                a=int(input(" ENTER CHOICE :"))

                if a==1:
                   studentmodule.viewbooks(username)
        
                elif a==2:
                   studentmodule.searchbook()
                    
                elif a==3:
                    print("\n LOGGING OUT...")  
                    break

                else:
                    print("\nINAVLID CHOICE..")
                    print("-----------------")
        
        else:
            print("\n THIS USERNAME EITHER DOESNOT EXIST OR NOT ISSUED ANY BOOK.")
     




while True:

    print("\n===LIBRARY MANAGEMENT===")
    print("1. ADMIN")
    print("2. STUDENT")
    print("3. EXIT")
    print("===========================")
    
    ur_role = int(input("ENTER CHOICE : "))
    print("-----------------")

    if ur_role == 1:
        admin_username="admin"
        admin_password="12345"
        username1 = input("ADMIN USERNAME : ").lower()
        password1 = input("ADMIN PASSWORD : ")
        print("-----------------")
        if (username1==admin_username) and (password1== admin_password):
            print("\nLOGIN SUCCESSFUL.. WELCOME")
            print("-----------------")
            admin1()
            
            
        else:
            print("\nINVALID USERNAME OR PASSWORD..")
            print("-----------------")

    elif ur_role == 2:
        student()
    elif ur_role==3:
        print("\n==THANK YOU FOR USING LIBRARY MANAGEMENT SYSTEM==")
        break

    else:
        print("\nINVALID ROLE..")
        print("-----------------")