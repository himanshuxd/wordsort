fname = input("Enter file name: ")
fh = open(fname)
l = list()
for line in fh:
    for word in line.split():
        if word not in l:
            l.append(word)
l.sort()
print(l)
