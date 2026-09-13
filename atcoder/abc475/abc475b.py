n = int(input())
a = list(map(int,input().split()))
charge = [] #下3桁=1000で割ったあまりに注目する
for i in a:
    charge.append(i % 1000)
#print(charge)
one = []
ten = []
hundred = []

for i in charge:
    x = 1000 - i
    a = x // 100
    hundred.append(a)
    b = (x - 100*a) // 10
    ten.append(b)
    c = x - 100*a - 10*b
    one.append(c)
print(sum(one))
print(sum(ten))
print(sum(hundred))

