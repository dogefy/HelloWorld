import time
f=open('log.txt','w')
a=time.localtime()
a=time.asctime(a)
f.write(str(a))
f.close()