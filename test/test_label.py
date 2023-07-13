import sys, os

path = os.getcwd() + r'/src'
sys.path.append(path)

import vidlbl

lbl=vidlbl.label()
lbl.label(0,1,2)

print(lbl.out)

file=open('test/test_label.csv','w',encoding='utf-8')
file.write(lbl.out)
file.close()