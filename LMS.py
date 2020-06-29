#Library Management System

#BLL
import pickle
class Student:
    booklist=[]
    def __init__(self):
        self.bookname=0
        self.bookid=0
        self.studentname=""

    def addbook(self):
        Student.booklist.append(self)

    def searchbook(self):
        for book in Student.booklist:
            if(book.bookname==self.bookname):
                self.bookname=book.bookname
                self.studentname=book.studentname
                print("The book you requested has now been borrowed")
            else :
                print ( "Sorry the book you have requested is currently not in the library" )

    def deletbook(self):
        for e in Student.booklist:
            if(e.bookname==self.bookname):
                Student.booklist.remove(e)
                return
    def reissuebook( self ):
        Student.booklist.append(self)


    def savetoPickle():
        f=open("D://cetpa//mypickle.txt","wb")
        pickle.dump(Student.booklist,f)
        f.close()

    def loadfromPickle():
        f = open("D://cetpa//mypickle.txt", "rb")
        Student.booklist=pickle.load(f)
        f.close()


#Presentation Layer

def displayall():
    for book in Student.booklist:
        print("BOOKNAME : ",book.bookname, "BOOK ID : ",book.bookid, "STUDENT NAME : ",book.studentname)
    def reissuebook (self ):
        print ( "Enter the name of the book you'd like to return>>" )
        self.book = input ( )
        return self.book

while(1):
    print ("1 to Return Book")
    print ( "2 to Issue Book" )
    print ( "3 to Search Book" )
    print ( "4 to Reissue Book" )
    print( "5 to Display All")
    print ( "6 save to pickle" )
    print ( "7 load from pickle" )
    print ( "8 to exit" )
    c = int(input("Enter Your Choice : "))
    if(c == 1): #Return Book
        book=Student()
        book.bookname=int(input("Enter Book Name : "))
        book.bookid=int(input("Enter Book ID : "))
        book.studentname=input("Enter Student Name : ")
        book.addbook()
    elif(c==2): #Issue Book
        book=Student()
        book.bookname=int(input("Enter Book Name : "))
        book.deletbook()
        print("Book Issued Successfully")
    elif(c==3): #Search Book
        book = Student( )
        book.bookname = int ( input ( "Enter Book Name : " ) )
        book.searchbook ( )
        print ( "BOOKNAME : " , book.bookname , "BOOK ID : " , book.bookid , "STUDENT NAME : " , book.studentname )
    elif(c==4): # Reissue Book
        book = Student ()
        book.bookname = int ( input ( "Enter Book Name : " ) )
        book.reissuebook()
        print(" Book Reissued Successfully")
    elif(c==5):
        displayall()
    elif (c == 6):
        Student.savetoPickle()
    elif (c == 7):
        Student.loadfromPickle()
    elif (c == 8):
        exit ( )
