#!/usr/bin/env python3

import os

# Initialize dictionaries to store data from file 2 and file 3
class FalconInfo:
    def __init__(self):
        self.andrewID_dict = {}
        self.dsp_data_dict = {}
        self.falcon_data_dict = {}
        self.inactive_machines = {}

# Read file 2 and store andrewID and department
    def get_ldapinfo(self,pth:str):
        with open(pth, 'r') as file2:
            for line in file2:
                columns = line.strip().split(',')
                andrewID = columns[0]
                try:
                    department = columns[2]
                except:
                    department = "No LDAP info"
                self.andrewID_dict[andrewID] = department

    def get_falconinfo(self, pth: str):
        with open(pth, 'r') as file4:
            for line in file4:
                columns = line.strip().split(',')
                falcon_hostname = columns[0]
                falcon_last_seen = columns[1]
                self.falcon_data_dict[falcon_hostname] = falcon_last_seen

# Read file 3 and store dsp_hostname and dsp_andrewid
    def get_dspinfo(self, pth: str):
        with open(pth, 'r') as file3:
            for line in file3:
                columns = line.strip().split(',')
                dsp_hostname = columns[0]
                dsp_andrewid = columns[1]
                self.dsp_data_dict[dsp_hostname] = dsp_andrewid

    def process_info(self, dsp_infopath: str, ldap_infopath: str, falcon_path:str, outpath: str, inactive_out: str):
        self.get_dspinfo(dsp_infopath)
        self.get_ldapinfo(ldap_infopath)
        self.get_falconinfo(falcon_path)
        with open(outpath, 'w') as outfile:
            outfile.write("Hostname,AndrewID,Last Seen,Department\n")
        with open(inactive_out, 'w') as inactive:
            inactive.write("Hostname,AndrewID,Department\n")
        with open(outpath, 'a') as outfile:
            with open(inactive_out, "a") as inactive:
                for hostname, andrewID in self.dsp_data_dict.items():
                    # Check if dsp_hostname matches hostname and dsp_andrewid is in andrewID_dict
                    if hostname in self.falcon_data_dict and andrewID in self.andrewID_dict:
                        department = self.andrewID_dict[andrewID].replace('"','')
                        last_seen = self.falcon_data_dict[hostname]
                        outfile.write(f"{hostname},{andrewID},{last_seen[:10]},{department}\n")
                    # Write users with computer who aren't in Falcon
                    elif andrewID in self.andrewID_dict and hostname:
                        department = self.andrewID_dict[andrewID].replace('"','')
                        inactive.write(f"{hostname},{andrewID},{department}\n")
                    # Write users who don't have computers on record w/ DSP
                for andrewID, department in self.andrewID_dict.items():
                    if andrewID not in self.dsp_data_dict.values():
                        inactive.write(f"{andrewID},{department},Not A Customer or no machine on SLA\n")
                    
if __name__ == '__main__':
    falcon = FalconInfo()
    falcon.process_info("dsp_users_and_machine.csv", "falconusersandgroups.csv", "falconexport.csv", "active_users.csv", "inactive_machines.csv")