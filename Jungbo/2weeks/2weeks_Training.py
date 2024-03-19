#id값
# x=10
# x=15
# print(id(x))

#변수출력
# r = 5
# p = 3.14
# print("반지름이" ,  r  , "인 원의 면적은" , r*r*p , "입니다.")

#리스트
# a_list=[1,2.5,"jfj",4]
# print(a_list[1])

#딕셔너리
# r=5
# p=170
# a={"이름":"일론머스크","회사":"테슬라","키":p}
# print(a["키"])

#연산자
# a=7
# b=2
# print("덧셈",a+b," 뺄셈",a-b," 곱셈",a*b," 정수나눗셈",a//b," 실수나눗셈",a/b," 나머지",a%b," 지수",a**b)

#+=
# x=0
# x +=2
# print(x)

#비교연산
# x=10
# y=4
# print(x==y)
# print(x!=y)
# print(x>y)
# print(x<y)

#input
# r=int(input("반지름을 입력하세요 :"))
# p=3.14
# print(r,"인 원의 면적은",r**2*p,"입니다.")

#문자연산
# a="10"
# b="20"
# print(a+b)

############## 오늘의과제
#숫자입력
a=int(input("세자리 숫자를 입력하세요:"))

#숫자때어내기
x=a//100
y=a//10-x*10 
z=a-x*100-y*10
print(x,y,z)

#b만들기
b=z*100+y*10+x
print(b)

print("a가b보다큰가?",a>b)

