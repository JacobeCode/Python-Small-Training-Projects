import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
import pandas as pd
from scipy.io.wavfile import write


class Generator:
    def __init__(self, low_range, high_range, steps):
        self.low_range = low_range
        self.high_range = high_range
        self.steps = steps
        self.t = np.linspace(self.low_range, self.high_range, self.steps)
        self.form = 0

    def sine(self, f, a):
        self.form = a*np.sin(2*np.pi*f*self.t)

    def square(self, f, a):
        self.form = np.sign(a*np.sin(2*np.pi*f*self.t))

    def sawtooth(self, f, a):
        self.form = a * ((self.t * 2 * f / 44.1 - 0.5) % 2) - a

    def triangle(self, f, a):
        phase = ((self.t * 2 * f / 44.1 - 0.5) % 2) - 1
        self.form = 2 * a * np.abs(phase) - a

    def white_noise(self, a):
        self.form = np.random.normal(0, a/4, self.steps)

    def choice(self):
        print("What do you want to do ?\n1. Print chart for waveform.\n2. Calculate Fourier Transform and print chart ")
        print("3. Calculate Fourier Transform and import to csv.\n4. Generate time course and import to .wav file.")
        while True:
            try:
                a = int(input("Please choose correct number : \n"))
                if a == 1:
                    Generator.chart(self)
                    return False
                elif a == 2:
                    Generator.fourier(self, self.t, self.form)
                    return False
                elif a == 3:
                    Generator.write_csv(self, self.t, self.form)
                    return False
                elif a == 4:
                    Generator.import_wav(self, self.form)
                    return False
            except ValueError:
                print("Wrong key. Please insert right one again.")

    def chart(self):
        plt.plot(self.t, self.form)
        plt.xlabel("time")
        plt.ylabel("amplitude")
        plt.grid()
        plt.show()

    def fourier(self, t, y):
        n = len(t)
        dt = t[1] - t[0]
        yf = 2.0 / n * np.abs(fft(y)[0:n // 2])
        xf = np.fft.fftfreq(n, d=dt)[0:n // 2]
        plt.plot(xf, yf)
        plt.grid()
        plt.show()

    def write_csv(self, t, y):
        n = len(t)
        dt = t[1] - t[0]
        yf = 2.0 / n * np.abs(fft(y)[0:n // 2])
        xf = np.fft.fftfreq(n, d=dt)[0:n // 2]
        data = {"t": xf, "y": yf}
        dataframe = pd.DataFrame(data)
        name = str(input("Please input .wav file name you want :\n"))
        dataframe.to_csv(name, index=False, sep="\t")

    def import_wav(self, form):
        name = str(input("Please input .wav file name you want :\n"))
        scaled = np.int16(form * 32767)
        write(name + '.wav', 44100, scaled)
