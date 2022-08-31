scope = [1,2,3,4,5]

for x in scope:
    print(x)
# 리스트형 scope의 각 요소의 값을 x에 하나씩 대입하여 출력
# 처음부터 끝까지의 요소를 다 돌면서 대입

str = 'abcdef'
for c in str:
    print(c)
# 문자열 str에 대입되어 있는 a부터 f 출력하는 for문

ascii_codes = {'a':97,'b':98,'c':99}
for c in ascii_codes:
    print(c)
# 딕셔너리?형 ascii_codes에 대입되어 있는 각 문자를 출력
# 출력할때는 오른쪽 쌍을 무시하고 왼쪽 쌍에 있는 문자만 출력 (하는듯..?)

for c in range(10):
    print(c)

# 0부터 9까지 출력
# range 함수는 0부터 해당 숫자(n)까지의 값을 요소로 반환 (해주는것 같다)