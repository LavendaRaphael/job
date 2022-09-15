#for n in range(10):
#    print(n*9**3, 10**n-1)

def check(
    i
):
    str_i = str(i)
    numx = 0
    for j in range(len(str_i)):
        numx += int(str_i[j])**3
    if (numx == i):
        print(i)

for i in range(100,1000):
    check(i)
