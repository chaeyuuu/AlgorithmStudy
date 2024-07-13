# 문제
# 1부터 연속적으로 번호가 붙어있는 스위치들이 있다. 스위치는 켜져 있거나 꺼져있는 상태이다. 
# <그림 1>에 스위치 8개의 상태가 표시되어 있다. ‘1’은 스위치가 켜져 있음을, ‘0’은 꺼져 있음을 나타낸다. 
# 그리고 학생 몇 명을 뽑아서, 학생들에게 1 이상이고 스위치 개수 이하인 자연수를 하나씩 나누어주었다. 
# 학생들은 자신의 성별과 받은 수에 따라 아래와 같은 방식으로 스위치를 조작하게 된다.

# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다. 
# 즉, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다. <그림 1>과 같은 상태에서 남학생이 3을 받았다면, 이 학생은 <그림 2>와 같이 3번, 6번 스위치의 상태를 바꾼다.

# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다. 
# 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.

# 1. 첫째줄에는 스위치의 개수 / 둘째 줄에는 각 스위치의 상태가 주어진다. 켜져 있으면 1, 꺼져있으면 0이라고 표시하고 사이에 빈칸이 하나씩 
# / 셋째줄 학생수 /  넷째 줄부터 마지막 줄까지 한 줄에 한 학생의 성별, 학생이 받은 수 ->  남학생: 1 여학생: 2,학생의 성별과 받은 수 사이에 빈칸이 하나씩 있다.

# <남자:1>
# 학생 성별이 1이면 남자 -> 받은 스위치 번호랑 스위치 리스트에 있는거 비교 -> 스위치 리스트 내에서 스위치번호의 배수(자기자신포함)인 애들 찾아서 상태 바꾸기
# 스위치 번호는 1부터임 

# <여자:2>
# 자신이 받은 스위치 기준 양 옆으로 대칭 확인 -> 대칭이면 대칭 아닐 때까지 계속 쭉 -> 대칭 아닌 순간 발견하면 그 안에 있는거 싹 스위치 상태 바꾸기
# left,right가 범위 벗어나거나 좌우로 대칭이면 stop
    

import sys

n = int(input()) # number of switches
switch = list(map(int, sys.stdin.readline().split())) # state of switch -> on:1 / off:0
std = int(input()) # number of student
for _ in range(std):
    sex, number = map(int,sys.stdin.readline().split())

    if sex == 1: # man
        for i in range(1,n+1):
            if i % number == 0:
                if switch[i-1] == 1:
                    switch[i-1] = 0
                else:
                    switch[i-1] = 1

    else: #female
        number -=1
        left, right = number, number
        
        while (left >= 0 and right < n and switch[left]==switch[right]):
            left-=1
            right+=1
        
        left+=1
        right-=1
            
        for i in range(left,right+1):
            if switch[i] == 1:
                switch[i] = 0
            else:
                switch[i] = 1
        
for i in range(n):
    print(switch[i],end=' ')
    if((i+1)%20==0):
        print()
        
