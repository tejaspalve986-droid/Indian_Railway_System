# List ------------------------------------------------------------------------------------

# states =["maharashtra","kerala","punjab","tamil nadu","gujrat"]

# print("Original List :",states)

# #Add elements

# states.append("karnataka")
# states.insert(2,"rajasthan") # insert an index
# print("After adding append and insert :",states)

# # Extended with another list
# states.extend(["goa","bihar"])
# print("After Extended :",states) 

# # Remoove elements 

# states.remove("bihar") # removing specific elements
# popped = states.pop() # remove and store last elements 
# print("Removed Elements :",popped)
# print("after remove & pop :",states)

# # Sorting & Reversing

# states.sort()
# print("sorted list :",states)
# states.reverse()
# print("Reversed list :",states)

# # index and count

# print("Index of kerala :",states.index("kerala"))
# print("Count of kerala :",states.count("kerala"))

# # copy & clear 

# copy_states =states.copy()
# print("copied list :",copy_states)
# states.clear()
# print("Cleared list :",states)

# Tuple ------------------------------------------------------------------------------------

# cities =("mumbai","kalyan","delhi","chennai","kolkata","mumbai")

# # count
# print("Count of mumbai :",cities.count("mumbai"))

# #index
# print("index of kolkata :",cities.index("kolkata"))

# # length
# print("length of cities :",len(cities))

# # membership
# print("delhi in tuple ?","delhi" in cities)

# # min and max (alphabetical)
# print("min",min(cities))
# print("max",max(cities))

# Dictionary ------------------------------------------------------------------------------------
#  functions get() ,keys() ,values (),items (),update (),pop (),copy(), clear () ----------------

# capitals = {
#     "maharashtra":"mumbai",
#     "tamil nadu":"chennai",
#     "gujrat":"gandhinagar", 
#     "goa":"panji"
# }

# print("Dictionary :",capitals)

# # Get Access
# print("Capital of goa :",capitals.get("goa"))

# # Key , Values and Items

# print("states :",capitals.keys())
# print("capitals :",capitals.values())
# print("pairs :",capitals.items())

# # Update and Add 

# capitals.update({"karnataka":"bengaluru"})
# capitals["punjab"] ="chandigarh"
# print("after update :",capitals)

# # Remove  

# capitals.pop("gujrat") # remove by key 
# capitals.popitem() # remove last inserted 
# print("after pop & pop items :",capitals)

# # Copy & Clear

# copy_caps =capitals.copy()
# capitals.clear()
# print("copied:",copy_caps)
# print("cleared:",capitals)

# Set ------------------------------------------------------------------------------------

# languages = {"hindi","english","marathi","tamil","telugu"}

# print("Original set :",languages)

# # Add & Remove 
# languages.add("gujarati")
# languages.discard("english")
# print ("Print add and discard language :",languages)

# # remove (error if not present )

# languages.remove("hindi")
# print("remove :",languages)

# # set operation

# south={"tamil","telugu","kannada"}
# print("union ;",languages.union(south))
# print("intersection;",languages.intersection(south))
# print("diffrence ;",languages.difference(south))
# print("symmetric diffrence ;",languages.symmetric_difference(south))

# # copy clear 
# copy_lang =languages.copy()
# languages.clear()
# print("copied :",copy_lang)
# print("clear :",languages)

# String ------------------------------------------------------------------------------------

# movie = "sholay is a classic bollywood movie 1"

# print("original :",movie)

# # case
# print(movie.upper())
# print(movie.lower())
# print(movie.title())
# print(movie.capitalize())
# print(movie.swapcase())

# # check 
# print(movie.startswith("sholay"))
# print(movie.endswith("movie"))
# print("is alpha :",movie.isalpha())
# print("is digit :",movie.isdigit())

# # find & replace 
# print("find 'Classic' :",movie.find("classic"))
# print(movie.replace("classic","legendary"))

# #Split & join
# words = movie.split()
# print("split:",words)
# joined ="-".join(words)
# print("joined :",joined)

# # Strip
# line = "    JAY HIND    "
# print("Stripped :",line.strip())
# print("left Strip :",line.lstrip())
# print("Right Strip :",line.rstrip())

# # Count & index 
# print("count of 'o ':",movie.count("o"))
# print("Index of bollywood :",movie.index("bollywood"))

# # Length
# print("Length :",len(movie))

# Date and Time ------------------------------------------------------------------------------------
# import datetime

# # Current date & time 
# now = datetime.datetime.now()
# print("Now:",now)

# # Today
# today=datetime.date.today()
# print("today:",today)

# # Specific date (Republic day)
# republic_day = datetime.date(1950,1,26)
# print("Republic day :",republic_day.strftime("%d-%b-%y"))

# # Time diffrence
# diff =today - republic_day
# print("Days since republic day :",diff.days)

# # Current Components

# print("year :",now.year)
# print("month:",now.month)
# print("day :",now.day)
# print("hour :",now.hour)
# print("minute :",now.minute)
# print("seconds :",now.second)

# # crreate a time object 
# t = datetime.time(10,30,15)
# print("Custome Time:",t)

# #Combine date & time 

# dt = datetime.datetime.combine(today,t)
# print("Combined datetime :",dt)

# # Formatting 
# print("formatted :",now.strftime("%A ,%d  %b  %y, %I:%M %p"))