# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Emmission spectrum of N2-Birge-Sponer data analysis
x0=[-3e-5,-2.5e-5,-2.3e-5]
y0=[0,1,2]

x1=[-3.1e-5,-3e-5]
y1=[0,1]


x2=[-2.25e-5,-2.04e-5]
y2=[3.1816e-3,3.202e-3]

plt.figure(1)
plt.plot(x1,y1, label = 'Birge-Sponer for zeroeth row')
plt.xlabel( '\u0394 wavenumber,cm-1')
plt.ylabel('v + 1')
plt.title('Birge-Sponer for zeroeth row')
plt.legend()
plt.show()

plt.figure(2)
plt.plot(x0,y0,label = 'Birge-Sponer for first row')
plt.xlabel('\u0394 wavenumber, cm-1')
plt.ylabel('v + 1')
plt.title('Birge-Sponer for first row')
plt.legend()
plt.show()

plt.figure(3)
plt.plot(x2,y1,label = 'Birge-Sponer for second row')
plt.xlabel('\u0394 wavenumber, cm-1')
plt.ylabel('v + 1')
plt.title('Birge-Sponer for second row')
plt.legend()
plt.show()



#Morse Potential
De=1.985e-22
r0=1.2e-10
r=np.linspace(0,1e-9,50)
B=4.07e9
V=De*(1-np.exp(-B*(r-r0)))**2

v=np.linspace(0,5,5)
vbar=400
xevbar=50
c=2.997e8
h=6.626e-34
G_levels=[]
for i in range(5):
    G=((i+1/2)*vbar-((i+1/2)**2)*xevbar)*h*c
    G_levels.append(G)
    



plt.figure(4)
plt.plot(r,V, label ='Morse Potential')
plt.hlines(y=G_levels[0],xmin=0,xmax=1e-9, label = 'G(0)')
plt.hlines(y=G_levels[1],xmin=0,xmax=1e-9, label = 'G(1)')
plt.hlines(y=G_levels[2],xmin=0,xmax=1e-9, label= 'G(2)')
plt.hlines(y=G_levels[3],xmin=0,xmax=1e-9, label = 'G(3)')
plt.hlines(y=G_levels[4],xmin=0,xmax=1e-9, label = 'G(4)')
plt.xlabel('Interatomic distance, (nm)')
plt.ylabel('Energy, (J)')
plt.legend()
plt.title('Morse Potential Plot, with energy levels')
plt.show()

print (G_levels)


#emission spectrum of a continuous source of white light
lambda1=np.linspace(300e-9,300e-8,100)
T=2800
k=1.38064852e-23
I=(2*np.pi*h*c**2)/(lambda1**5*(np.exp((h*c)/(lambda1*k*T))-1))

plt.plot(lambda1,I, label= 'T=2800K')
plt.xlabel('Wavelength, (nm)')
plt.ylabel('Intensity, (counts)')
plt.title('Blackbody at 2800K')
plt.legend()
plt.show()


#Absorption of I2
excel_file = 'part3and4.xlsx'
wavelengths=pd.read_excel(excel_file, usecols=0)
Intensity=pd.read_excel(excel_file,usecols=1)




plt.figure()
plt.plot(wavelengths,Intensity)
plt.xlim(500,516)

plt.legend()
plt.show()


wavelengths1=pd.read_excel(excel_file, usecols=6)
Intensity1=pd.read_excel(excel_file,usecols=7)

plt.figure()
plt.plot(wavelengths1,Intensity1)
plt.xlim(500,516)

plt.legend()
plt.show()


wavelengths2=pd.read_excel(excel_file, usecols=11)
Intensity2=pd.read_excel(excel_file,usecols=12)

plt.figure()
plt.plot(wavelengths2,Intensity2)
plt.xlim(500,516)

plt.legend()
plt.show()



#Emission spectrum of N2
excel_file1='part4.xlsx'
wavelength3=pd.read_excel(excel_file1, usecols=0)
Intensity3=pd.read_excel(excel_file1,usecols=1)

plt.figure()
plt.plot(wavelength3, Intensity3)
plt.xlim(310,420)
plt.xlabel('Wavelength, (nm)')
plt.ylabel('Intensity, (counts)')
plt.title('Emission Spectrum of N2')
plt.legend()
plt.show()


#part 4
wavelength4=[18477,18552,18625]
qn=[28.5,29.5,30.5]

z = np.polyfit(qn,wavelength4, 2)
print (z)
plt.plot(qn,wavelength4, label = 'Anharmonic Eigenvalues')
plt.xlabel( 'wavenumber,cm-1')
plt.ylabel('v + 1/2')
plt.title('Anharmonic Vibrational Transitions')
plt.legend()
plt.show()