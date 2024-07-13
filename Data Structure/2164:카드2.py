# 문제
# N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
# 이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# 예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 
# 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.

# N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

# 1. 주어지는 카드의 개수 n개 입력
# 2. 제일 위에 있는 카드 바닥에 버림
# 3. 그 다음 제일 위에 있는 카드 아래에 있는 카드 밑으로 옮김
# 4. 예를 들어 n=4 -> 위에서부터 1234 -> 1버림 -> 234 -> 그다음 위에 있는 애가 2니까 342 -> 그다음에 버림 -> 42 -> 그다음 4를 밑으로 보내면 24 -> 2버림 -> 한장 남은거 출력

# --- 시간 초과--- 
# import time

# numList=[]

# N=int(input())
# sstart = time.time()
# for i in range(N,0,-1):
#     numList.append(i)
  

# while len(numList) != 1:  
#     numList.pop()
#     next=numList.pop()
#     numList.insert(0,next)

# print(f'{numList}, 삽입 수행 시간, {time.time() - sstart} 초')
# print(numList)

# --- deque 사용 ----
from collections import deque

N=int(input())
myqueue = deque()

for i in range(N,0,-1):
    myqueue.append(i)
    
while len(myqueue) != 1:
    myqueue.pop()
    next = myqueue.pop()
    myqueue.appendleft(next)

print(myqueue[0])



    
    

