m1 = [
    [1 1 1 1]
    [2 2 2 2]
    [3 3 3 3]
    [4 4 4 4]
]
m2 = [
    [1 1 1 1]
    [2 2 2 2]
    [3 3 3 3]
    [4 4 4 4]   
]
pro =[]
res = []
for row in range(len(m1)):
    t = []
    for column in range(len(m2)):
        t.append(m2[column][row] * m1[row][column])
    res.append(t)

print(res)
