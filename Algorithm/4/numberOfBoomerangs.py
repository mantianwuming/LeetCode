def numberOfBoomerangs(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    count = 0
    for i in range(len(points)):
        res = {}
        for j in range(len(points)):
            if i != j:
                num = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                if num not in res:
                    res[num] = 1
                else:
                    res[num] += 1
        print(res)
        for num in res:
            if res[num] >= 2:
                count += res[num] * (res[num] - 1)
    return count

points = [[0,0],[1,0],[2,0]]

print(numberOfBoomerangs(points))
