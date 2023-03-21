# No.1 중복(Duplicated)

N = int(input())    # 최초의 카드 수

sum = 0 # 반례찾기2 참고
sum_s2 = 0
min_to_max = 0
min2_to_max2 = 0

# s의 범위 : 1~10000
min = 10000
max = 1

for _ in range(N+2):    # 추가된 카드2장 포함
    # 카드번호는 s로 입력받음
    s = int(input())
    
    # 모든 카드의 숫자 더하기 // 제곱해서 더하기
    sum = sum + s
    sum_s2 = sum_s2 + s**2

    # s 중에서 최소/최대 찾기
    if min > s:
        min = s
    if max < s:
        max = s

# 최소부터 최대까지 더하기 // 제곱해서 더하기
for i in range(min, max+1): # min ~ max
    min_to_max = min_to_max + i
    min2_to_max2 = min2_to_max2 + i**2

# 최소 + ... + 최대 + 중복카드1 + 중복카드2 = sum을 이용하여 중복카드1 + 중복카드2 구하기 // 제곱해서 구하기
diff = sum - min_to_max
diff2 = sum_s2 - min2_to_max2

# diff2 = x^2 + y^2를 이용하여, 나머지가 어떤 수의 제곱일 경우(=y가 정수일 경우)를 찾기 
for x in range(min, max):   # x는 카드의 최소~최대 사이에 존재함 ([min min+1 ... max-1 max] 에서 2장 => [min, min+1] 선택 ~ [max-1, max] 선택 => 첫 번째 카드는 max-1까지)
    y2 = diff2 - x**2
    y = y2**(1/2)

    # 1. y가 어떤 수의 제곱일 경우(루트값이 소수x 정수o)
    # 2. 두 번째 카드가 범위 밖으로 벗어나지 않게 하기 (반례찾기1 참고)
    # 3. diff = x + y를 이용 (반례찾기2 참고)
    if y.is_integer() and (y <= max) and (diff == x + y):
        print(x)
        print(int(y))
        break   # x가 더 작기 떄문에 출력 후 바로 종료



# 반례찾기1 : a^2 + b^2 = 1 + x^2 인 x가 존재하는가? ( 단, a > 1, a < b)
# a = 4, b = 7일 때
# 4^2 + 7^2 = 16 + 49 = 65 = 1 + 64 = 1 + 8^2
# ex. 1 2 3 4 5 6 7 / 4 7 의 카드가 있을 때 => 1 8부터 찾으면 8은 카드 범위 밖이라 오류
# 따라서, 카드 범위 밖으로 벗어나지 못하게 확인 필요

# 반례찾기2 : a^2 + b^2 = c^2 + x^2의 x의 경우의 수는? (단, a >= 1, a < c < b)
# a = 2, b = 9일 때
# 2^2 + 9^2 = 4 + 81 = 85 = 36 + 49 = 6^2 + 7^2
# ex. 2 3 4 5 6 7 8 9 / 6 7 의 카드가 있을 때 => 2 9부터 찾게 되는데 이는 답이 아님
# 따라서, 제곱이 아니라 일반 차도 고려해야함
# diff == a + b인지 확인하면 : 2+9 = 11이라 넘어가고, 6+7 = 13이라 답임