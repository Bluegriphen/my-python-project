# Example of Class Object
class Book:

    def __init__(self, Name, Author, Pages):
        self.Name = Name
        self.Author = Author
        self.Pages = Pages

    def display(self):
        print("Book Name = ",self.Name)
        print("Author  = " ,self.Author)
        print("Pages = " ,self.Pages)
        print("\n")



Number = int(input("How many books You want to add : "))

books = []
for i in range(Number):
    Name = input("Enter Book Name : ")
    Author = input("Enter Author Name : ")
    Pages = input("Enter Pages : ")
    
    book = Book(Name, Author, Pages)
    books.append(book)

print("\nooks Details : \n")
for Book in books:
   Book.display()