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

# N = 3
# a = []
# a[0] = N
# # N[0] = 0
# print(a)

# def mult2(N):
    
#     if N == user:
#         print(N)
#         quit()
#     if N// 10 != 0:
#         a = []
#         for i in str(N):
#             a.append(i)
#         a = list(map(int, a))
#         b = sum(a)
#         c = []
#         for i in str(b):
#             c.append(i)
#         c = list(map(int, c))
#         c = c.pop()
#         N = 10 * int(a[1]) + int(c)
#         mult2(N)

#     else:
#         print(N)
#         quit()
        
# user = input()
# user = int(user)
# mult2(user)

# TKN = input()
# TKN = int(TKN)
# for i in range(TKN):
#     TK = list(map(int, input().split(" ")))
#     M = TK[0]
#     del TK[0]
#     TK_AVE = sum(TK)/len(TK)
    
#     Sus = []
#     for i in range(M):
#         if int(TK[i]) > TK_AVE:
#             Sus.append(TK[i])
#         else:
#             continue
           
#     sol = len(Sus)*100/M
#     sol_error = sol
#     sol = "{:.3f}".format(sol)
#     if sol_error == 0:
#         print("0.000%")
#     else:
#         print(f"{sol}%")

# text = input()
# text = list(text.strip().split(" "))
# print(len(text))

# from string import ascii_uppercase
# alpha = list(ascii_uppercase)
# d = {}
# n = 2
# i = 0
# while True:
    
#     d[n] = list(alpha[i:i+3])
#     n += 1
#     i = i + 3
    
#     if n == 7:
#         d[n] = list(alpha[i:i+4])
#         i = 20
#     elif n == 9:
#         d[n] = list(alpha[i:i+4])
#     if n == 9:
#         break
# print(d)

def hello():
    print("hi")
    
hello()
