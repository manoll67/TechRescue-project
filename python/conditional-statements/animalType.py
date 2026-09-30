#animal = input()
#if animal == "dog":
 #   print("mammal")
#elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
 #   print("reptile")
#else:    print("unknown")

#Number in Range 
#number = int(input())
#if -100 <= number <= 100 and number != 0:
#    print("Yes")    
#else:    
#    print("No")

# Working Hours 
#time = int(input())
#day = input()
#if 10 <= time <= 18 and (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday"):
#    print("open")
#else:    print("closed")

# Working Hours -- with list

time = int(input())
day = input()

work_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday" ]
change_day = "Sunday"
if 10 <= time <= 18 and day in work_days:
    print("open")
elif day == change_day and time >= 10 and time <= 18:
    print("closed")
else:    print("closed")

# Working Hours -- with list -- simplified  
time = int(input())
day = input()
work_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if day == "Sunday":
    print("closed")
elif 10 <= time <= 18 and day in work_days:
    print("open")
else:
    print("closed")