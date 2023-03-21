# No.2 회문(Palindrome)

# 내부확인 함수
def inner(str, left, right):
    while left < right: # 커서가 같거나(길이:홀수) 반전되는(길이:짝수) 순간 종료
        if str[left] != str[right]: # 내부의 양옆도 다르면 => 전체는 : 문자열
            return "문자열"
        left += 1
        right -= 1
    return "유사회문"    # 내부의 양옆은 모두 같았으면 => 전체는 : 유사회문
        


N = int(input())    # 문자열의 개수

for _ in range(N):
    str = input()   # 문자열 1개 입력받기

    left = 0
    right = len(str) - 1
    result = "회문"

    while left < right: # 커서가 같거나(길이:홀수) 반전되는(길이:짝수) 순간 종료
        if str[left] != str[right]: # 양옆이 다르면 유사회문or문자열
            result = "유사회문"

            inner_result1 = inner(str, left + 1, right)    #  왼쪽커서 바꿔서 내부확인
            inner_result2 = inner(str, left, right - 1)    #  오른쪽커서 바꿔서 내부확인

            if (inner_result1 == "문자열") and (inner_result2 == "문자열"):  # 둘 중 하나라도 내부가 유사회문이라면 result는 유사회문 ==> 둘 다 문자열이라면 result는 문자열
                result = "문자열" # result = 3

            break   # 내부를 이미 유사회문 or 문자열 로 판별하였으므로 바로 종료
        left += 1
        right -= 1

    if result == "회문":
        print(1)
    elif result == "유사회문":
        print(2)
    elif result == "문자열":
        print(3)



# 반례찾기 : a b b a b
# a와 b를 비교 시
# 1) left+1 : b와 b 동일해서 유사회문~~~> 내부는 b a라 문자열
# 2) right-1 : a와 a 동일해서 유사회문 ~~~> 내부는 b b => 유사회문
# 어떤 것을 먼저 계산하느냐에 따라 결과가 달라짐
# 따라서, 둘 중 하나라도 유사회문이라면 유사회문로 판별할 것