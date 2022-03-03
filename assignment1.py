m1 = [
    [2 3 3 4]
    [4 4 4 4]
    [1 1 1 1]
]
m2 = [
    [2 3 3 4]
    [4 4 4 4]
    [1 1 1 1]
]
res = []
for row in range(len(m1)):
    t = []
    for column in range(len(m2)):
        t.append(m2[row][column] - m1[row][column])
    res.append(t)

print(res)
