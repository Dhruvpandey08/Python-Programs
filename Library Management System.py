class Library:
    def __init__(self,listOfBooks):
        self.books=listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are:")
        for book in self.books:
            print(" *"+book)
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, this book has already been issued to someone else.")
            return False

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book!")
         
class student:
        def requestBook(self):
            self.book=input("Enter the name of the book you want to borrow")
            return self.book

        def reutrnBook(self):
             self.book=input("Enter the name of the book you want to return")
             return self.book

if __name__=="__main__":
    centralLibrary=Library(["Algorithms","Django","Clrs","Python Notes"])
    centralLibrary.displayAvailableBooks()
    student=student()
    while(True):
        welcomeMsg='''=======Welcome to Central Library====
        Please choose an option:
        1. Listing all the books
        2. Request a book
        3. Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a=int(input("Enter a choice:"))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.reutrnBook())
        elif a==4:
            print("Thanks for using this library! Have a great Day")
            exit()
        else:
            print("Invalid Choice!")