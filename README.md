# CrowdstrikeReport
Simple python script to import and parse info from various sources to see who is in CrowdStrike Falcon
This only depends on the os library which is built into Python 3. This is tested in 3.9 but should run on any modern verison of Python3.
## Usage
Linux/Mac
```
git clone https://github.com/HirschyKirkwood-Work/CrowdstrikeReport.git
cd CrowdstrikeReport
chmod +x ./falcon_info.py
./falcon_info.py
```
Windows
```
git clone https://github.com/HirschyKirkwood-Work/CrowdstrikeReport.git
cd CrowdstrikeReport
python3 .\falcon_info.py
```
Note: You should be able to just right-click run it on either OS as well as long as the needed files are in your same directory.
## Setup
All names can be changed in the [final line](./falcon_info.py) where the `falcon.process_info` function is called.
### Export CSV from ABR
Default filename value: dsp_users_and_machine.csv

Format: Default. Full data, comma separated. NOT SEMI! If you have any manual entries to add, make sure to have the hostnames in column 0 (Letter A) and andrewIDs in column 18 (Letter S) at the very bottom.

### Export CSV from Crowdstrike

Default Filename value: falconexport.csv

Format: `Hostname,Last_Seen` (Again, I just paired it down to these two columns)

### Export LDAP info for Department

Default Filename value: falconusersandgroups.csv

Format: `AndrewID,Given Name,Department`

### Set Active Users Export file

Default Filename value: active_users.csv

This file is your generated output.

### Set Export "Inactive Devices" file

Default Filename Value: inactive_machines.csv
