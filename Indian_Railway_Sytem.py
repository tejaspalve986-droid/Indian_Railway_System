# Defining Variables for Indain Railway System -------------------

train_name ="Rajdhani Express"
train_number = 12031
ticket_price = 2450.50
is_ac_available = True 
seat_number = [1,2,3,4,5]

# Showing the Deatails using print Functions ----------------------

# print("Train Name : ",train_name)
# print("Train Number : ",train_number)
# print("Ticket Price : ",ticket_price)
# print("AC Availability : ",is_ac_available)
# print("Seat Numbers : ",seat_number)

# Show the data types for the Varaibles using the Type Functions ---

# print("The data type of Train Name :",type(train_name))
# print("The data type of Train Number :",type(train_number))
# print("The data type of Ticket Price :",type(ticket_price))
# print("The data type of Is_ac_ Available :",type(is_ac_available))
# print("The data type of Seat Numbers :",type(seat_number))

# Getting passenger Information # ---------------------------------

# print("===  INDIAN RAILWAY BOOKING SYSTEM  ===")
# passenger_name =input("ENTER PASSENGER NAME :")
# age = int(input("ENTER AGE :"))
# destination = input("ENTER DESTINATION :")

# # display boooking confirmation ---------------------------------

# print("\n=== BOOKING DETAILS ===")
# print(f"Passenger :{passenger_name}")
# print(f"Age :{age}")
# print(f"Destination :{destination}")
# print("Booking confirmed !")

# Arthimetic Operator ---------------------------------------------

# base_price =1500
# service_charge = 100
# total_price = base_price + service_charge

# print(f"Base Price :₹{base_price}" )
# print(f"Service Charge :₹{service_charge}")
# print(f"Total Price :₹{total_price}")

# Comparision Operators -------------------------------------------

# passenger_age = 25
# senior_citizen_age = 60
# is_senior = passenger_age >= senior_citizen_age

# print(f"\n Is Passenger is Senior Citizen ? {is_senior}")

# Logical Operator ------------------------------------------------

# has_ticket = True
# has_id_proof = True
# can_board = has_ticket and has_id_proof

# print(f"Can Board Train ? {can_board}")

# Conditional statemants -------------------------------------------

# Control Flow - If statements ------------------------------------

# Age base Price ---------------------------------------------------

# Age = int(input("Enter Passenger Age : "))

# if Age < 5 :
#     price = 0
#     category = " Infant (Free )"
# elif Age < 12 :
#     price =750
#     category = "Child (50% Discount)"
# elif Age >= 60 :
#     price = 1200
#     category ="Senior Citizens (20% Discount)"
# else  :
#     price =1500
#     category = "Adult"

# print(f"category : {category}")
# print(f"Ticket Price : ₹{price}")

# Loops -----------------------------------------------------------

# For Loop - Display Available Trains

# trains = [
#     {"name":"Rajdhani Express",
#      "number":12301,
#     "destination":"New Delhi"},
#     {"name":"Shatapdi Express",
#      "number":12001,
#     "destination":"Chennai"} ,
#     {"name":"Duronto Express",
#      "number":12291,
#     "destination":"Mumbai"} ,
#     {"name":"Deccan Express",
#      "number":12221,
#     "destination":"Pune"} 
# ]

# print("AVAILABLE TRAINS : ")
# for trains in trains :
#     print(f"{trains["number"]}-{trains["name"]}-{trains["destination"]}")

# # While Loop - Booking System Menu

# print("\n=== BOOKING MENU ===")
# choice = 0

# while choice != 3:
#     print("1 . Book Ticket")
#     print("2. Check Status")
#     print("3. Exit")
#     choice = int(input("Enter Your Choice : "))

#     if choice == 1:
#         print("Booking Ticket .................")
#     elif choice == 2:
#         print("Checking Status ................" )
#     elif choice == 3:
#         print("Thank You For Using Indian Railways !")
#     else:
        # print("Invalid Choice ! ----------------")

# Ticket Price Calculator

# def calculated_ticket_price(distance,class_type):
#     base_rate = 0.5

#     if class_type == "Sleeper":
#         multiplier = 1.0
#     elif class_type == "AC 3 Tier":
#         multiplier = 2.0
#     elif class_type == "AC 2 Tier":
#         multiplier = 2.5
#     elif class_type == "AC 1 Tier":
#         multiplier = 3.0
#     else:
#         multiplier = 1.0
#     price = distance * base_rate * multiplier

#     return round(price,2)

# distance = 500
# Class_type = "Sleeper"
# price = calculated_ticket_price(distance,Class_type)

