length = int(input())
s = str(input())
output = ''
counter = 0
for i in range(2, len(s) + 1, 2):
    a = s[i - 2] + s[i - 1]
    if a not in ['ab', 'ba']:
        counter += 1
        if a.count('a') == 2:
            a = 'ab'
        else:
            a = 'ba'
    output = output + a
print(counter)
print(output)
