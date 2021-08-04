# cook your dish here
for _ in range(int(input())):
    D,d,P,Q=map(int,input().split())
    total=0
    quotient=D//d
    rem=D%d
    for i in range(quotient):
        total+=d*P
        P=P+Q
    total+=rem*P
    print(total)
