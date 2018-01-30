Mon = [0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1]
Tue = [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0]
Ans = 0

for x in range(12):
    Pro = Mon[x] * Tue[x]
    if Pro == 1:
        Ans += 1        
print(Ans)