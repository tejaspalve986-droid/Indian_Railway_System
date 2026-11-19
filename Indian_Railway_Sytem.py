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

train = [
    {"name":"rajdhani","price":2500,"duration":16},
    {"name":"shatabdi","price":1800,"duration":8},
    {"name":"Duronto","price":2000,"duration":12},
]

# map------------------------------------------------------------------------------------------------

train_name = list(map(lambda x : x['name'],train))
print(f"\n Train Names :{train_name}")

# Filter------------------------------------------------------------------------------------------------

affordale_trains = list(filter(lambda x: x['price']<2200,train))

print("Affordable Trains :",[t["name"] for t in affordale_trains])

# Sorted ------------------------------------------------------------------------------------------------

sorted_by_price = sorted(train,key=lambda x:x["price"])
print("Sorted By price : ",[t["name"]for t in sorted_by_price])


