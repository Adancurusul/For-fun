import numpy as np
from scipy import fftpack
import time

start_time = time.time()
size = 5000000
first = np.random.randint(size,size=size)
second = np.random.randint(size,size=size)
print("numpy init time:"+str(time.time()-start_time))
start_time = time.time()
def test():
    np.sum([first,second])
test()
print("numpy sum time :"+str(time.time()-start_time))

