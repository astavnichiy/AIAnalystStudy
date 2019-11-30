S = str(input("Введите строку S: "))
 
print("Строка \'%s\' имеет длину %d сиволов." % (S, len(S)))

subs_set2 = list(S)

subs_set = set()
print (subs_set2)

for i in range(len(S)):
    print(i)
    for j in range(len(S)-1 if i == 0 else len(S), i, -1):
        print(i, j)
        subs_set.add(hash(S[i:j]))
        
        
print("Количество различных подстрок в этой строке:", len(subs_set))