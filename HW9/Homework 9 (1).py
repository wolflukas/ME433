#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import *


# In[26]:


#Reading each file and assigning lists for each column
col_names = ["time", "value"]
sigA = pd.read_csv(R"C:\Users\lwolf\Documents\GitHub\ME433\HW9\sigA.csv", names = col_names)
timeA = sigA['time'].tolist()
valuesA = sigA['value'].tolist()

col_names = ["time", "value"]
sigB = pd.read_csv(R"C:\Users\lwolf\Documents\GitHub\ME433\HW9\sigB.csv", names = col_names)
timeB = sigB['time'].tolist()
valuesB = sigB['value'].tolist()

col_names = ["time", "value"]
sigC = pd.read_csv(R"C:\Users\lwolf\Documents\GitHub\ME433\HW9\sigC.csv", names = col_names)
timeC = sigC['time'].tolist()
valuesC = sigC['value'].tolist()

col_names = ["time", "value"]
sigD = pd.read_csv(R"C:\Users\lwolf\Documents\GitHub\ME433\HW9\sigD.csv", names = col_names)
timeD = sigD['time'].tolist()
valuesD = sigD['value'].tolist()


# In[3]:


#Finding Sample Rates
sampA = len(timeA)/(timeA[-1]-timeA[0])
sampB = len(timeB)/(timeB[-1]-timeB[0])
sampC = len(timeC)/(timeC[-1]-timeC[0])
sampD = len(timeD)/(timeD[-1]-timeD[0])


# In[4]:


#Using Matplotlib
import matplotlib.pyplot as plt # for plotting
import numpy as np # for sine function
import math

plt.plot(timeD,valuesD,'b-*')
plt.xlabel('Time [s]')
plt.ylabel('Signal')
plt.title('Signal vs Time')
plt.show()


# In[5]:


#Converting sigA to freq
s = valuesA

Fs = sampA # sample rate
Ts = 1.0/Fs; # sampling interval
ts = np.arange(0,timeA[-1],Ts) # time vector
y = s # the data to make the fft from
n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq = frq[range(int(n/2))] # one side frequency range
Y = np.fft.fft(y)/n # fft computing and normalization
Y = Y[range(int(n/2))]

print(len(y))
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(timeA,y,'b')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude for A')
ax2.loglog(frq,abs(Y),'b') # plotting the fft
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|Y(freq)| for A')
plt.show()


# In[6]:


#Converting sigB to freq
s = valuesB

Fs = sampB # sample rate
Ts = 1.0/Fs; # sampling interval
ts = np.arange(0,timeB[-1],Ts) # time vector
y = s # the data to make the fft from
n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq = frq[range(int(n/2))] # one side frequency range
Y = np.fft.fft(y)/n # fft computing and normalization
Y = Y[range(int(n/2))]

print(len(y))
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(timeB,y,'b')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude for B')
ax2.loglog(frq,abs(Y),'b') # plotting the fft
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|Y(freq)| for B')
plt.show()


# In[7]:


#Converting sigC to freq
s = valuesC

Fs = sampC # sample rate
Ts = 1.0/Fs; # sampling interval
ts = np.arange(0,timeC[-1],Ts) # time vector
y = s # the data to make the fft from
n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq = frq[range(int(n/2))] # one side frequency range
Y = np.fft.fft(y)/n # fft computing and normalization
Y = Y[range(int(n/2))]

print(len(y))
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(timeC,y,'b')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude for C')
ax2.loglog(frq,abs(Y),'b') # plotting the fft
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|Y(freq)| for C')
plt.show()


# In[8]:


#Converting sigD to freq
s = valuesD

Fs = sampD # sample rate
Ts = 1.0/Fs; # sampling interval
ts = np.arange(0,timeD[-1],Ts) # time vector
y = s # the data to make the fft from
n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq = frq[range(int(n/2))] # one side frequency range
Y = np.fft.fft(y)/n # fft computing and normalization
Y = Y[range(int(n/2))]

print(len(y))
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(timeD,y,'b')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude for D')
ax2.loglog(frq,abs(Y),'b') # plotting the fft
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|Y(freq)| for D')
plt.show()


# In[9]:


#Low Pass Filter for SigA
x = 10
newvalsA = []
for i in range(len(valuesA)):
     tots = sum(valuesA[i-x:i])
     average = tots/x
     newvalsA.append(average)

