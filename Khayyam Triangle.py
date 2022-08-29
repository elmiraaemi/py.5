a = int(input("rows : "))
b=[[1 for i in range(a)] for j in range(a) ] 
for i in range(0,a):
        for j in range(1,i):
               b[i][j]=b[i-1][j-1] + b[i-1][j]
for i in range(a):
        for j in range(i+1):
                print(b[i][j],end="  ")
        print()