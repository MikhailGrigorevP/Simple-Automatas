f = open('Task2\\result.txt')
nf = f.read()
__A = nf.split('\n')
f.close()
f = open('Task3\\result.txt')
nf = f.read()
__A2 = nf.split('\n')
f.close()

for element in __A2:
    if element not in __A:
        print(element)

