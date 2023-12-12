try:
    f = open("none","r")
except FileNotFoundError as e:
    print(e)
else:
    data = f.read()
    print(data)
    f.close()
finally:
    print("프로그램을 종료합니다.")