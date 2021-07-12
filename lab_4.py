#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 09:14:04 2021

@author: alielguindi
"""

#we modified the text files (deleted the headlines and replaced the commas with an empty space)
#In our submission, we are gonna hand out the modified text files so they are executable
import matplotlib.pyplot as plt
  

#Plotting data for the 1st surface
velocity_1 = []
height_1 = []
turb_intensity1 = []
U1 = 0.99 * 4.334865
vert_momentum_flux1 = []
for row in open('BL_1.txt', 'r'):
    rows = [i for i in row.split()]
    velocity_1.append(float(rows[0]))
    height_1.append(float(rows[3]))
    turb_intensity1.append(float(rows[1])/U1)
    vert_momentum_flux1.append(float(rows[2]))
    

      
plt.title('Velocity vs height (Smooth aluminum surface)')
plt.xlabel('velocity')
plt.ylabel('height')

plt.plot(velocity_1, height_1, marker = 'o', c = 'b')
  
plt.show()

      
plt.title('Turbulence intesity vs height (Smooth aluminum surface)')
plt.xlabel('turb_intensity1')
plt.ylabel('height')

plt.plot(turb_intensity1, height_1, marker = 'o', c = 'r')
plt.show()


plt.title('mean vertical momentum flux vs height (Smooth aluminum surface)')
plt.xlabel('vert_momentum_flux1')
plt.ylabel('height')

plt.plot(vert_momentum_flux1, height_1, marker = 'o', c = 'g')
plt.show()


print('Velocity at which we compute the boundary layer height is %f m/s' % U1)
height_1 = 0.3170628
print('Height of the boundary layer1 is %f m' % height_1 )



#-------------------------------------------------------------------------------


#Plotting data for the 2nd surface
velocity_2 = []
height_2 = []
turb_intensity2 = []
U2 = 0.99  * 4.3463
vert_momentum_flux2 = []
for row in open('BL_2.txt', 'r'):
    rows = [i for i in row.split()]
    velocity_2.append(float(rows[0]))
    height_2.append(float(rows[3]))
    turb_intensity2.append(float(rows[1])/U2)
    vert_momentum_flux2.append(float(rows[2]))
    

      
plt.title('Velocity vs height (Rough surface)')
plt.xlabel('velocity')
plt.ylabel('height')

plt.plot(velocity_2, height_2, marker = 'o', c = 'b')
  
plt.show()

plt.title('Turbulence intesity vs height (Rough surface)')
plt.xlabel('turb_intensity2')
plt.ylabel('height')

plt.plot(turb_intensity2, height_2, marker = 'o', c = 'r')
plt.show()


plt.title('mean vertical momentum flux vs height (Rough surface)')
plt.xlabel('vert_momentum_flux2')
plt.ylabel('height')

plt.plot(vert_momentum_flux2, height_2, marker = 'o', c = 'g')
plt.show()





print('Velocity at which we compute the boundary layer height is %f m/s' % U2)

height_2 = 0.45
print('Height of the boundary layer2 is %f m' % height_2 )



#-----------------------------------------------------------------------------------

#Plotting data for the 3rd surface
velocity_3 = []
height_3 = []
turb_intensity3 = []
U3 = 0.99 * 7.28663881183297
vert_momentum_flux3 = []
for row in open('BL_3.txt', 'r'):
    rows = [i for i in row.split()]
    velocity_3.append(float(rows[0]))
    height_3.append(float(rows[3]))
    turb_intensity3.append(float(rows[1])/U3)
    vert_momentum_flux3.append(float(rows[2]))

      
plt.title('Velocity vs height (Modeled urban canopy)')
plt.xlabel('velocity')
plt.ylabel('height')

plt.plot(velocity_3, height_3, marker = 'o', c = 'b')
  
plt.show()


plt.title('Turbulence intesity vs height (Rough surface)')
plt.xlabel('turb_intensity3')
plt.ylabel('height')

plt.plot(turb_intensity3, height_3, marker = 'o', c = 'r')
plt.show()

plt.title('mean vertical momentum flux vs height (Modeled urban canopy)')
plt.xlabel('vert_momentum_flux3')
plt.ylabel('height')

plt.plot(vert_momentum_flux3, height_3, marker = 'o', c = 'g')
plt.show()





print('Velocity at which we compute the boundary layer height is %f m/s' % U3)
height_3 = 0.855
print('Height of the boundary layer3 is %f m' % height_3 )




