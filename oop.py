#1.create a class called Car with attributes brand and color.Instantiate an object of the car class and print its attributes
class car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        my_car = car("benz" ,"black" and "white")

        print(f"car brand:{my_car.brand},car_color:{my_car.color}")

        
#2.add a method called start_engine to the prints a message saying the engine of the car has started.create an instance of car and call the method.
class car:
    def ___init__(self,brand,color):
        self.brand = brand
        self.color = color

        def start_engine(self):
            print(f"The engine of the {self.color} {self.brand} has started ")
            my_car = car("benz" ,"black" and "white")
            my_car.start_engine()
     
#3.create a class called BankAccount with attributes account_number and balance. Add methods to:
#Deposit an amount.
#Withdraw an amount(only if sufficient balance exists)
#Print the account balance.
class BankAccount:
    def __init__(self, account_number, balance =0):
        self.account_number = account_number
        self.balance = balance

        def deposit(self, amount):
            self.balance += amount
            print(f"deposited{amount}.New balance: {self.balance}")

            def withdraw(self,amount):
                if amount > self.balance:
                    print("Insufficient balance!") 
                else:
                    self.balance -= amount
                    print(f"Withdrew {amount}.New balance: {self.balance}")

                    def  display_balance(self):
                       print(f"Account Number:{self.acount_number}, Balance:{self.balance}")

#4.Implement a class called Library that manages a collection of books. Each book has a title,author,and available status,.The Library class should have methods to:
#add a book to the library
#remove a book from the library
#check if a book is available by title
#borrow a book (mark it as unavailable if its available)
# return a book(mark it as available again if it was borrowed)class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = book(title, author)
        self.books.append(book)
        print(f"Added '{title}' by {author} to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Removed '{title}' from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    def check_availability(self, title):
        for book in self.books:
            if book.title == title:
                return f"'{title}' is {'available' if book.available else 'not available'}."
        return f"Book '{title}' not found in the library."

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print(f"You borrowed '{title}'.")
                else:
                    print(f"'{title}' is currently not available.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    print(f"Returned '{title}' to the library.")
                else:
                    print(f"'{title}' was not borrowed.")
                return
        print(f"Book '{title}' not found in the library.")

library = Library()
library.add_book("The Catcher in the Rye", "J.D. Salinger")
library.add_book("1984", "George Orwell")
print(f'library.check_availability("1984")')
library.borrow_book("1984")
print(f'library.check_availability("1984")')
library.return_book("1984")
print(f'library.check_availability("1984")')
