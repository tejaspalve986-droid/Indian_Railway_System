# for i in range (0,10,2):
#     print(i)

# for i in range (1,21): ---------Even Numbers ------------------
#     if i % 2 == 0:
#         print(i)

# for i in range (1,21): ---------Odd Numbers ------------------
#     if i % 2 != 0:
#         print(i)

# num = 5               ---------- Tables ----------------------
# for i in range(1,11): 
#     print(num,"x",i,"=",num*i)

# total = 0   ---------- Total of Numbers ----------------------
# for i in range (1,11): 
#     total = total + i
# print("Total :",total)

# num= 5       --------------- Factorail ----------------------
# fact =1
# for i in range (1,num + 1):
#     fact = fact * i
# print ("Factorial:",fact)

# ------------------------------------------------------------------

# chars = "python"
# for char in chars:
#     print(char)

# names =["Aarti","Suraj","Tejas","Om","Yash","Yash"]
# for name in names:
#     print(name)

# num = [10,20,30,50,40,60,200,500]
# largest = num[0]
# for i in num:
#     if i > largest:
#         largest = i
# print("Largest Number :",largest)

# text ="python programming"
# count = 0
# for char in text:
#     if char in "aeiou":
#         count +=1
# print("Nummber of Vowels :",count)

# WHILE LOOP _____________________________________________________________

# i =1
# while i<=10:
#     print(i)
#     i+=1
# print(i)

# i = 1
# total = 0 
# while i <=10 :
#     total  += i
#     i += 1
# print("Total :",total)

# num = 12345  ----------------------REVERSE OF NUMBERS --------------------
# reverse = 0
# while num > 0:
#     digit =num % 10
#     reverse =reverse * 10 + digit 
#     num //= 10

# print("Reverse Number :",reverse)

# num = 123456  ----------------------COUNT OF NUMBERS --------------------
# count = 0
# while num > 0 :
#     num  //= 10
#     count +=1
# print("The Number Of Digit : ",count)

# correct_numbers = 4   ----------------------Guessing a correct  NUMBERS --------------------
# guess = int(input("Enter a number :"))
# while guess != correct_numbers:
#     print("Wrong Numbers !!")

#     guess=int(input("Enter a Number :"))

# print ("correct guess !!")

# LOOP CONTROL STATEMENTS ______________________________________________________________________________

# for i in range (20):
#     if i == 12:
#         break
#     print(i)


# for i in range (20):
#     if i == 12:
#         continue
#     print(i)


train_name = "Deccan Express"
train_number = 12301
ticket_price =2450.50
is_ac_available = True
seat_number = [1,2,3,4,5]

# print("Train Name :",type(train_name))
# print("Train Number :",type(train_number))
# print("Ticket Price :",type(ticket_price))
# print("AC Availability :",type(is_ac_available))
# print("Seat Number :",type(seat_number))


# print(f"Train name :{train_name}")
# print(f"Train number :{train_number}")
# print(f"Ticket Price : {ticket_price}")
# print(f"Ac availability : {is_ac_available}")
# print(f"Seat numbers : {seat_number}")

print("===========INDIAN RAILWAY BOOKING SYSTEM ===========")

passenger_name =input("Enter Passenger Name :")
age = int(input("Enter Age :"))
destination = input("Enter Destination :")

print("\n----------DISPLAY BOOKING DETAILS------------")
print(f"Passenger :{passenger_name}")
print(f"Age :{age}")
print(f"Destination :{destination}")
print("\n BOOKING CONFIRMED !!!!!!!")


print("=======================================")
base_price =1500
service_charge =100
total_price = base_price + service_charge

print(f"Base price :₹{base_price}")
print(f"Service charge :₹{service_charge}")
print(f"Total price :{total_price}")

print("=======================================")

if age < 5 :
    total_price = 0
    category = " Infant (Free )"
elif age < 12 :
    total_price =750 + 100
    category = "Child (50% Discount)"
elif age >= 60 :
    total_price = 1200 + 100
    category ="Senior Citizens (20% Discount)"
else  :
    price =1500
    category = "Adult"

print(f"category : {category}")
print(f"Ticket Price : ₹{total_price}")

print("=======================================")

has_ticket = True
has_id_proof = True
can_board = has_ticket and has_id_proof

print(f"Can Board Train ? {can_board}")

print("============================================")
trains =[
    {"name":"Deccan Express",
    "number":12301,
    "destination":"Pune"},
     {"name":"Rajdhani Express",
    "number":12301,
    "destination":"New Delhi"},
    {"name":"Shatapdi Express",
    "number":12001,
    "destination":"Chennai"} ,
    {"name":"Duronto Express",
    "number":12291,
    "destination":"Mumbai"} 
]
print("============================================")
print("Available Trains")
for trains in trains :
    print(f"{trains["number"]}-{trains["name"]}-{trains["destination"]}")