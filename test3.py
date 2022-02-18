from itertools import combinations

N = [1,2,3,4,5,6,7]
Na = combinations(N,5)

store = {}
print ("ALLE KOMBINATIONEN MIT PRODUKT UND SUMME")
print (" 1 | 2 | 3 | 4 | 5 | Produkt | Summe | ungerade ")
print ("---+---+---+---+---+---------+-------+----------")
for na in Na:
    p = 1
    for n in na:
        p = p * n
    s = sum(na)
    if p in store:
        store[p].append(s)
    else:
        store[p] = [s]
    print (f" {na[0]} | {na[1]} | {na[2]} | {na[3]} | {na[4]} |  {('     ' + str(p))[-6:]} |   {('   ' + str(s))[-3:]} | {['  ','JA'][s%2]}")
    
print ()
print ("ALLE PRODUKTE DIE MEHRFACH VORKOMMEN")
print (" Produkt | Summen")
print ("---------+-----------------")
for key in store.keys():
    if len(store[key]) > 1:
        print (f" {('     ' + str(key))[-6:]} | {' '.join([str(n) for n in store[key]])} ")

print ()
print ("ALLE PRODUKTE DIE MEHRFACH VORKOMMEN UND DEREN SUMME MAL GERADE MAL UNGERADE IST")
print (" Produkt | Summen")
print ("---------+-----------------")
for key in store.keys():
    if len(store[key]) > 1 and ((store[key][0] % 2) != (store[key][1] % 2)):
        print (f" {('     ' + str(key))[-6:]} | {' '.join([str(n) for n in store[key]])} ")
        
        
