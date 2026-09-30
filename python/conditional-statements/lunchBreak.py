import math

name_of_film = input()
length_of_film = int(input())
length_of_break = int(input())

lunch_time = length_of_break / 8
relax_time = length_of_break / 4

off_time = length_of_break - lunch_time - relax_time
if off_time >= length_of_film:
    print(f"You have enough time to watch {name_of_film} and left with {math.ceil(off_time - length_of_film)} minutes free time.")
else:    
    print(f"You don't have enough time to watch {name_of_film}, you need {math.ceil(length_of_film - off_time)} more minutes.")  
