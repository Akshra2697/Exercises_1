list=[]
for i in range(1500, 2701):
    if (i%7==0) and (i%5==0):
        list.append(str(i))
print(list)