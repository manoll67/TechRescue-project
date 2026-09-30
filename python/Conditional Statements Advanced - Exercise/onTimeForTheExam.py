exam_hure = int(input())
exam_minute = int(input())
arrival_hure = int(input())
arrival_minute = int(input())

exam_time = exam_hure * 60 + exam_minute
arrival_time = arrival_hure * 60 + arrival_minute
time_diff = arrival_time -exam_time 

if  time_diff < 0 and abs(time_diff) <= 30:
        print("On time")
        print(f"({abs(time_diff)} minutes before the start)")

elif time_diff < 0:
      print("Early")
      diff = abs(time_diff)
      if diff < 60:
            print(f"{diff} minutes before the start")
      else:
            print(f"{diff // 60}:{diff % 60:02d} hours before the start")  
         
else:
      print("Late")
      if time_diff < 60:
            print(f"{time_diff} minutes after the start")
      else:
            print(f"{time_diff // 60}:{time_diff % 60:02d} hours affter the start")





     






