from math import *

GSPEED = 9.81

def maxHeight(theta, zeroVelo):
    return (zeroVelo**2 * sin(theta)**2) / (2 * GSPEED)

def range(theta, zeroVelo):
    return (zeroVelo**2 * sin(2 * theta)) / GSPEED

def flyingtime(theta, zeroVelo):
    return (2 * zeroVelo * sin(theta)) / GSPEED

def calculate_theta(zeroVelo, range):
    sin_2theta = (range * GSPEED) / (zeroVelo ** 2)
    if sin_2theta > 1 or sin_2theta < -1:
        return None
    theta = 0.5 * asin(sin_2theta)
    return degrees(theta)

print('=============== 진공탄도계산기 ===============')
while True:
    print('무엇을 계산?')
    n = int(input('1 : 포각으로 계산\n2 : 포각을 계산\n'))
    if n == -1:
        break
    elif n == 1:
        theta = float(input('포각 : '))
        zeroVelo = float(input('포구초속 : '))
        theta = radians(theta)
        a = int(input('무엇을 계산?\n1 : 최대고도\n2 : 체공시간\n3 : 탄착거리\n'))
        if a == 1:
            print("최대고도 : 약", round(maxHeight(theta, zeroVelo), 2), "m\n\n")
        elif a == 2:
            print("체공시간 : 약", round(flyingtime(theta, zeroVelo), 1), "초\n\n")
        elif a == 3:
            print("탄착거리 : 약", round(range(theta, zeroVelo), 2), "m앞에 떨어짐\n\n")
        else:
            print("입력이 잘못됨")
            continue

    elif n == 2:
         range = float(input('거리 : '))
         zeroVelo = float(input('포구초속 : '))
         canonLen = float(input('포신 길이 : '))
         print("거리와 포구초속에 따라 포각은 약", round((calculate_theta(zeroVelo, range)), 2), "도 입니다\n\n")
         #포신의 길이가 0일때로 한정

    else:
        print('잘못 입력')
        continue

























