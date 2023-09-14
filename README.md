# CrowdstrikeReport
Simple python script to import and parse info from various sources to see who is in CrowdStrike Falcon

## Setup
### Export CSV from ABR
Default filename value: dsp_users_and_machine.csv
Format: `Hostname,AndrewID` (I just manually removed all other columns)
### Export CSV from Crowdstrike
Default Filename value: falconexport.csv
Format: `Hostname,Last_Seen` (Again, I just paired it down to these two columns)
### Export LDAP info for Department
Default Filename value: falconusersandgroups.csv
Format: `AndrewID,Given Name,Department`
### Set Export file
Default Filename value: active_users.csv
This file is your generated output.
