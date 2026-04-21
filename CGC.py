# import keyword
# print(len(keyword.kwlist))

# a = None
# print(a)
# a =10
# print(a)

# s = 'hello EVERYONE'
# print(id(s))
# s = 'healo EVERYONE'
# print(id(s))
# print(s)

# l = [10, 7j-3, False, 9.5, "Hellooo", [45, 5.8]]
# l.append(10000)
# l.insert(0,99999)
# print(l)
# l.remove(False)
# print(l)

# a = (10,)
# print(a)
# print(bool(()))
# t = (10, 7j-3, False, 9.5, "Hello",[45,5.8])
# t[5][0] = 9999
# print(t)

# s = {100, 34.5, 6+7j,"Hello", (7,6,5)}
# print(s)
# s.pop()
# print(id(s))
# s.pop()
# print(id(s))

# d = {"Jhansi" : 1415721, "Tanishq" : 151654121, "Rashi" : 12457963, "Suraj" : 2614812526}
# print(d['Tanishq'])
# d[90]=100
# print(d.())

# data = (10,[20,30,[40,50]],60)

# print(len(data))
# print(data[1])
# print(data[1][2])
# data[1][2][1] = 500
# print(data)

e = 456
f = 256
# print(e  is not f)
# print(id(e))
# print(id(f))
# print(type(e))
# i = 10
# c = 7j-3
# b = False
# f = 9.5
# s = "Hello"
# l = [45,5.8]
# print(e,f,i,c,b,f,s,l,sep=", ")
# print(f'id(i) : {id(i)}, id(c) : {id(c)}')
# age = int(input('Enter a Number : '))
# print(f'My age is {age}')
# print(type(age))
# l = eval(input('Enter a List : '))
# print(f'My List is {l}')
# print(type(l))
# money = int(input('Enter a number : '))
# if money >= 50:
#     print("you bought chocolates")
# else:
#     print("bought other item cheaper than Rs50.")
# print("Exit the shop!")

# money = abs(int(input('Enter a number : ')))
# print(money)
# if money >= 500:
#     print("Proposal Accepted. 😁")
# else:
#     print("Proposal Rejected. 💔")
# print("")

# Wap to Grade depending on the marks
# marks = int(input('Enter your marks : '))
# if marks >= 90 and marks < 100:
#     print('Grade : AA')
# elif marks >= 80:
#     print('Grade : A')
# elif marks >= 59:
#     print('Grade : C')
# elif marks < 59 and marks > 0:
#     print('Grade : F')
# else:
#     print('Input is not correct.')

# marks = int(input('Enter your marks : '))
# if marks >= 90 and marks >=81:
#     print('Grade : AA')
# if marks >= 80 and marks >=71:
#     print('Grade : A')
# if marks >= 59:
#     print('Grade : C')
# if marks < 59:
#     print('Grade : F')

# ch = input("Enter an Character : ")
# if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
#     if ch in 'AEIOUaeiou':
#         print('Vowel')
#     else:
#         print('Consonant')
# else:
#     print("Not an Alphabet.")

# i = 1 #Initialization
# while i < 11: 
#     print(i) #Statement
#     i+=1 #Updation

# i=1 #initialization
# while i < 51:
#     if i%2==0:
#         print(i) 
#     i+=1 #Updation

# n = int(input('Enter the Number to Claculate Factorial : '))
# i = 1
# fact = 1
# while i < n+1:
#     fact=fact*i
#     i+=1
# print(f"Factorial of {n} is {fact}")

# l = [100, 34.5, 6+7j,"Hello", (7,6,5)]
# for i in l:
#     print(i)

# d = {"Jhansi" : 1415721, "Tanishq" : 151654121, "Rashi" : 12457963, "Suraj" : 2614812526}
# for i in d:
#     print(i, d[i])

# s = eval(input('Enter an Collection : '))
# length = 0
# for i in s:
#     length+=1
# print("Length of the Collection is", length)

# s = input('Enter an Collection : ')
# out = ''
# for i in s:
#     if i in 'AEIOUaeiou':
#         out+=i
# print("Vowels :", out)

# for i in range(0,51,3):
#     print(i)

# l = eval(input('Enter an List : '))
# i = 0
# out = 0
# while i < len(l):
#     if type(l[i]) == int:
#         out+=l[i]
#     i+=1
# print(out)

# l = [100, 34.5, 6+7j,"Hello", (7,6,5)]
# for i in l:
#     print(i)


# d = {"Jhansi" : 1415721, "Tanishq" : 151654121, "Rashi" : 12457963, "Suraj" : 2614812526}
# for i in d:
#     print(i, d[i])

# l = [100, 34.5, 6+7j,"Hello", (7,6,5)]
# length = 0
# for i in l:
#     length+=1
# print(length)

# s = input('Enter an String : ')
# out = ''
# for i in s:
#     if i in 'aeiouAEIOU':
#         out=out+i
# print(out)

# print(list(range(0,51,3)))
# for i in range(0,51):
#     if i%3==0:
#         print(i)

# s = input('Enter an String : ')
# p = ''
# for i in s:
#     p = i + p
# if p == s:
#     print('String is palindrome.')
# else:
#     print('String is not palindrome.')

# print(list(set(eval(input('Enter an List :')))))

# l = eval(input("Enter the List : "))
# out = []
# for i in l:
#     if i not in out:
#         out.append(i)
# print(out)

# t = (12, 3.4, 'Hello', 2+3j, 'python', 'bye', False)
# out = {}
# for i in t:
#     if isinstance(i,str):
#         out[i] = len(i)
# print(out)

# s = 'abcabacbcbc'
# out = ''
# for i in s:
#     if i not in out:
#         out+=i+str(s.count(i))
# print(out)

# def sum(a,b):
#     print(a+b)

# print('hello world!')

# sum(10,20)
# sum()
# for i in range(1,10,1):
#     if i%2==0:
#         pass
#     print(i)

# def sum(a,b):
#     return(a+b)

# print('hello world!')
# print(sum(10,20))

# def to_uppercase(string):
#     out = ''
#     for letter in string:
#         if 'a' <= letter <= 'z':
#             out+=chr(ord(letter)-32)
#         else:
#             out+=letter
#     return out
# print(to_uppercase(input('Enter an String : ')))

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact

# print(factorial(int(input("enter a number :"))))

# def sam(a,b = 50):
# 	print('Value Of a : ', a)
# 	print('Value Of b : ', b)
# sam(20)

# def sam(**d):
# 	print(type(d))
# 	print(d)

# sam(a=20,b=30,c=40)

# def sam(*t):
#     print(type(t))
#     for i in t:
#         print(i)

# sam(10,20,30,40,50,60)