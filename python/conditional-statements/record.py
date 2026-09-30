#record = float(input())
#distance = float(input())
#time_per_meter = float(input())
#delay = (distance // 15) * 12.5
#total_time = distance * time_per_meter + delay
#if total_time < record:
#    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
#else:
#    print(f'No, he failed! He was {total_time - record:.2f} seconds slower.')   
    
#Fruit or Vegetable
product = input()
vegetables = ["tomato", "cucumber", "pepper", "carrot"]
fruits = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
if product in vegetables:
    print("vegetable")
elif product in fruits:
    print("fruit")
else:
    print("unknown")