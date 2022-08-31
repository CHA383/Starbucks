scope = [1,2,3,4,5]

for x in scope:
    print(x)
    if x < 3:
        continue
    else:
        break

print()
    # 리스트형 scope의 각 요소를 출력한다
    # 단, if문으로 continue와 break를 통해
    # 반복문을 더 세밀하게 쓸수 있다
    # continue : 현재 반복문을 중단하고 다음 반복문 실행
    # break : 반복문 탈출

    # continue없이 위 코드와 동일한 출력결과를 가진 코드를 만들 수 있다

for x in scope:
    print(x)
    if x>= 3:
        break