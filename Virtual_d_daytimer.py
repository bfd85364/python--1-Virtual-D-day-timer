#D-day 시계#
#실제 시간을 나타낸다기보다는 그저 날짜를 세고, 시간의 흐름을 초단위로 구현한 매우 간단한 프로그램"
#D-day를 입력하면 그 날까지의 시간을 세어준다.
#D-day가 되면 프로그램이 종료된다.
#time.sleep()함수를 사용하여 게임이나 가상공간의 시간의 흐름을 구현할수 있다.->FPS(초당 프레임워크)를 조절할 경우 tick() 사용
#time.sleep()함수는 초를 입력받는다.
import time
print("===========================================================\n")
print("=-------------------Project Moon({i)----------------------=\n")
print("===========================================================\n")
print("This program will help you to calculate the number of days\n")
print("to your D-day\n")

#D-day 입력칸
s= input("Enter the number of your D-days:")
D=int(s)

#타이머(초)
V= input("Enter your virtual time:(please, enter by 'seconds': ")
T=int(V)

def D_day(n):
    date = 0
    hour = 1
    while date <= n:
        while hour < 24:
            time.sleep(T)
            print("Hour", hour,"\n")
            hour += 1
        date += 1
        hour = 1
        if (date <n):
            time.sleep(T)
            print(date, "Days\n")
        elif(date == n):
            time.sleep(T)
            print("today is D-day", date, "day")
            break
D_day(D)
