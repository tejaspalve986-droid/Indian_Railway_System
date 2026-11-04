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