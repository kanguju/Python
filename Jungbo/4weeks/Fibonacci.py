n=int(input("숫자를 입력하세요:"))

a,b=1,1
if n==1 or n==2:
    print(a)
for i in range(1,n):
    a,b=b,a+b
    print(a)
print("결과",a)