plt.plot(timeA, valuesA, color='k', label='unfiltered')
plt.plot(timeA, newvalsA, color='r', label='filtered')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Filtered vs. Unfiltered Data SigA, Data Points Averaged:10 ")
plt.legend()
plt.show()




# In[10]:


#Low Pass Filter for SigB
x = 15
newvalsB = []
for i in range(len(valuesB)):
     tots = sum(valuesB[i-x:i])
     average = tots/x
     newvalsB.append(average)

plt.plot(timeB, valuesB, color='k', label='unfiltered')
plt.plot(timeB, newvalsB, color='r', label='filtered')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Filtered vs. Unfiltered Data SigB, Data Points Averaged:15 ")
plt.legend()
plt.show()




# In[11]:


#Low Pass Filter for SigC
x = 1000
newvalsC = []
for i in range(len(valuesC)):
     tots = sum(valuesC[i-x:i])
     average = tots/x
     newvalsC.append(average)

plt.plot(timeC, valuesC, color='k', label='unfiltered')
plt.plot(timeC, newvalsC, color='r', label='filtered')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Filtered vs. Unfiltered Data SigC, Data Points Averaged:1000 ")
plt.legend()
plt.show()




# In[12]:


#Low Pass Filter for SigA
x = 15
newvalsD = []
for i in range(len(valuesD)):
     tots = sum(valuesD[i-x:i])
     average = tots/x
     newvalsD.append(average)

plt.plot(timeD, valuesD, color='k', label='unfiltered')
plt.plot(timeD, newvalsD, color='r', label='filtered')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Filtered vs. Unfiltered Data SigD, Data Points Averaged:15")
plt.legend()
plt.show()




# In[13]:


#Low Pass Filter with IIR for SigA
A = 0.5
B = 0.5
newvalsA = [0]
for i in range(len(valuesA)):
     newpoint = A*newvalsA[i-1]+B*valuesA[i]
     newvalsA.append(newpoint)

newvalsA.remove(0)
plt.plot(timeA, valuesA, color='k', label='unfiltered')
plt.plot(timeA, newvalsA, color='r', label='filtered')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Filtered vs. Unfiltered Data SigA, A = 0.5 , B = 0.5 ")
plt.legend()
plt.show()




# In[14]:


#Low Pass Filter with IIR for SigB
A = 0.8
B = 0.2
newvalsB = [0]
for i in range(len(valuesB)):
     newpoint = A*newvalsB[i-1]+B*valuesB[i]
     newvalsB.append(newpoint)

newvalsB.remove(0)
plt.plot(timeB, valuesB, color='k', label='unfiltered')
plt.plot(timeB, newvalsB, color='r', label='filtered')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Filtered vs. Unfiltered Data SigB, A = 0.8 , B = 0.2 ")
plt.legend()
plt.show()




# In[15]:


#Low Pass Filter with IIR for SigC
A = 0.9
B = 0.1
newvalsC = [0]
for i in range(len(valuesC)):
     newpoint = A*newvalsC[i-1]+B*valuesC[i]
     newvalsC.append(newpoint)

newvalsC.remove(0)
plt.plot(timeC, valuesC, color='k', label='unfiltered')
plt.plot(timeC, newvalsC, color='r', label='filtered')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Filtered vs. Unfiltered Data SigC, A = 0.9 , B = 0.1 ")
plt.legend()
plt.show()


# In[16]:


#Low Pass Filter with IIR for SigD
A = 0.4
B = 0.6
newvalsD = [0]
for i in range(len(valuesD)):
     newpoint = A*newvalsD[i-1]+B*valuesD[i]
     newvalsD.append(newpoint)

newvalsD.remove(0)
plt.plot(timeD, valuesD, color='k', label='unfiltered')
plt.plot(timeD, newvalsD, color='r', label='filtered')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Filtered vs. Unfiltered Data SigD, A = 0.4 , B = 0.6 ")
plt.legend()
plt.show()


# In[40]:


