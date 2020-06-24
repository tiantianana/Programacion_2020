# -*- coding: utf-8 -*-

def combine(list1, list2):
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i])
        
    for i in range(len(list2)):
        list3.append(list2[i])
        
    maximo = max(list3)
    list3.reverse()
    
    for i in range(maximo):
        while(list3.count(i) > 1):
            list3.remove(i)
    list3.reverse()
    return list3

print(combine([3,6,1,7,23,5,2,1,8],[0,2,35,7,4,5,9,1]))