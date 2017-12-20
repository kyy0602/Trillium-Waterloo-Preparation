n=5
for x in range(1,5):
    for o in range(x,n*x+1,x):
        print(o,end=' ')
    print(end='\n')