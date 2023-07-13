import sys, os

path = os.getcwd() + r'/src'
sys.path.append(path)

import vidlbl

nggyu=vidlbl.video("test/never_gonna_give_you_up.mp4")

nggyu.show()

nggyu.show(speed=2) #2倍速

nggyu.show(start=60) #前60秒快进