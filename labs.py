from scipy import signal
from scipy.signal import convolve2d
from pylab import *
import numpy as np



f = np.array([[2,3,1],
			  [0,5,1],
			  [1,0,8]])
# f = np.array([[3,4,4],
# [1,0,2],
# [-1,0,3]])
img = np.array([[0,-1,0],
			  [-2,5,1],

				[1,0,-1]
		])

print(convolve2d(img,f,'same'))
def cov2(img, f, strde):
	inw, inh = img.shape
	w, h = f.shape
	outw = (inw - w) / strde + 1
	outh = (inh - h) / strde + 1
	arr = np.zeros(shape=(outw, outh))
	for g in range(outh):
		for t in range(outw):
			s = 0
			for i in range(w):
				for j in range(h):
					s += img[i + g * strde][j + t * strde] * f[i][j]
				# s = img[i][j] * f[i][j]
			arr[g][t] = s
	return arr



