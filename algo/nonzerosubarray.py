'''Fin non-zero subarray with largest sum'''
arr = [-4, -1, -2, -7, -3, -4]

'''O(N)'''
def bruteforce():
    arrp = [4, -1, 2, -7, 3, 4]
    maxSum = arrp[0]
    for i in range(len(arrp)):
        biggest = 0;
        for x in range(i, len(arrp)):
            biggest += arrp[x]
            maxSum = max(maxSum, biggest)

    print(maxSum)

bruteforce()
'''O(N)'''
def goodforce():
    arrp = [4, -1, 2, -7, 3, 4]
    maxs = arrp[0]
    curs = 0

    for n in arrp:
        curs = max(curs, 0)
        print("curs: " , curs)
        curs += n
        print("curs plus n: " , curs, n)
        maxs = max(maxs, curs)
        print("maxs: ", maxs)
    print(maxs)

goodforce()
