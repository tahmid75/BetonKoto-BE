pop = [3,5,-2]
popList = []

for i in range(2,-1,-1):
    print(pop[i])
    sum = 0

    j = i

    while(j >=0 ):
        sum += pop[j]
        popList.append(sum)
        j+=1


print(popList)