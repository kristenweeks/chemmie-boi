# -*- coding: utf-8 -*-

import pandas as pd
import sys
import csv
import webbrowser
import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt

#Ask how many trials were ran to make the program generic for the spectrometer.
Trialnumber=((int(input("How many trials does your CSV include?")))*2) 
header_list=[i for i in range(Trialnumber)]
wavcol=[]
for x in header_list:
    wavcol.append(x % 2==0)
intcol=[]
for x in header_list:
    intcol.append(x % 2==1)

#Ask for the length of the longest trial ran in excel to make the program generic for the spectrometer
Length=(int(input("What is the length of your longest trial in excel (#of cells in excel):"))-1)


#Names of the trials will be exported into a list (trialnames) for later use
csvfile = open('emissiondata.csv','r')
csvreader1 = csv.reader(csvfile)
for i in range(1):
    trialnames=(csvreader1.__next__())
csvfile.close()

#reading in the csv file using pandas
df = pd.read_csv('emissiondata.csv',header=0, skiprows=1, nrows=Length)

#normalize the dataframe
#first find the max of the intensity values
maxvalues=df.iloc[:,intcol].max()
max=maxvalues.max()
max=int(max)
#Divide all intensities by the max and multiply by 100

df.iloc[:,intcol]/= max
df.iloc[:,intcol]*= 100

#List the lambda maxes
mi1=df['I1'].idxmax()
mi1=int(mi1)
print("Lambda max 1 is:", df.loc[mi1,'W1'])
mi2=df['I2'].idxmax()
mi2=int(mi2)
print("Lambda max 2 is:", df.loc[mi2,'W2'])
mi3=df['I3'].idxmax()
mi3=int(mi3)
print("Lambda max 3 is:", df.loc[mi3,'W3'])
mi4=df['I4'].idxmax()
mi4=int(mi4)
print("Lambda max 4 is:", df.loc[mi4,'W4'])
mi5=df['I5'].idxmax()
mi5=int(mi5)
print("Lambda max 5 is:", df.loc[mi5,'W5'])

LML = [df.loc[mi1,'W1'],df.loc[mi2,'W2'],df.loc[mi3,'W3'],df.loc[mi4,'W4'],df.loc[mi5,'W5']]
#Plot in color of lambda max (im sure there is a more simple way of doing this but i could not figure it out)
colordict={"r1":"red","r2":"lightcoral","r3":"indianred","r4":"maroon","r5":"darkred","O1":"lightsalmon","O2":"tomato","O3":"coral","O4":"orange","O5":"darkorange","Y1":"lemonchiffon","Y2":"khaki","Y3":"palegoldenrod","Y4":"lightyellow","Y5":"yellow","G1":"palegreen","G2":"limegreen","G3":"green","G4":"darkolivegreen","G5":"darkgreen","B1":"aqua","B2":"powderblue","B3":"royalblue","B4":"blue","B5":"navy","V1":"orchid","V2":"magenta","V3":"violet","V4":"darkviolet","V5":"indigo"}
color1=[]
for i in LML:
    if i <=450:
        color1.append(colordict["V1"])
        break
    elif i > 450 and i <= 495:
        color1.append(colordict["B1"])
        break
    elif i > 495 and i <= 570:
        color1.append(colordict["G1"])
        break
    elif i > 570 and i <= 590:
        color1.append(colordict["Y1"])
        break
    elif i > 590 and i <= 620:
        color1.append(colordict["O1"])
        break
    elif i<= 750:
        color1.append(colordict["R1"])
        break
color2=[]
for i in LML:
    if i <=450:
        color2.append(colordict["V2"])
        break
    elif i > 450 and i <= 495:
        color2.append(colordict["B2"])
        break
    elif i > 495 and i <= 570:
        color2.append(colordict["G2"])
        break
    elif i > 570 and i <= 590:
        color2.append(colordict["Y2"])
        break
    elif i > 590 and i <= 620:
        color2.append(colordict["O2"])
        break
    elif i<= 750:
        color2.append(colordict["R2"])
        break
color3=[]
for i in LML:
    if i <=450:
        color3.append(colordict["V3"])
        break
    elif i > 450 and i <= 495:
        color3.append(colordict["B3"])
        break
    elif i > 495 and i <= 570:
        color3.append(colordict["G3"])
        break
    elif i > 570 and i <= 590:
        color3.append(colordict["Y3"])
        break
    elif i > 590 and i <= 620:
        color3.append(colordict["O3"])
        break
    elif i<= 750:
        color3.append(colordict["R3"])
        break
color4=[]
for i in LML:
    if i <=450:
        color4.append(colordict["V4"])
        break
    elif i > 450 and i <= 495:
        color4.append(colordict["B4"])
        break
    elif i > 495 and i <= 570:
        color4.append(colordict["G4"])
        break
    elif i > 570 and i <= 590:
        color4.append(colordict["Y4"])
        break
    elif i > 590 and i <= 620:
        color4.append(colordict["O4"])
        break
    elif i<= 750:
        color4.append(colordict["R4"])
        break
        
color5=[]
for i in LML:
    if i <=450:
        color5.append(colordict["V5"])
        break
    elif i > 450 and i <= 495:
        color5.append(colordict["B5"])
        break
    elif i > 495 and i <= 570:
        color5.append(colordict["G5"])
        break
    elif i > 570 and i <= 590:
        color5.append(colordict["Y5"])
        break
    elif i > 590 and i <= 620:
        color5.append(colordict["O5"])
        break
    elif i<= 750:
        color5.append(colordict["R5"])
        break

#Plot data on same axes
n=50
df['max1'] = df.iloc[argrelextrema(df.I1.values, np.greater_equal, order=n)[0]]['I1']
df['max2'] = df.iloc[argrelextrema(df.I2.values, np.greater_equal, order=n)[0]]['I2']
df['max3'] = df.iloc[argrelextrema(df.I3.values, np.greater_equal, order=n)[0]]['I3']
df['max4'] = df.iloc[argrelextrema(df.I4.values, np.greater_equal, order=n)[0]]['I4']
df['max5'] = df.iloc[argrelextrema(df.I5.values, np.greater_equal, order=n)[0]]['I5']
ax=df.plot.scatter(x='W1',y='I1',c=color1);
df.plot.scatter(x='W2',y='I2',c=color2,ax=ax);
df.plot.scatter(x='W3',y='I3',c=color3,ax=ax);
df.plot.scatter(x='W4',y='I4',c=color4,ax=ax);
df.plot.scatter(x='W5',y='I5',c=color5,ax=ax);
df.plot.scatter(x='W1',y='max1',c="black",ax=ax);
df.plot.scatter(x='W2',y='max2',c="black",ax=ax);
df.plot.scatter(x='W3',y='max3',c="black",ax=ax);
df.plot.scatter(x='W4',y='max4',c="black",ax=ax);
df.plot.scatter(x='W5',y='max5',c="black",ax=ax)
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Normalized intensity")
plt.show()
plt.savefig("Emissiongraph.png")
#Summarize results on a website
url = "file:///C:/Users/tinkw/OneDrive/Programming/Finalproject.html"
webbrowser.open_new(url)