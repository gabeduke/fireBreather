INTRODUCTION
------------

fireBreather gathers sensor data from the thermostat sensor and enables or disables the fan control relay according to the user defined thresholds

INSTALLATION
------------

 # (Optional) First install a virtual python env to keep separate from main python installation
 
```bash
git clone https://github.com/gabeduke/fireBreather.git
cd firebreather
[sudo] pip install virtualenv
virtualenv venv
source venv/bin/activate
```
 
 * in root dir run `python setup.py install`
 
 * run `python fireBreather.py` to run the service
