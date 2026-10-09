from database import mydb, mycursor
import requests
from bs4 import BeautifulSoup
import csv
import time

#print(response.status_code)  #200 means correct value
#list to store all books


def webscraping():
    all_books_data=[]

    '''
     for page_num in range(1,21):
            url=f"https://books.toscrape.com/catalogue/page-{page_num}.html"
            print(f"SCRAPING PAGE {page_num} : {url}")
            response=requests.get(url)
    
            if response.status_code!=200:
                print(f"PAGE {page_num} NOT FOUND.stopping")
                break
    
            soup=BeautifulSoup(response.content,"html.parser")
            all_books_on_page = soup.find_all("article", class_="product_pod")
    
            for book in  all_books_on_page:
                title=book.h3.a["title"]
                price=book.find("p",class_="price_color").text.replace("£","")
                rating=book.p["class"][1]
                
                #add in dictionary
                book_info={
                    "title":title,
                    "price":price, 
                    "rating":f"{rating} stars"
                    }
                all_books_data.append(book_info)
    
    
    #time delays so server donot gets overloaded
            print(f"PAGE {page_num} SCRAPED.WAITING 1 SECOND")
            time.sleep(1)
    print("TOTAL BOOKS:", len(all_books_data))

    
     #store in csv (comma separated value) file)  utf-8 is for characters
    with open ("book.csv","w",newline="",encoding="utf-8") as file:
        headers=["title","price","rating"]
    
        writer=csv.DictWriter(file,fieldnames=headers)
    
        writer.writeheader()    
        writer.writerows(all_books_data)
    
    
    '''
    #check book in database
    found=False
    print("-----------------")
    book_name=input("\nENTER BOOK NAME :").lower().strip()
    print("-----------------")
    sql = "SELECT book_id FROM book1 WHERE lower(book_name) = %s"
    mycursor.execute(sql, (book_name,))
    result = mycursor.fetchone()
    
    if result:
         print("\nBOOK ALREADY EXISTS IN DATABASE")
    
    else:
    
        for page_num in range(1,21):
            url=f"https://books.toscrape.com/catalogue/page-{page_num}.html"
           # print(f"SCRAPING PAGE {page_num} : {url}")
            response=requests.get(url)
    
            if response.status_code!=200:
                print(f"PAGE {page_num} NOT FOUND.stopping")
                break
    
            soup=BeautifulSoup(response.content,"html.parser")
            all_books_on_page = soup.find_all("article", class_="product_pod")
    
            for book in  all_books_on_page:
                title=book.h3.a["title"]
                
                if book_name.lower()== title.lower():
                    price=book.find("p",class_="price_color").text.replace("£","")
                    rating_dict = {
                        "One": 1.0,
                        "Two": 2.0,
                        "Three": 3.0,
                        "Four": 4.0,
                        "Five": 5.0
                        }
                    rating=rating_dict[book.p["class"][1]]
                    found=True
                    break
         #stop page loop
            if found:
                break   
    
                
        if found:
                print("-----------------")
                print("\nINSERTING..")
                print("-----------------")
                sql="insert into book1( book_name , author , publisher , rating , price , quantity  ) values(%s,%s,%s,%s,%s,%s)"
                val=(title,"unknown","unknown",rating,float(price),3)
                mycursor.execute(sql, val)
                mydb.commit()
                
                #fetch inserted book
                sql2="select book_name,rating,price,quantity from book1 where lower(book_name)=%s"
                mycursor.execute(sql2,(title.lower(),))
                result = mycursor.fetchone()
    
                if result:
                    
                    print("\nBOOK IMPORTED SUCCESSFULLY..")
                    print("-----------------")
                    print("BOOK NAME  :", result[0])
                    print("RATING     :", result[1])
                    print("PRICE      :", result[2])
                    print("QUANTITY   :", result[3])
                    print("-----------------")
                mydb.commit()
        else:
            print("\n BOOK NOT FOUND ON WEBSITE.")
            print("-----------------")
#webscraping()