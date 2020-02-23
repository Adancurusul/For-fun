import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft,ifft




def show(ori_func, ft, sampling_period = 5):
    n = len(ori_func)
    interval = sampling_period / n

    plt.subplot(2, 1, 1)
    plt.plot(np.arange(0, sampling_period, interval), ori_func, 'black')
    plt.xlabel('Time'), plt.ylabel('Amplitude')
    # 绘制变换后的函数
    plt.subplot(2,1,2)
    frequency = np.arange(n / 2) / (n * interval)
    nfft = abs(ft[range(int(n / 2))] / n )
    plt.plot(frequency, nfft, 'red')
    plt.xlabel('Freq (Hz)'), plt.ylabel('Amp. Spectrum')
    plt.savefig("fun.png")
    plt.show()

