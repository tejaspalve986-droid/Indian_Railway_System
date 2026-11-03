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

trains = [
    {"name":"Rajdhani Express",
     "number":12301,
    "destination":"New Delhi"},
    {"name":"Shatapdi Express",
     "number":12001,
    "destination":"Chennai"} ,
    {"name":"Duronto Express",
     "number":12291,
    "destination":"Mumbai"} ,
    {"name":"Deccan Express",
     "number":12221,
    "destination":"Pune"} 
]

print("AVAILABLE TRAINS : ")
for trains in trains :
    print(f"{trains["number"]}-{trains["name"]}-{trains["destination"]}")

# While Loop - Booking System Menu

print("\n=== BOOKING MENU ===")
choice = 0

while choice != 3:
    print("1 . Book Ticket")
    print("2. Check Status")
    print("3. Exit")
    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        print("Booking Ticket .................")
    elif choice == 2:
        print("Checking Status ................" )
    elif choice == 3:
        print("Thank You For Using Indian Railways !")
    else:
        print("Invalid Choice ! ----------------")
