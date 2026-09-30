#hour = int(input())
#minute = int(input())
#time = hour * 60 + minute + 15
#hour = time // 60
#minute = time % 60
#if hour > 23:
#    hour = hour - 24
#print(f"{hour}:{minute:02d}")

#Cinema Tickets
dey_of_week = input()
if dey_of_week == "Monday" or dey_of_week == "Tuesday" or dey_of_week == "Friday":
    print("12")
elif dey_of_week == "Wednesday" or dey_of_week == "Thursday":
    print("14")
else:
    print("16")
    
