s = input("Enter the string  ")
li = [i for i in s]
l = len(s)
lis = []
if l % 2 == 0:
    for i in range(l):
        if i == l//2-1 or i == l//2:
            continue
        else:
            lis.append(li[i])
else:
    for i in range(l):
        if i == l//2:
            continue
        else:
            lis.append(li[i])
s = ""
for i in lis:
    s = s+i

print(s)
