int_data = 1                        # 정수 선언
float_data = 3.14                   # 실수 선언
complex_data = 1 + 5j               # 복소수 선언

# 수치형 자료
# 정수형 : -1,0,1같은 정수
# 실수형 : 분수로 표현가능한 유리수, 무리수를 포함한 실수
# 복소수 : 실수 + 허수 로 구성된 복소수 (이해가 잘 안됨)
# 복소수형 상수를 선언할때 허수부분에 j를 붙인다


str_data1 = 'I love python'         # 문자열 선언 (영문)
str_data2 = "반갑습니다"             # 문자열 선언 (한글)

# 문자형 자료
# 한글자 이상의 문자나 숫자, 기호로 구성된 배열
# ''로 감싸 대입하는 방법, ""로 감싸 대입하는 방법 두가지가 있다


list_data = [1,2,3]                 # 리스트 선언  

# 리스트 자료
# [] 안에 객체를 순서대로 나열한 자료형이다
# 각 요소는 콤마로 구분한다
# 리스트의 각 요소는 임의의 자료형이나 객체가 될수 있다


tuple_data = (1,2,3)                # 튜플 선언

# 튜플형 자료
# 리스트와 비슷하지만 요소값을 변경할 수 없다 (C 에서의 static이나 define 느낌?)


dict_data = {0:'False', 1:'True'}   # 사전 선언

# 사전 자료
# {} 안에 키 : 값 으로된 쌍이 요소로 구성된 자료
# 순서가 없으므로 인덱스로 값에 접근불가
# 리스트처럼 콤마로 각 요소를 구분하며, 키를 이용해 대응되는 값에 접근


# 반복 가능한 자료형
# for문에서 in 다음에 사용될 수 있는 자료형을 말한다
# 반복가능한 자료형으로 쓸 수 있는것 (취급되는 것)
# 문자열, 리스트, 튜플, 사전등등 다용한 객체 형태로 존재
# 반복 가능한 자료형은 파이썬 내장함수 list()를 이용해 리스트 자료로 변환할 수 있다