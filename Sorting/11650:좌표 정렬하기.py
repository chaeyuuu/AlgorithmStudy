# 문제
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
# 출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

# 1. 정렬할 좌표 개수 받기 N
# 2. for 문으로 map이랑 list 이용해서 받기
# 3. x좌표끼리 비교해서 정렬 
# 4. x 좌표 같으면 y 좌표 증가 순서대로 정렬

# --- 시간 초과 ---

# import sys

# N = int(input())
# const = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# for i in range(N):
#     for j in range(N-i-1):
#         if const[j][0] > const[j+1][0] or (const[j][0]==const[j+1][0] and const[j][1]>const[j+1][1]):
#             const[j], const[j+1] = const [j+1], const [j]

# for point in const:
#     print(point[0], point[1])

# --- sorted 이용 ---

import sys
N = int(input())
const = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
const_s = sorted(const)

for point in const_s:
    print(point[0], point[1])
    


    