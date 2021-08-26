class Library:
    def __init__(self , listofbooks):
        self.books = listofbooks

    def displayAvailableBooks(self):
        print("Books present in this library are : ")
        for book in self.books:
            print(" ~ " + book)

    def borrowBook(self , bookName):
        if bookName in self.books:
            print(f"you have been issued this book {bookName} , please handle it with care!")
            self.books.remove(bookName)         #if borrowing the book toh boook ko remove kardera
            return True
        else:
            print("this book is not available or has already been issued")
            return False

    def returnBook(self , bookName):
        self.books.append(bookName)
        print("thanks for reading this book!")

class Student:
    def reqBook(self):
        self.book = input("Enter the name of the book you want to request : ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return : ")
        return self.book


if __name__ == "__main__":

    CentralLibrary = Library(["django" , "python" , "BOOKS" , "mathematics"])
    # CentralLibrary.displayAvailableBooks()
    student  =  Student()
    
    while(True):
        welcomeMsg = ''' \n~~~~~~~~~~~~~  WELCOME TO CENTRAL LIBRARY  ~~~~~~~~~~~~~~~
        please choose an Option
        1. List all the books
        2. request a book
        3. return a book 
        4. Exit
        '''
        print(welcomeMsg)
        a = int(input("Enter your choice : "))
        if a ==1 :
            CentralLibrary.displayAvailableBooks()
        elif a==2:
            CentralLibrary.borrowBook(student.reqBook())
        elif a==3:
            CentralLibrary.returnBook(student.returnBook())   
        elif a==4:
            print("thanks for using central library!")
            exit()
        else:
            ("invalid choice")

        