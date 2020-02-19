a= ["234794","343334","333344","236678"]
L=len(a)
C=len (a[0])
b=["3","6"]
l=len(b)
c=len (b[0])
a[1][1:3]
tt= [-1,-1]
for i in range(L - l +1):
    print("i"+str(i))
    for j in range (C-c +1):
        print("j"+str(j))
        ver=1
        for k in range(l):
            print("k"+str(k))
            print("a"+str(a[i][j+k:j+k+l])+"b"+str(b[k][:]))
            if(a[i+k][j:j+c]!= b[k][:]):
                ver=0
                break
        if (ver==1):
            tt=[i,j]
            break
    if (ver==1):
        break
print(tt)
len(b)
for i in range(30):
    if (i%2==0):
        print(str(i))

import datetime
delta=datetime.timedelta(days=6)
today =datetime.date.day
today=today+delta
today.AddYears(2)