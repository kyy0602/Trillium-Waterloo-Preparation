Row = ["P", "Q", "R", "S", "T", "U", "V"]
a=0

for x in range(60):
    if x <= 60:
        a = Row [6]
        Row [6] = Row [5]
        Row [5] = Row [4]
        Row [4] = Row [3]
        Row [3] = Row [2]
        Row [2] = Row [1]
        Row [1] = Row [0]
        Row [0] = a
print(Row[6])