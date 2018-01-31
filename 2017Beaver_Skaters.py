ROW = ["P", "Q", "R", "S", "T", "U", "V"]
A = 0

for x in range(60):
    if x <= 60:
        a = ROW[6]
        ROW[6] = ROW[5]
        ROW[5] = ROW[4]
        ROW[4] = ROW[3]
        ROW[3] = ROW[2]
        ROW[2] = ROW[1]
        ROW[1] = ROW[0]
        ROW[0] = a
print(ROW[6])