import xml.etree.ElementTree
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

e = xml.etree.ElementTree.parse('output.xml').getroot()

veh_co2avglist = []
bus_co2avglist = []
timelist = []

for timestep in e.findall('timestep'):
    veh_count = 0
    veh_co2sum = 0
    bus_count = 0
    bus_co2sum = 0
    for vehicle in timestep.findall('vehicle'):
        if vehicle.get('eclass') == "HBEFA3/PC_G_EU4":
            veh_count += 1
            veh_co2sum += float(vehicle.get('CO2'))
        if vehicle.get('eclass') == "HBEFA3/Bus":
            bus_count += 1
            bus_co2sum += float(vehicle.get('CO2'))
    if veh_count != 0 and bus_count != 0:
        veh_co2avglist.append(veh_co2sum/veh_count)
        bus_co2avglist.append(bus_co2sum/bus_count)
        timelist.append(float(timestep.get('time')))
    
x = np.array(timelist)
veh_y = np.array(veh_co2avglist)
bus_y = np.array(bus_co2avglist)

plt.plot(x,veh_y,'r', label='Car')
plt.plot(x,bus_y,'b', label='Bus')
plt.legend(loc='upper right')

plt.title("Avarage CO2 Emission for Vehicles")
plt.xlabel("Time Step")
plt.ylabel("CO2 emission (mg/s)")

plt.show()
