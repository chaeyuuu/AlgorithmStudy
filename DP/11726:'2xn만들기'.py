# 문제
# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# 아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

box=[]
n = int(input())
box = [0] * max(4,n+1)
box[1]=1
box[2]=2

for i in range(3,n+1):
    box[i] = box[i-2] + box[i-1]

print(box[n]%10007)