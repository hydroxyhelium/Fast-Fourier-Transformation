## Analog to DSP converter 
from random import sample
import numpy as np
import matplotlib.pyplot as plt

from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io
import numpy as np
from cmath import exp
from cmath import pi 


class Signal(): 
    def __init__(self, path):
        self.path = path 
        self.samplerate, self.data = wavfile.read(path)
        self.dtf = []
        self.amp = []
        print("data successfully read")

    def visualize(self):
        data = self.data
        samplerate = self.samplerate
        length  = data/ samplerate
        time = np.linspace(0., length, data.shape[0])
        plt.plot(time, data)
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.show()

    def change_frequency(self, frequency):
        data = [x for x in self.data]
        output = [] 
        samplerate = self.samplerate

        if(frequency>samplerate):
            print("Sorry we can't do that")

        ratio = samplerate/frequency

        point_in_100 = int(ratio*100) 

        j = 0 
        while(j+100 < len(data)):
            temp = sample(data[j:j+100], point_in_100)
            output.extend(temp)
            j += 100

        self.data = output 
    

    def DFT(self):
        data=self.data 

        signals = [x*100 for x in range(1, 200)]
        amp = []

        for i in range(len(signals)):
            frequency = signals[i]

            sum = 0

            for j, amplitude in enumerate(data): 
                sum += amplitude*(exp(pi*(-1j)*2*frequency*i/len(data)))
            
            amp.append(sum)
        
        self.amp = amp 
        
        return amp
        

signal_obj = Signal('/Users/priyanshusharma/Documents/signal-processing/audio/StarWars3.wav')



print(signal_obj.DFT())
