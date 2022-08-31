x = 0
while x < 10:
    x += 1
    if x < 3:
        continue
    print(x)
    if x > 7:
        break

# for                   while
# 범위가 지정된 자료나   특정조건을 만족하는 경우
# 반복이 가능한 객체를   지속적으로 실행을 할 때 
# 사용할 때              

# while 기본 구조
# while 조건:
#   반복실행코드
#   continue        # 구문처음으로 이동하여 반복문 계속
#   ...
#   break           # while구문 탈출

# 1 ~ n 까지의 합을 구할때,
# 누적합이 10만보다 커질때의 n의 값
x= 1
total = 0
while 1:
    total += x
    if total > 100000:
        print(x)
        print(total)
        break
    x += 1

# while문의 조건이 1이기 때문에 (0 이 아닌 모든 수는 전부 True 값으로 본다. 0 은 False 값)
# 무한루프에 빠진다
# 무한루프일 경우 break문을 적어 빠져나올 수 있게 해주자