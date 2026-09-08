# def say_myself(name, man=True, age): 초기화 하고 싶은 매개 변수는 항상 뒤로
def say_myself(name, age, man = True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % age)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")

say_myself("박응용", 27)

