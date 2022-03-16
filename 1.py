today = ""

list1=[]
EX_COUNT = {"가슴":0, "등":0}
while True:
    s=input('입력: ')
    list1.append(s)

    print(list1)

    EX_COUNT[s] += 1
    print(EX_COUNT)