# if문의 동작
# number=1
# if number>0:
#     print(1)
#     print(2)
#     print(3)

# if예제
# age=20
# if age<18:
#     print("미성년자입니다.")
#     if age == 20:
#         print("성인 입니다.")
# else:
#     print("성인입니다.")

# 연습 1
# jumsu=float(input("점수를 입력하세요"))
# if jumsu>=90:
#     print("A")
#     grade="A"
# elif jumsu>=80:
#     print("B")
#     grade="B"
# elif jumsu>=70:
#     print("C")
#     grade="C"
# else:
#     print("F")
#     grade="F"
# print(f"당신의 학점은 {grade} 입니다.")

# f
# a=1
# b=11
# c="안녕"
# print(f"{a},{b},{c}")

#연습 2
# 5자리 숫자를 입력받는다.v
# 만약 5자리숫자가 아니라면 “5자리 숫자만 입력하세요” 출력하기.v
# 5자리 숫자가 짝수인지 홀수인지 출력하기.v
# 만약 짝수라면 5의 배수인지 확인후 출력.v
# 만약 홀수라면 3의 배수인지 확인후 출력.v
number=int(input("5자리 숫자를 입력하세요:"))
if number<10000:
    print("5자리 숫자만 입력하세요")
elif number>99999:
    print("5자리 숫자만 입력하세요")

A=number%2
if A==0:
    print("짝수입니다.")
    B=number%5
    if B==0:
        print("5의 배수입니다.")
    elif B!=0:
        print("5의 배수가아닙니다.")
else:
    print("홀수입니다.")
    B=number%3
    if B==0:
        print("3의 배수입니다.")
    elif B!=0:
        print("3의 배수가아닙니다.")