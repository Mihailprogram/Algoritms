def tree(m):
    #4 -1 4 1 1  3 4
    sl={}
    mas=[]
    dubl=[]
    s=''
    count_1=0
    count_2=0
    for i in m:
        s+=str(i)

    for i in range(len(m)):
        for z in range(i+1,len(m)):
            if m[i]==m[z] and (m[i] not in dubl):
                mas.append(z)
                count_1+=1

        if s.count(str(m[i]))==1 and m[i]!=-1:

            mas.append(i)

            count_2+=1
        if count_1>0:
            dubl.append(m[i])
            count_1=0
            mas.insert(0,i)
            sl[m[i]]=mas
            mas=[]
        elif count_2>0:
            count_2=0
            sl[m[i]]=mas
            mas=[]
    if s.count(str(m[-1]))==1 and m[-1]!=-1:
        sl[m[-1]]=len(m)-1
    return sl


#{9: [0, 5, 6, 7], 7: [1], 5: [2, 3], 2: [4, 8]}
#print(tree([9,7,5,5,2,9,9,9,2,-1]))
a={0: [1, 3], 4: [2], 3: [4]}
print(tree([-1,0,4,0,3]))
#a=tree([9,7,5,5,2,9,9,9,2,-1])
mas=[0]




zap={}
def higt(num):


    m=[]
    learn=[]
    mas[0] += 1
    if type(a[num])==list:
        for i in  a[num]:

            if i in a:

                for z in a[num]:
                    if z!=i and z not in m:
                        learn.append(z)
                zap[num]=learn

                return higt(i)
            else:
                m.append(i)

    aboba=mas[0]
    mas[0]=0

    return aboba


mas1=[]
for i in a.keys():
    mas1.append(higt(i))
print(max(mas1))
#
# def main():
#     print(higt(tree([9,7,5,5,2,9,9,9,2,-1])))
# if __name__=='__main__':
#     main()


