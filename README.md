# SUMO-plotter
This application plots graphs of CO2 emission and fuel consumption of various vehicles which simulated with SUMO traffic simulator. 
## Requirements
- [SUMO](http://sumo.dlr.de/userdoc/Installing.html) installation
- [Python](http://www.python.org/) (>= 2.7) installation
- SUMO installation directory has to be writeable
### Generating Simulation Network via OpenStreetMap(OSM)
We are going to use osmWebWizard tool which comes with the SUMO installation.

You start the OSM Web wizard by invoking the following command in the tools directory of SUMO. 

```python osmWebWizard.py```

At the opened browser page, you can choose any desired area for simulation. (You can also set how many vehicles there will be)

![alt text][res/scenerio.png]

Clicking on "Generate Scenario" will trigger generation, and automatically SUMO-gui will appear. But we will not going to use any kind of gui material. So you can close it afterwards.

![alt text][res/simulation.png]

The OSM Web Wizard stores the entire simulation scenario sumo config and intermediate files in a local directory with a name in the format of "yyyy-mm-dd-hh-mm-ss". The data will be stored inside the tools directory.

![alt text][res/timestamp.png]

In order to take emission output, you should run following command in the freshly generated "yyyy-mm-dd-hh-mm-ss" directory. 

Example: `sumo -c "C:\Program Files (x86)\DLR\Sumo\tools\2018-03-13-16-54-59\osm.sumocfg" --emission-output "C:\Users\<your-username>\Desktop\output.xml"` 

*Note: You should create the `output.xml` file before running this command.*

[Example output file](output.xml)

See [this page](http://sumo.dlr.de/userdoc/Simulation/Output.html) for various outputs.
