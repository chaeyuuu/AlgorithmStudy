# N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

T= int(input())
for _ in range(T):
    N = int(input())
    fb = [0] * max(3,N+1)
    fb[0] = [1, 0]
    fb[1] = [0, 1]


    for i in range(2, N+1):
        a = ((fb[i-1][0]+fb[i-2][0]))
        b = (fb[i-1][1]+fb[i-2][1])
        fb[i] = (list((a,b)))
    
    print(fb[N][0], fb[N][1])
