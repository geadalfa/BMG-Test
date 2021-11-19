def Iter(num):
    tmpData = []
    for i in range(num+1):
        if i>0:
            if i%2 == 0 or i%5==0 and i%3==0: 
                tmpData.append(str(i))
            else:
                tmpData.append(str(i))
            if i%3==0:
                tmpData.append('Frontend')

            if i%5==0:
                tmpData.append('Backend')

    print(','.join(tmpData))

Iter(50)