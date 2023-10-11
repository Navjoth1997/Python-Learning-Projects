

# Write a Library class with no_of_books and books as two instance variables. 
# Write a program to create a library from this Library class and show how you can print all books, 
# add a book and get the number of books using different methods.


books = []
total_Count_of_books = 0
class Library:
    def __init__ (self,name,count_of_books):
        self.name = name
        self.no_of_books = count_of_books
        print(f"\nThe Book name is {self.name} and Qunatity stored is {self.no_of_books}\n")

B=int(input("Please enter the how many books data you wants to store:"))

for i in range(0,B):
     C= str(input("Please enter the book name:"))
     books.append(C)
     D=int(input("Please enter Quantity of books:"))
     total_Count_of_books += 0 + D 
     a=Library(C,D)

print(f"Books stored in Library are: {books}")
print(f"the total count of all book stores is: {total_Count_of_books}")










