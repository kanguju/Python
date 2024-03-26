#변수입력
n=int(input("총 갯수를 입력하세요:"))
r=int(input("뽑을 갯수를 입력하세요:"))

#factorial,n
nfac=1
for i in range(1,n+1):
    print(i)
    nfac=nfac*i

#factorial,r
for i in range(1,r+1):
    print(i)
    rfac=rfac*1


print(nfac)
print(rfac)


