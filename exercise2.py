import time

name=input("Enter your name: ").title()
current_time= time.strftime("%H:%M:%S")
print(current_time)

hour = int((time.strftime('%H')))

if hour <= 4 and hour < 12:
    print("Good Morning",name)

elif hour >= 12 and hour < 15:
        print("Good Afternoon",name)
elif hour >= 15 and hour < 19:
          print("Good Evening",name)
else:
           print("Good Night",name)