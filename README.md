# CrowdstrikeReport
Simple python script to import and parse info from various sources to see who is in CrowdStrike Falcon
This only depends on the os library which is built into Python 3. This is tested in 3.9 but should run on any modern verison of Python3.

## Known issues with Data

Output data processed through this script should be accurate based on what data is fed to it. The old rule of GIGO always applies. A lot of the process-related stuff like refreshes will not show up in ABR data for months when inactive machines get booted out. Likewise with how it determines who "owns" a machine. If it's a multi-use machine like police often have, it's just going to be HECKIN inaccurate. Or if it gets tied to a DSP tech or something, or the machine is given to a new hire, that data is all highly subject to change and creates false positives. If we had one solution that has absolutely everything in it, such as Ninja One or a similar service where we have control, reliability, and more insight into the inner workings, a lot of this would resolve itself. 

Other inconsistencies, like customers not telling us when someone leaves or moves departments, leading to non-customers being flagged here will always exist until HR fixes their processes.
Please create a [PR](https://github.com/HirschyKirkwood-Work/CrowdstrikeReport/pulls) to add other Known-issues to this Doc.


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

### Export CSV from Crowdstrike of DSP Managed SID

Default Filename value: falconexport.csv

Format: Default.

### Export CSV from Crowdstrike of Self-Managed SID

Default Filename value: self_managed.csv

Format: Default.

### Export LDAP info for Department

Default Filename value: falconusersandgroups.csv

Format: `AndrewID,Given Name,Department`

### Set Active Users Export file

Default Filename value: active_users.csv

This file is your generated output.

### Set Export "Inactive Devices" file

Default Filename Value: inactive_machines.csv

