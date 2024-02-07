from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io
import matplotlib.pyplot as plt
import numpy as np

def get_wav_info(wav_file):
    rate, data = wavfile.read(wav_file)
    print(rate, data.shape)
    return rate, data

def graph_spectrogram(wav_file):
    rate, data = get_wav_info(wav_file)
    nfft = 200 # Length of each window segment
    fs = 8000 # Sampling frequencies
    noverlap = 120 # Overlap between windows
    nchannels = data.ndim
    if nchannels == 1:
        pxx, freqs, bins, im = plt.specgram(data, nfft, fs, noverlap = noverlap)
    elif nchannels == 2:
        pxx, freqs, bins, im = plt.specgram(data[:,1], nfft, fs, noverlap = noverlap)
    print(pxx.shape, freqs, bins, im)   
    plt.show()
    return pxx

def data_test():
    samplerate, data = wavfile.read('./src/data/1.wav')
    print(f'rate = {samplerate}Hz, data shape = {data.shape}')
    print(f"number of channels = {data.shape[1]}")

    length = data.shape[0] / samplerate
    print(f"length = {length}s")


    time = np.linspace(0., length, data.shape[0])
    plt.plot(time, data[:, 0], label="Left channel")
    plt.plot(time, data[:, 1], label="Right channel")
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()

if __name__ == '__main__':
    data_test()
    pxx = graph_spectrogram('./src/data/example_train.wav')
    print(pxx[70,20])