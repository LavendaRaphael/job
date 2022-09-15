# int 10 to 2, forward backward same 9 1001
# input intx ? yes or no
def ten2two(
    int_10: int
):
    list_2 = []
    while True:
        a = int_10 // 2
        b = int_10 % 2
        print(a, b)
        list_2.append(b)
        if a == 0:
            return list_2
        int_10 = a

def check(
    int_10
):
    #int_2 = int(int_10, 2)
    list_2 = ten2two(int_10)
    for i in range(len(list_2)):
        if list_2[i] != list_2[-i]:
            print('yes')
            return
    print('no')
    return

int_10 = 10
list_2 = ten2two(int_10)
print(list_2)
check(int_10)