#FIR for SigA
Coef= [
    0.000000000000000000, 0.000107471582249417,0.000489445559985020,0.000797744264715327,-0.000000000000000001,
    -0.003185446950930511,-0.008958597724915779,-0.014708972158554308,-0.014323472521224501,0.000000000000000005,
    0.033405462945619017,0.083653989989879274,0.139357676236242706,0.183331306629546442,0.200066784294775396,
    0.183331306629546442,0.139357676236242733,0.083653989989879288,0.033405462945619024,0.000000000000000005,
    -0.014323472521224510,-0.014708972158554316,-0.008958597724915798,-0.003185446950930513,-0.000000000000000001,
    0.000797744264715328,0.000489445559985019,0.000107471582249418,0.000000000000000000,
]
sumnew = []
newvalsA = [0]*30
for i in range(len(valuesA)):
    for j in range(len(Coef)):
        if j ==0:
            sumnew = []
            sumnew.append(Coef[j]*valuesA[i-j])
        else:
            sumnew.append(Coef[j]*valuesA[i-j])
    newvalue = sum(sumnew)
    newvalsA.append(newvalue)
del newvalsA[0:30] 

plt.plot(timeA, valuesA, color='k', label='unfiltered')
plt.plot(timeA, newvalsA, color='r', label='filtered')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("FIR for sigA, cutoff=100Hz, Bandwidth=60Hz, 30 coefficients")
plt.legend()
plt.show()



# In[41]:


#FIR for SigB
Coef=[
    0.000000000000000000, -0.000005844052064368, -0.000023820134943225, -0.000054014799697821, -0.000095582479747764, -0.000146488652240137, -0.000203195486496576, -0.000260312240141827, -0.000310242125590523, -0.000342864778695147,
    -0.000345297969930517,-0.000301783157890913,-0.000193736507668975,0.000000000000000000,0.000302683516790705, 0.000738961467904740,0.001333935369994300,0.002112021425993310,0.003095649626814402,0.004303859403838475, 0.005750863568281213, 0.007444662160847579, 0.009385792950955006, 0.011566304999335716, 0.013969035618708839,
    0.016567259316002080, 0.019324760360190832, 0.022196359357808549, 0.025128899832021673, 0.028062674748091803, 0.030933246829661972, 0.033673592044276793, 0.036216474422077878, 0.038496943856761001, 0.040454837896876573, 0.042037164583642997, 0.043200246523484170, 0.043911516541016181, 0.044150871927461845, 0.043911516541016181,
    0.043200246523484170,0.042037164583643004,0.040454837896876573,0.038496943856761001,0.036216474422077892, 0.033673592044276793,0.030933246829661989,0.028062674748091803, 0.025128899832021680, 0.022196359357808556, 0.019324760360190832, 0.016567259316002090, 0.013969035618708835, 0.011566304999335721, 0.009385792950955010,
    0.007444662160847576, 0.005750863568281216, 0.004303859403838477, 0.003095649626814402, 0.002112021425993311,
    0.001333935369994301, 0.000738961467904741, 0.000302683516790706, 0.000000000000000000, -0.000193736507668975,
    -0.000301783157890913, -0.000345297969930516, -0.000342864778695147, -0.000310242125590522, -0.000260312240141827,
    -0.000203195486496576,-0.000146488652240137,-0.000095582479747764,-0.000054014799697822,-0.000023820134943225,
    -0.000005844052064368, 0.000000000000000000,
]
sumnew = []
newvalsB = [0]*30
for i in range(len(valuesB)):
    for j in range(len(Coef)):
        if j ==0:
            sumnew = []
            sumnew.append(Coef[j]*valuesB[i-j])
        else:
            sumnew.append(Coef[j]*valuesB[i-j])
    newvalue = sum(sumnew)
    newvalsB.append(newvalue)
del newvalsB[0:30]
plt.plot(timeB, valuesB, color='k', label='unfiltered')
plt.plot(timeB, newvalsB, color='r', label='filtered')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("FIR for sigB, cutoff=20Hz, Bandwidth=60Hz, 77 coefficients")
plt.legend()
plt.show()



# In[36]:


