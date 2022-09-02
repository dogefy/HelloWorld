import time

f = open('log.txt', 'w')
a = time.localtime()
a = time.asctime(a)
f.write(str(a))
f.write('hahaha')
f.close()
for i in range(100):
    pass
