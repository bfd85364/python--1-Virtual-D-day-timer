#D-day �ð�#
#���� �ð��� ��Ÿ���ٱ⺸�ٴ� ���� ��¥�� ����, �ð��� �帧�� �ʴ����� ������ �ſ� ������ ���α׷�"
#D-day�� �Է��ϸ� �� �������� �ð��� �����ش�.
#D-day�� �Ǹ� ���α׷��� ����ȴ�.
#time.sleep()�Լ��� ����Ͽ� �����̳� ��������� �ð��� �帧�� �����Ҽ� �ִ�.->FPS(�ʴ� �����ӿ�ũ)�� ������ ��� tick() ���
#time.sleep()�Լ��� �ʸ� �Է¹޴´�.
import time
print("===========================================================\n")
print("=-------------------Project Moon({i)----------------------=\n")
print("===========================================================\n")
print("This program will help you to calculate the number of days\n")
print("to your D-day\n")

#D-day �Է�ĭ
s= input("Enter the number of your D-days:")
D=int(s)

#Ÿ�̸�(��)
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
