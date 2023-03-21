# No.3 붕어빵(Fish bread)

k = int(input())

for _ in range(5):
    Fish = list(map(int, input().split()))
    Fish = [0] + Fish   # 제일 앞에 0 추가하여, 인덱스1이 1번을 가르키게 하기

    cutInfo = []    # 불연속블록(= 인덱스와 번호가 같지 않은 블록) 의 정보 저장 : [[부호, 절댓값], [], ...]
    isCut = False   # 불연속블록 여부

    for i in range(1, k + 1): # 1번~k번
        # 불연속블록 진행O + [직전과 연속X or 지금이 마지막원소] => 불연속 종료
        if (isCut == True) and ((Fish[i-1] + 1 != Fish[i]) or (i == k)):
            isCut = False

        # 불연속블록 진행X + 직전과 연속 X => 불연속 시작
        if (isCut == False) and (Fish[i-1] + 1 != Fish[i]):
            if i == Fish[i]:    # 연속부분
                cutInfo.append([0] + [Fish[i]])    
            elif Fish[i] > 0:    # 양수부분
                cutInfo.append([1] + [Fish[i]])
            elif Fish[i] < 0:    # 음수부분
                cutInfo.append([-1] + [-Fish[i]])
            isCut = True

    # 제일 뒤 연속 제외
    if cutInfo[-1][0] == 0:
        cutInfo = cutInfo[:-1]

    # one)  -
    # two)  -+ +- (0은 불가) : 길이2의 곱셈은 -
    #       -- : 길이2의 앞과 뒤는 -
    #       --+ +-- (0은 불가) : 길이3의 중간은 -, 양옆곱셈은 -
    #       -0- (+는 불가) : 길이3의 중간은 0, 양옆은 -
    #       -+- 의 절댓값이 - > + > - (0은 불가) : 길이3의 중간은 +, 양옆은 -, 절댓값비교
    # over) 나머지

    if len(cutInfo) == 1 and cutInfo[0][0] < 0:
        print("one") 
    elif (len(cutInfo) == 2 and cutInfo[0][0]*cutInfo[1][0] < 0)\
        or (len(cutInfo) == 2 and cutInfo[0][0] == cutInfo[1][0] < 0)\
        or (len(cutInfo) == 3 and cutInfo[1][0] < 0 and cutInfo[0][0]*cutInfo[2][0] < 0)\
        or (len(cutInfo) == 3 and cutInfo[1][0] == 0 and cutInfo[0][0] == cutInfo[2][0] < 0)\
        or (len(cutInfo) == 3 and cutInfo[1][0] > 0 and cutInfo[0][0] == cutInfo[2][0] < 0 and (cutInfo[0][1] > cutInfo[1][1] > cutInfo[2][1])):
        print("two")
    else:
        print("over")



# 반례찾기1 :  1 6 3 4 5 -2 7
# + 연속 - => over이어야함
# 따라서, -+ +- || -+- --+ +-- => 중간에 연속 X. 붙어있어야함
# -- || -연- => 모두 가능 (중간에 연속 O)

# 반례찾기2 : 1 2 -4 -3 7 8 -6 -5 9
# - + - => over이어야함
# 1 2 3 4 5 6 7 -> 1 2 -7 -6 -5 -4 -3 -> 1 2 -7 -6 4 5 -3 처럼 크게 + 안에 작게 뒤집는 경우는 -+-
# -+- 블록이 순서대로, -첫번째절댓값 > +첫번째절댓값 > -첫번째절댓값 이어야함