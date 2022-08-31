a = 200
msg = 'I love Python'
list_data = ['a','b','c']
dict_data = {'a':97,'b':98}
print(a)
print(msg)
print(list_data)
print(list_data[0])
print(dict_data)
print(dict_data['a'])

# print문은 기본적으로 인자로 입력된 값을 출력한 후 줄바꿈을 한다
# C로 따지자면 printf("코드 \n")로 되어 있는 것
# 만약 print를 쓰면서 줄바꿈을 하지 않으려면 print의 두번째 인자로 end = ""를 지정해주면 된다

print('# ', end = "")
print('#')