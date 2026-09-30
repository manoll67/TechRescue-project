#time_first = int(input())
#time_second = int(input())
#time_third = int(input())
#total_time = time_first + time_second + time_third
#minutes = total_time // 60
#seconds = total_time % 60
#print(f"{minutes}:{seconds:02d}")

                       
#grade = float(input())
#if grade >= 5.50:
 #   print("Excellent!")
#password = input()
#if password == "s3cr3t!P@ssw0rd":
  #  print("Welcome")
#else:
   # print("Wrong password!")
# coment

#number = int(input())
#if number < 100:
#    print("Less than 100")
#elif 100 <= number <= 200:
#    print("Between 100 and 200")
#else:
#    print("Greater than 200")

#speed
#speed = float(input())
#if speed <= 10:
#    print("slow")
#elif 10 < speed <= 50:
#    print("average")
#elif 50 < speed <= 150:
#    print("fast")
#elif 150 < speed <= 1000:
#    print("ultra fast")
#else:
#    print("extremely fast")

figure = input()
if figure == "square":
    side = float(input())
    area = side * side
    print(f"{area:.3f}")
elif figure == "rectangle":
    width = float(input())
    height = float(input())
    area = width * height
    print(f"{area:.3f}")
elif figure == "circle":
    radius = float(input())
    area = 3.14159 * radius * radius
    print(f"{area:.3f}")
elif figure == "triangle":
    side_a = float(input())  # Дължина на страната
    height = float(input())  # Височина
    area = (side_a * height) / 2  # Лице на триъгълника
    print(f"{area:.3f}")

