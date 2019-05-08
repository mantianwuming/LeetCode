import time

for i in range(1,9):
    n = pow(10, i)

    startTime = time.time()
    sum = 0
    for j in range(n):
        sum += j

    endTime = time.time()

    print('10^{} : {}s'.format(i, endTime-startTime))
