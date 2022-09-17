n = int(input())
a = [int(i) for i in (str(input()).split())]
b = []
for i in range(len(a)):
    b.append([max(a), a.index(max(a))])
    a[a.index(max(a))] = 0
 
x = 0
counter = 0
outputs = ''
for el in b:
    counter += (el[0] * x) + 1
    x += 1
    outputs = outputs + str(el[1] + 1) + ' '
print(counter)
print(outputs.rstrip(' '))
