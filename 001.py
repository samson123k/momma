# Q.91
# inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}

# print(inventory)

# Q.92
# inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}

# print(inventory["메로나"][0], "원")

# Q.93
# inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}

# print(inventory["메로나"][1], "개")

# Q.94
# inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
# inventory["월드콘"] = [500, 7]

# print(inventory)

# Q.95
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나':1000}
# a = list(icecream.keys())

# print(a)

# Q.96
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나':1000}
# v = list(icecream.values())

# print(v)

# Q.97
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나':1000}
# v = list(icecream.values())
# print(sum(v))

# Q.98
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나':1000}
# new_product = {'팥빙수': 2700, '아맛나':1000}
# icecream.update(new_product)

# print(icecream)

# Q.99
# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# a = zip(keys, vals)

# print(dict(a))

# Q.100
# date = ['09/05', '09/06', '09/07', '09,08', '09,09']
# close_price = [10500, 10300, 10100, 10800, 11000]
# close_table = dict(zip(date, close_price))

# print(close_table)

# Q.111
# a = input()
# print(2*a)

# Q.112
# a = input()
# a = int(a)

# print(a + 10)

# Q.113
# a = input()
# a = int(a)
# if a % 2 == 0:
#     print("짝수")
    
# else:
#     print("홀수")

# Q.114
# a = input()
# a = int(a) + 20
# if a <= 255:
#     print(a)
# else:
#     print(255)

# Q.115
# a = input()
# a = int(a) - 20
# if 0 <= a <= 255:
#     print(a)
# elif a < 0:
#     print(0)
# else:
#     print(255)

# Q.116
# a = input("현재시간 :")
# # a = int(a)
# b = a.split(":")
# c = b[1]
# if c == "00":
#     print("정각입니다")
# else:
#     print("정각이 아닙니다")

# a = input("현재시간 :")
# if a[-2:] == "00":
#     print("정각입니다")
# else:
#     print("정각이 아닙니다")

# Q.117
# fruit = ["사과", "포도", "홍시"]
# a = input("좋아하는 과일은?:")
# if a in fruit:
#     print("정답입니다")
# else:
#     print("오답입니다")

# Q.118
# warn_investment_list = ["Mincrosoft", "Google", "Naver", "KaKao", "LG"]
# a = input("종목명:")
# if a in warn_investment_list:
#     print("Warning")
# else:
#     print("Non.Warning")

# Q.119
# fruit = {"봄":"딸기", "여름":"토마토", "가을":"사과"}
# a = input("제가 좋아하는 계절은:")
# v_fruit = list(fruit.keys())
# if a in v_fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")
    
# fruit = {"봄":"딸기", "여름":"토마토", "가을":"사과"}
# a = input("제가 좋아하는 계절은:")
# if a in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# Q.120
# fruit = {"봄":"딸기", "여름":"토마토", "가을":"사과"}
# a = input("좋아하는 과일은?:")
# v_fruit = list(fruit.values())
# if a in v_fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# Q.121
# a = input()

# if a.islower():
#     print(a.upper())
# else:
#     print(a.lower())

# Q.122
# a = input("score:")
# a = int(a)

# if 0<a<=20:
#     print("E")
# elif 20<a<=40:
#     print("D")
# elif 40<a<=60:
#     print("C")
# elif 60<a<=80:
#     print("B")
# else:
#     print("A")

# Q.123
# 환율 = {"달러": 1167, 
#         "엔": 1.096, 
#         "유로": 1268, 
#         "위안": 171}
# user = input("입력: ")
# num, currency = user.split()
# print(float(num) * 환율[currency], "원")

# Q.124
# a1 = input("input number1:" )
# a2 = input("input number2:" )
# a3 = input("input number3:" )

# a_list = [int(a1), int(a2), int(a3)]

# solve = max(a_list)
# print(solve)

# Q.125
# phone_num = input("휴대전화 번호 입력:" )
# phone_num = phone_num.split("-")

# if phone_num[0] == "011":
#     print("당신은 SKT 사용자입니다.")
# elif phone_num[0] == "016":
#     print("당신은 KT 사용자입니다.")
# elif phone_num[0] == "019":
#     print("당신은 LGU 사용자입니다.")
# elif phone_num[0] == "010":
#     print("알 수 없음")
# else:
#     print("너 누구야")

# Q.127
# adress = input("주민등록번호:" )
# adress = adress[7]

# if adress == "1" or adress == "3":
#     print("남자")
# elif adress == "2" or adress == "4":
#     print("여자")
# else:
#     print("none")

# Q.128
# a = input("주민등록번호:" )
# a = a.split("-")
# a = a[0]
# a = a[4:]
# if 0<=int(a)<9:
#     print("서울이 아닙니다")
# elif 9<=int(a)<13:
#     print("서울이 맞습니다")
# else:
#     print("fuXX")

# Q.129
# a = input("주민등록번호:" )
# a = list(a)
# a1 = (int(a[0])*2 + int(a[1])*3 + int(a[2])*4 + int(a[3])*5 + int(a[4])*6 + int(a[5])*7 + int(a[7])*8 + int(a[8])*9 + int(a[9])*2 + int(a[10])*3 + int(a[11])*4 + int(a[12])*5)

# a2 = a1 % 11
# if 11 - a2 == int(a[13]):
#     print("유효")
# else:
#     print("무효")

# Q.129-1
# a = "011207-3032419"
# a = list(a)
# del a[6]

# n = 0
# b = 0
# for i in a:
    
#     if i == a[12]:
#         break
    
#     k = float(i) * (2 + n)
#     b +=k
#     n = n + 1
    
#     if n == 8:
#         n = 0
#     else:
#         n = n
    
# sol = b % 11
# if 11 - sol == int(a[12]):
#     print("유효")
# else:
#     print("무효")

# Q.130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

print(btc, type(btc))