#FIR for SigC
Coef=[0.000000000000000000,0.000006654468709502,0.000029128522936023,0.000071630294094485,0.000139045364715286,0.000237018146420107, 0.000371990776314115, 0.000551191427798928, 0.000782566139698271, 0.001074650878794299,0.001436383452247726, 0.001876857948081446, 0.002405027463171737, 0.003029363833662816, 0.003757485769150283,
    0.004595769074907365, 0.005548954406576212, 0.006619769140808002, 0.007808580390891126, 0.009113095905728782, 0.010528128553079571, 0.012045438326481696, 0.013653663385294468, 0.015338348625262888, 0.017082076796941639,
    0.018864703378109852, 0.020663692418049256, 0.022454546570933227, 0.024211320690754524, 0.025907204835505290,0.027515159476891312,0.029008583268927898,0.030361992005490210,0.031551686475304340,0.032556386852028101,
    0.033357812050676970,0.033941184117168982,0.034295640137166114,0.034414537262454484,0.034295640137166114,0.033941184117168982,0.033357812050676984,0.032556386852028101,0.031551686475304340,0.030361992005490220,0.029008583268927898,0.027515159476891322,0.025907204835505290,0.024211320690754531,0.022454546570933234,
    0.020663692418049256,0.018864703378109866,0.017082076796941632,0.015338348625262895,0.013653663385294473,0.012045438326481693,0.010528128553079576,0.009113095905728785,0.007808580390891126,0.006619769140808005,0.005548954406576217,0.004595769074907367,0.003757485769150290,0.003029363833662813,0.002405027463171739,
    0.001876857948081447,0.001436383452247725,0.001074650878794302,0.000782566139698270,0.000551191427798929,
    0.000371990776314116,0.000237018146420106,0.000139045364715286,0.000071630294094485,0.000029128522936022,
    0.000006654468709502,0.000000000000000000,
]
sumnew = []
newvalsC = [0]*30
for i in range(len(valuesC)):
    for j in range(len(Coef)):
        if j ==0:
            sumnew = []
            sumnew.append(Coef[j]*valuesC[i-j])
        else:
            sumnew.append(Coef[j]*valuesC[i-j])
    newvalue = sum(sumnew)
    newvalsC.append(newvalue)
del newvalsC[0:30]
plt.plot(timeC, valuesC, color='k', label='unfiltered')
plt.plot(timeC, newvalsC, color='r', label='filtered')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("FIR for sigC, cutoff=10Hz, Bandwidth=60Hz, 77 coefficients")
plt.legend()
plt.show()



# In[39]:


#FIR for SigD
Coef=[0.000000000000000000,-0.000001319141083373,-0.000015037313908626,-0.000048929861550471,-0.000093996664133037,
    -0.000121097214665483,-0.000087940706624356,0.000043173644613606,0.000281036018594741,0.000583343861189437,0.000848013234296021,
    0.000928130925893553, 0.000674576914741099, -0.000000000000000001, -0.001053922749802707, -0.002272668217137566,
    -0.003275996229222991,-0.003593354611233491,-0.002804226036126631,-0.000713809294050129,0.002488908659412765,
    0.006154250435223402, 0.009230072602858803, 0.010477456279280485, 0.008818454391629834, 0.003739623152209966,
    -0.004362056504063843,-0.014012247373391169,-0.022763272224928108,-0.027597084946237208,-0.025571469013799610,-0.014573549491730026,
    0.006006621874578889,0.034872852321315616,0.068829121009071376,0.103238579440193781,0.132861903510084645,0.152896816951269054,
    0.159978084734463205,0.152896816951269054,0.132861903510084645,0.103238579440193795,0.068829121009071376,0.034872852321315616,
    0.006006621874578891,-0.014573549491730026,-0.025571469013799617,-0.027597084946237208,-0.022763272224928115,-0.014012247373391174,-0.004362056504063843,
    0.003739623152209968,0.008818454391629831,0.010477456279280491,0.009230072602858807,0.006154250435223401,0.002488908659412767,
    -0.000713809294050129,-0.002804226036126631,-0.003593354611233493,-0.003275996229222994,-0.002272668217137566, -0.001053922749802709,
    -0.000000000000000001, 0.000674576914741099, 0.000928130925893554, 0.000848013234296021, 0.000583343861189439, 0.000281036018594740, 0.000043173644613606,
    -0.000087940706624357, -0.000121097214665482, -0.000093996664133037, -0.000048929861550471, -0.000015037313908625, -0.000001319141083373, 0.000000000000000000,
]
sumnew = []
newvalsD = [0]*30
for i in range(len(valuesD)):
    for j in range(len(Coef)):
        if j ==0:
            sumnew = []
            sumnew.append(Coef[j]*valuesD[i-j])
        else:
            sumnew.append(Coef[j]*valuesD[i-j])
    newvalue = sum(sumnew)
    newvalsD.append(newvalue)
del newvalsD[0:30]
plt.plot(timeD, valuesD, color='k', label='unfiltered')
plt.plot(timeD, newvalsD, color='r', label='filtered')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("FIR for sigD, cutoff=80Hz, Bandwidth=60Hz, 77 coefficients")
plt.legend()
plt.show()


