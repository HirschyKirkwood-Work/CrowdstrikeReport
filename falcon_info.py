#!/usr/bin/env python3

import os

# Initialize dictionaries to store data from file 2 and file 3
class FalconInfo:
    def __init__(self):
        self.andrewID_dict = {}
        self.dsp_data_dict = {}
        self.falcon_data_dict = {}
        self.inactive_machines = {}
        self.self_managed = {}

# Read file 2 and store andrewID and department
    def get_ldapinfo(self,pth:str):
        with open(pth, 'r') as file2:
            for line in file2:

                columns = line.strip().split(',')
                andrewID = columns[0].lower()
                try:
                    department = columns[2]
                    if department == '':
                        department = "No LDAP info"
                        
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

    def get_self_managed(self, pth: str):
        with open(pth, 'r') as file69:
            for line in file69:
                columns = line.strip().split(',')
                falcon_hostname = columns[0]
                falcon_last_seen = columns[1]
                self.self_managed[falcon_hostname] = falcon_last_seen

# Read file 3 and store dsp_hostname and dsp_andrewid
    def get_dspinfo(self, pth: str):
        with open(pth, 'r') as file3:
            for line in file3:
                columns = line.strip().split(',')
                dsp_hostname = columns[0]
                dsp_last_seen = columns[2]
                dsp_andrewid = columns[18].lower()

                # Check if the andrewid is already in the dictionary
                if dsp_hostname not in self.dsp_data_dict:
                    self.dsp_data_dict[dsp_hostname] = {}  # Create a new dictionary if not exists

                # Add or update data for the andrewid
                self.dsp_data_dict[dsp_hostname]["andrewID"] = dsp_andrewid
                self.dsp_data_dict[dsp_hostname]["hostname"] = dsp_hostname
                self.dsp_data_dict[dsp_hostname]["last_seen"] = dsp_last_seen

    def process_info(self, dsp_infopath: str, ldap_infopath: str, falcon_path:str, outpath: str, inactive_out: str, self_managed: str):
        self.get_dspinfo(dsp_infopath)
        self.get_ldapinfo(ldap_infopath)
        self.get_falconinfo(falcon_path)
        self.get_self_managed(self_managed)
        with open(outpath, 'w') as outfile:
            outfile.write("Hostname,AndrewID,Last Seen,Department\n")
        with open(inactive_out, 'w') as inactive:
            inactive.write("Hostname,AndrewID,Department,Last Seen\n")
        with open(outpath, 'a') as outfile:
            with open(inactive_out, "a") as inactive:
                andrew_ids = [value["andrewID"] for value in self.dsp_data_dict.values()]
                for hostname, andrewID in self.dsp_data_dict.items():
                    # Check if dsp_hostname matches hostname and dsp_andrewid is in andrewID_dict
                    if hostname in self.falcon_data_dict and andrewID["andrewID"] in self.andrewID_dict:
                        department = self.andrewID_dict[andrewID['andrewID']].replace('"','')
                        last_seen = self.falcon_data_dict[hostname]
                        outfile.write(f"{hostname},{andrewID['andrewID']},{last_seen[:10]},{department}\n")
                    # Write users with computer who aren't in the right SID in Falcon
                    elif hostname in self.self_managed and andrewID["andrewID"] in self.andrewID_dict:
                        department = self.andrewID_dict[andrewID['andrewID']].replace('"','')
                        last_seen = self.self_managed[hostname]
                        inactive.write(f"{hostname},{andrewID['andrewID']},{last_seen[:10]},{department},They Used the Self-Managed SID\n")
                    # Users who do not show up with their machine in Falcon.
                    elif andrewID['andrewID'] in self.andrewID_dict and hostname:
                        department = self.andrewID_dict[andrewID['andrewID']].replace('"','')
                        inactive.write(f"{hostname},{andrewID['andrewID']},{department},{andrewID['last_seen']}\n")
                    # Users who are signed into a computer w/ Falcon, but don't appear in the Falcon Groupers
                    elif hostname in self.falcon_data_dict.keys() and andrewID['andrewID'] not in self.andrewID_dict.keys():
                        outfile.write(f"{hostname},{andrewID['andrewID']},{last_seen[:10]},Not in Falcon Grouper but still has Falcon installed.\n")
                    # else:# Non-Falcon users
                    #     print(andrewID['andrewID'], hostname)
                # Write users who don't have computers on record w/ DSP
                for andrewID, department in self.andrewID_dict.items():
                    if andrewID not in andrew_ids:
                        inactive.write(f"Not A Customer or no machine on SLA,{andrewID},{department},N/A\n")
                    
if __name__ == '__main__':
    falcon = FalconInfo()
    falcon.process_info("dsp_users_and_machine.csv", "falconusersandgroups.csv", "falconexport.csv", "active_users.csv", "inactive_machines.csv", "self_managed.csv")