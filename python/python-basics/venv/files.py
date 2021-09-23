l = [str(i)+str(i-1) for i in range(20)]
f = open('text.txt', 'w')
for n in l:
    f.write(n +'\n')
f.close()
f = open('text.txt', 'r')
for line in f:
    print(line)

l = [line.strip() for line in f]
print(l)
f.close()