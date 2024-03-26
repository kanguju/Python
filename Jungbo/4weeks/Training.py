# #range함수
# print(list(range(5)))
# print(list(range(5,15,3)))

# #연습1
# for i in range(1,11):
#     print("*"*i)

# #연습2
# for i in range(1,11):
#     print(" "*(10-i),"*"*i)
    
# #+end문
# x=10
# for i in range(1,11):
#     print(" "*x,end="")
#     print("*"*i)
#     x=x-1


# #연습3
# x=10
# for i in range(1,22,2):
#     print(" "*x,end="")
#     print("*"*i)
#     x=x-1

# #while반복문
# a=0
# while a<10:
#     print("현재 a의 값은",a)
#     a+=1

# #반복문과 조건문
# is_wrong = True
# a=523
# while is_wrong:
#     number=int(input("3자리 정수를 입력하세요"))
#     if number<a:
#         print(f"{number}보다 큽니다.")
#     elif number >a:
#         print(f"{number}보다 작습니다.")
#     elif number ==a:
#         print("정답입니다.")
#         break

# #이중반복,구구단
# for i in range(1,10):
#     for r in range(1,10):
#         print(f"{i}*{r}={i*r}")


# #연습4
# #사용자에게 n이라는 정수를 입력받는다.
# n=int(input("정수를 입력하세요:"))
# #N보다 작은 정수중에 짝수를 모두 출력한다.
# a=1
# is_Wrong=True
# while is_Wrong:
#     if a==n:
#         break
#     elif a%2==0:
#         print(a)
#     a=a+1

#연습5
#사용자에게 n이라는 정수를 입력받는다.
n=int(input("정수를 입력하세요:"))
#N보다 작은 소수를 출력한다.
#(2중반복문써야함.)

#1부터 n까지
for i in range(1,n):
    if n==1 or n==2:
        print(n)
        break
    #현재 숫자가 소수인지판단
    for r in range(2,i):
        if i%r==0:
            break
        elif r==(i-1):
            print(i)
    

    
