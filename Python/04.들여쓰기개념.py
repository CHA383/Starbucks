# 들여쓰기
# 다른 언어에서의 {} 를 대신할수 있는 코드

listdata = ['a','b','c']
if 'a' in listdata:
    print('a가 list안에 있습니다')
    print(listdata)

    # 보이는 것처럼 들여쓰기의 간격은 동일해야 하고
    # 쓸데없이 공백(스페이스, 탭) 사용 X
    # 만약 들여쓰기를 잘못쓰면 SyntaxError: unexpected indent 오류 발생
else:
    print('a가 listdata에 존재하지 않습니다')