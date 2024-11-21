#1.create a class called Car with attributes brand and color.Instantiate an object of the car class and print its attributes
class car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        my_car = car("benz" ,"black" and "white")

        print(f"car brand:{my_car.brand},car_color:{my_car.color}")

        
#2.add a method called start_engine to the prints a message saying the engine of the car has started.create an instance of car and call the method.
class car:
    def __init__(self,brand,color):
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

                    

#4.Implement a class called Library that manages a collection of books. Each book has a title,author,and available status,.The Library class should have methods to:
#add a book to the library
#remove a book from the library
#check if a book is available by title
#borrow a book (mark it as unavailable if its available)
# return a book(mark it as available again if it was borrowed)