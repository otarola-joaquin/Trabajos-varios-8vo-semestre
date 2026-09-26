import math
import numpy as np
import matplotlib.pyplot as plt
capas_atmosfericas=[[11000,-0.0065],[20000,0],[32000,0.001],[47000,0.0028],[52000,0],[61000,-0.002],[79000,-0.004],[90000,0.006]]
def altura_geopotencial(h,re=6356766):
    return re*h/(re+h)
def condición_atmosferica(z,delta_temp=0, capas=capas_atmosfericas):
    T_i=(15+delta_temp)+273.15
    P_i=101300
    rho_i=1.225
    R=287.0528
    g_0=9.806645
    kappa=1.4
    if z<0:
        print("Error: Altura geopotencial negativa")
        exit()
    prev_alt=0
    T_z,P_z=T_i,P_i

    for height, gradient in capas:
        if z<=height:
            if gradient!=0:
                T_z=T_i+(gradient*(z-prev_alt))
                P_z=P_i*(T_z/T_i)**(-g_0/(R*gradient))
            else:
                T_z=T_i
                P_z=P_i*math.exp(-g_0*(z-prev_alt)/(R*T_i))
            break
        else:
            if gradient!=0:
                T_top=T_i+(gradient*(height-prev_alt))
                P_top=P_i*(T_top/T_i)**(-g_0/(R*gradient))
            else:
                T_top=T_i
                P_top=P_i*math.exp(-g_0*(height-prev_alt)/(R*T_i))
            T_i,P_i=T_top,P_top
            prev_alt=height
        # print(T_i,P_i)
    rho=P_z/(R*T_z)
    sigma=rho/rho_i
    mach=math.sqrt(kappa*R*T_z)
    # print('temperatura:', T_z, 'K', 'presion:', P_z,'Pa', 'densidad:', rho,'kg/m^3', 'densidad relativa:', sigma, 'numero de mach:', mach, 'm/s')
    return T_z,P_z

# Z=altura_geopotencial(13000)
# print(Z)
a=condición_atmosferica(52000,delta_temp=0, capas=capas_atmosfericas)


# temp=[]
# height=[]
# for i in [i for i in range(52000)]:
#     temp.append(condición_atmosferica(i)[0])
#     height.append(i)
# print(temp)
# plt.plot(temp,height)
# plt.show()


