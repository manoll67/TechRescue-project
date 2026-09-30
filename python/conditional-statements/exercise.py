#time_first_second = int(input())
#time_second_second = int(input())
#time_third_second = int(input())
#total_time = time_first_second + time_second_second + time_third_second
#minutes = total_time // 60
#seconds = total_time % 60
#print(f"{minutes}:{seconds:02d}")

number = int(input())
bonus = 0
if number <= 100:
    bonus = 5
elif number <= 1000:
    bonus = number * 0.20
elif number > 1000:
    bonus = number * 0.10

if number % 2 == 0:
       bonus += 1
elif number % 10 == 5:
         bonus += 2

print(bonus)
print(number + bonus)   


