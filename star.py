row=int(input("Number of rows ? : "))
rows=(row*2)-1
stars=1
for i in range(1):
    for j in range(row-1):
        print(" "*rows,"*"*stars)
        rows-=1
        stars+=2
    for j in range(1):
        print(" "*rows,"*"*stars)
    for j in range(row-1):
        rows+=1
        stars-=2
        print(" "*rows,"*"*stars)


            # or
            
# row=int(input("Number of rows ? : "))
# rows=(row*2)-1
# stars=1
# for i in range(1):
#     for j in range(1):
#         print(" "*rows,"*"*stars)
#     for j in range(row-1):
#         rows-=1
#         stars+=2
#         print(" "*rows,"*"*stars)
#     for j in range(row-2):
#         rows+=1
#         stars-=2
#         print(" "*rows,"*"*stars)
#     for j in range(1):
#         rows+=1
#         print(" "*rows,"*")     