# print(f"Price for {distance}km in {Class_type} : ₹{price}")


# Ticket Booking -----------------------------------------------------------------------

# def book_ticket(passenger_name,age,destination,class_type = "Sleeper"):
#     Ticket = {
#         "Passenger Name" : passenger_name,
#         "Age" : age,
#         "Destination" : destination,
#         "Booking ID" :f"BK{hash(passenger_name)% 10000:04d}"
#     }
#     return Ticket

# def get_passenger_details(*args,**kwargs):
#     print("Positional arguments : ",args)
#     print("Keyword arguments : ",kwargs)


# ticket1 = book_ticket("Samyak Ubale",22,"Goa","AC 1 tier")
# ticket2 = book_ticket("Priya Singh",21,"Delhi","AC 3 tier")

# print("\nTicket 1 : ",ticket1)
# print("\nTicket 2 : ",ticket2)

# get_passenger_details("Samyak",22,"Goa",class_type = "AC 1 tier",Meal_Preference = "NON-VEG")

# Calculate Discounts _______________________________________________________________________

# calculate_discounts = lambda price, discount_percentage : price * (1- discount_percentage/100)

# original_price = 1500

# discounted_price = calculate_discounts(original_price,20)

# print(f"Oiginal :₹{original_price}, Discounted Price :₹{discounted_price}")

# train = [
#     {"name":"rajdhani","price":2500,"duration":16},
#     {"name":"shatabdi","price":1800,"duration":8},
#     {"name":"Duronto","price":2000,"duration":12},
# ]

# # map------------------------------------------------------------------------------------------------

# train_name = list(map(lambda x : x['name'],train))
# print(f"\n Train Names :{train_name}")

# # Filter------------------------------------------------------------------------------------------------

# affordale_trains = list(filter(lambda x: x['price']<2200,train))

# print("Affordable Trains :",[t["name"] for t in affordale_trains])

# # Sorted ------------------------------------------------------------------------------------------------

# sorted_by_price = sorted(train,key=lambda x:x["price"])
# print("Sorted By price : ",[t["name"]for t in sorted_by_price])

# OOP based train system ----------------------------------------------------------------------------------

# class Train :
#     def __init__(self,train_number,name,source,destination,total_seats):
#         self.train_number=train_number
#         self.name=name
#         self.source=source
#         self.destination=destination
#         self.total_seats=total_seats
#         self.available_seats =total_seats

#     def display_info(self):
#         print(f"{self.train_number} - {self.name}")
#         print(f"Route :{self.source} to {self.destination}")
#         print(f"Available seats :{self.available_seats}/{self.total_seats}")

#     def book_seats (self):
#         if self.available_seats > 0:
#             self.available_seats -=1
#             return True
#         return False

# train1 =Train(12301,"Deccan Express","Mumbai","Pune",500)  
# train2 =Train(12302,"Rajdhani Express","Howrah","New Delhi",400)   

# print("== TRAIN INFORMATION ==")

# train1.display_info()
# print()
# train2.display_info()

# print("\n === BOOKING TICKETS ===")

# if train1.book_seats():
#     print("Seat Booked Sucessfully in deccan Express !!")
#     train1.display_info()
# print ("__________________________________________________________________")
# class Train :
#     def __init__(self,train_number,name,source,destination):
#         self.train_number=train_number
#         self.name=name
#         self.source=source
#         self.destination=destination

#     def get_info(self):
#         return f"{self.train_number} - {self.name}"


# class ExpressTrain(Train):
#     def __init__(self, train_number, name, source, destination,max_speed):
#         super().__init__(train_number, name, source, destination)
#         self.max_speed =max_speed

#     def get_info(self):
#         base_info = super().get_info()
#         return f"{base_info} (Max Speed : {self.max_speed} km/h)"       

# class PassengerTrain(Train):
#     def __init__(self, train_number, name, source, destination,stops):
#         super().__init__(train_number, name, source, destination)
#         self.stops = stops

#     def get_info(self):
#         base_info = super().get_info()
#         return f"{base_info} (Stops : {len(self.stops)})"  

# express = ExpressTrain(12301,"Deccan Express ","Mumnai","Pune",130)
# passenger =PassengerTrain(11001,"Intercity Express ","Mumbai","pune",["lonavala","khandala"])

# print("== Train Types ==")
# print(f"Express Train :{express.get_info()}")
# print(f"Passenger train{passenger.get_info()}")

# Encapsulation ------------------------------------------------------------------------------------

# class BankAccount:

