# Defining Variables for Indain Railway System

train_name ="Rajdhani Express"
train_number = 12031
ticket_price = 2450.50
is_ac_available = True 
seat_number = [1,2,3,4,5]

# Showing the Deatails using print Functions

# print("Train Name : ",train_name)
# print("Train Number : ",train_number)
# print("Ticket Price : ",ticket_price)
# print("AC Availability : ",is_ac_available)
# print("Seat Numbers : ",seat_number)

# Show the data types for the Varaibles using the Type Functions

# print("The data type of Train Name :",type(train_name))
# print("The data type of Train Number :",type(train_number))
# print("The data type of Ticket Price :",type(ticket_price))
# print("The data type of Is_ac_ Available :",type(is_ac_available))
# print("The data type of Seat Numbers :",type(seat_number))

# Getting passenger Information #

print("===  INDIAN RAILWAY BOOKING SYSTEM  ===")
passenger_name =input("ENTER PASSENGER NAME :")
age = int(input("ENTER AGE :"))
destination = input("ENTER DESTINATION :")

# display boooking confirmation 

print("\n=== BOOKING DETAILS ===")
print(f"Passenger :{passenger_name}")
print(f"Age :{age}")
print(f"Destination :{destination}")
print("Booking confirmed !")

