# 문제
# 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 
# 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 
# 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다.
# 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 
# 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 
# 여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.

# 테스트 케이스 개수 입력 받기 
# 엔터 치기 전까지 입력된 () 얘네 스택에 저장
# 하나씩 팝 하면서 짝 있는지 확인하고 없으면 yes, 있으면 no


stack=[]
t = int(input())
for _ in range (t):
    data = input()
    isVPS=True
    for char in data:
        if char=='(':
            stack.append(char)
        elif char==')':
            if stack:
                stack.pop()
            else:
                isVPS=False
                break
            
    # 다 처리한 후에 스택에 남아있는게 있으면 vps가 아님
    if stack:
        isVPS=False

    
    if isVPS:
        print("YES")
    else:
        print('NO')
    
    stack.clear()


 