#     def __init__(self,account_number,initial_balance =0):
#         self._account_number =account_number  # protected attribute we use  "_"
#         self.__balance= initial_balance      # private attribute we use "__"  

#     @property
#     def balance(self):
#         return self.__balance

#     @property
#     def account_number(self):
#         return self._account_number

#     def deposit(self,amount):
#         if amount > 0 :
#             self.__balance += amount
#             print(f"Deposited Amount: ₹{amount}. New Balance :₹{self.__balance}")
#         else:
#             print("Invalid Amount !!")

#     def withdraw(self,amount):
#         if 0 < amount <= self.__balance :
#             self.__balance -= amount
#             print(f"Witthdrawn Amount :₹{amount}. New Balance :₹{self.__balance}")
#         else:
#             print("Invalid Witthdrawl or insufficient Funds  !!")


# class Ticket :
#     def __init__(self,pasenger_name,train_number,seat_number):
#         self.__passenger_name = pasenger_name
#         self.__train_number = train_number
#         self.__seat_number= seat_number
#         self.__is_confirmed = False

#     def confirm_ticket(self):
#         self.__is_confirmed = True

#     def Details(self):
#         status ="Confirmed " if self.__is_confirmed else "Pending"
#         return{
#             "Passenger :":self.__passenger_name,
#             "Train :":self.__train_number,
#             "Seat Number :":self.__seat_number,
#             "Status :":status
#         }

# print("===== BANK ACCOUNT =====")
# account = BankAccount("IR123456789")
# account.deposit(1000)
# account.withdraw(500)
# print("Current balance :₹",account.balance)

# print("\n==Ticket==")

# ticket = Ticket("Tejas palve",12301,"A5")
# print("Before Confiramation :",ticket.Details())
# ticket.confirm_ticket()
# print("After Confirmation :",ticket.Details())

# Polymorphism -----------------------------------------------------------------------------------

# class PaymentMethod :
#     def process_payment(self,amount):
#         raise NotImplementedError("Subclass must implemented anstract method")

# class creditCard(PaymentMethod):
#     def process_payment(self, amount):
#         return f"Processing {amount} via Credit card ."

# class DebitCard(PaymentMethod):
#     def process_payment(self, amount):
#         return f"Processing {amount} via Debit card ."

# class Upi(PaymentMethod):
#     def process_payment(self, amount):
#         return f"Processing {amount} via Upi ."

# class NetBanking(PaymentMethod):
#     def process_payment(self, amount):
#         return f"Processing {amount} via Net Banking ."
    

# def make_payment(payment_method,amount):
#     return payment_method.process_payment(amount)

# print("=== Payment method ===")

# payments =[
#     creditCard(),
#     DebitCard(),
#     Upi(),
#     NetBanking()
# ]

# for payments in payments:
#     print(make_payment(payments,1500))

# Magic Methods For Customized Behaviours -------------------------------------------------------

# class Ticket :
#     def __init__(self,pnr,passenger_name):
#         self.pnr =pnr
#         self.passenger_name = passenger_name

#     def __str__(self):
#         return  f"Ticket(PNR :{self.pnr}, passenger :{self.passenger_name})"

#     def  __repr__(self):
#         return f"Ticket(pnr ='{self.pnr}',passenger_name='{self.passenger_name}')"

#     def __eq__(self,other):
#         if isinstance(other,Ticket):
#             return self.pnr == other.pnr
#         return False

# print("== Ticket magic Methods ==")
# ticket1 = Ticket("1234567890","Rahul kumar")
# ticket2 = Ticket("1234567890","Rahul kumar")
# ticket3 = Ticket("9034567890","Priya Singh")

# print(f"User - Friendly :{ticket1}")
# print(f"Developer - friendly : {repr(ticket2)}")
# print(f"Ticket1 == Ticket2 :{ticket1 == ticket2}")
# print(f"Ticket1 == Ticket3 :{ticket1 == ticket3}")

# Train Shedule Management ---------------------------------------------------------------------

train_schedule =[]

train_schedule.append({
    "number":1234,
    "name":"Rajdhani Express",
    "departure":"14:00",
    "arrival":"10:30",
    "duration":"20h 30m"
})

train_schedule.append({
    "number":1233,
    "name":"Deccan Express",
    "departure":"16:00",
    "arrival":"9:30",
    "duration":"4h 30m"
})

# List Operation 

print("Train Schedules")
print(f"Total trains :{len(train_schedule)}")

first_train = train_schedule[0]
print(f"First Train :{first_train}")

Morning_train = train_schedule[:1]
print(f"Morning Train  :{[t['name'] for t in Morning_train]}")

print(Morning_train)


