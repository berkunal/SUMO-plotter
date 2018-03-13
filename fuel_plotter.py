import xml.etree.ElementTree
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

e = xml.etree.ElementTree.parse('output.xml').getroot()

veh_fuelavglist = []
bus_fuelavglist = []
timelist = []

for timestep in e.findall('timestep'):
    veh_count = 0
    veh_fuelsum = 0
    bus_count = 0
    bus_fuelsum = 0
    for vehicle in timestep.findall('vehicle'):
        if vehicle.get('eclass') == "HBEFA3/PC_G_EU4":
            veh_count += 1
            veh_fuelsum += float(vehicle.get('fuel'))
        if vehicle.get('eclass') == "HBEFA3/Bus":
            bus_count += 1
            bus_fuelsum += float(vehicle.get('fuel'))
    if veh_count != 0 and bus_count != 0:
        veh_fuelavglist.append(veh_fuelsum/veh_count)
        bus_fuelavglist.append(bus_fuelsum/bus_count)
        timelist.append(float(timestep.get('time')))
    
x = np.array(timelist)
veh_y = np.array(veh_fuelavglist)
bus_y = np.array(bus_fuelavglist)

plt.plot(x,veh_y,'r', label='Car')
plt.plot(x,bus_y,'b', label='Bus')
plt.legend(loc='upper right')

plt.title("Avarage Fuel Consumption for Vehicles")
plt.xlabel("Time Step")
plt.ylabel("Fuel Consumption (ml/s)")

plt.show()
