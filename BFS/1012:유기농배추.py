# 입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를
# 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 
# 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.

# 출력
# 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = [(x,y)]
    matrix[x][y] = 0 # 방문한 곳 = 0
    
    while queue:
        x,y=queue.pop(0)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
        # 범위 확인
            if nx<0 or nx>=M or ny<0 or ny>=N:
                continue
        
            if matrix[nx][ny] == 1:
                queue.append((nx,ny))
                matrix[nx][ny] = 0 


T = int(sys.stdin.readline()) # 테스트 케이스 개수
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    matrix = [[0]*(N) for _ in range(M)] # 배추밭 크기만큼 이차원 배열 생성
    for _ in range(K):
        X, Y = map(int, input().split())
        matrix[X][Y] = 1 # 배추 위치 = 1 
        
    cnt = 0
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 1:
                bfs(i,j) # 배추위치가 1인 곳이 있으면 bfs 수행
                cnt +=1  # 카운트 값 증가
                
    print(cnt)
                
        