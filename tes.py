def Iter(num):
    tmpData = []
    for i in range(1,num+1):

        if i%3==0 :
            tmpData.append('Frontend')
        elif i%5==0:
            tmpData.append('Backend')
        else:
            tmpData.append(str(i))
        if i%5==0 and i%3==0 :
            tmpData.append('Backend')
            

    print(','.join(tmpData))

Iter(50)