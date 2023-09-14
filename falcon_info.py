#!/usr/bin/env python3

import os

# Initialize dictionaries to store data from file 2 and file 3
class FalconInfo:
    def __init__(self):
        self.andrewID_dict = {}
        self.dsp_data_dict = {}

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

# Read file 3 and store dsp_hostname and dsp_andrewid
    def get_dspinfo(self, pth: str):
        with open(pth, 'r') as file3:
            for line in file3:
                columns = line.strip().split(',')
                dsp_hostname = columns[0]
                dsp_andrewid = columns[1]
                self.dsp_data_dict[dsp_hostname] = dsp_andrewid

    def process_info(self, dsp_infopath: str, ldap_infopath: str, falcon_path:str, outpath: str):
        self.get_dspinfo(dsp_infopath)
        self.get_ldapinfo(ldap_infopath)
        with open(outpath, 'w') as outfile:
            outfile.write("Hostname,AndrewID,Last Seen,Department\n")

        with open(outpath, 'a') as outfile:
            # Read file 1 and append the desired information to outpath
            with open(falcon_path, 'r') as file1:
                for line in file1:
                    columns = line.strip().split(',')
                    hostname = columns[0]
                    last_seen = columns[1]

                    # Check if dsp_hostname matches hostname and dsp_andrewid is in andrewID_dict
                    if hostname in self.dsp_data_dict and self.dsp_data_dict[hostname] in self.andrewID_dict:
                    # if hostname inself.dsp_data_dict and falcon_user in andrewID_dict:
                        # print(hostname, falcon_user, andrewID_dict[falcon_user])
                        andrewID = self.dsp_data_dict[hostname]
                        department = self.andrewID_dict[andrewID].replace('"','')
                        outfile.write(f"{hostname},{andrewID},{last_seen},{department}\n")
                    
if __name__ == '__main__':
    falcon = FalconInfo()
    falcon.process_info("dsp_users_and_machine.csv", "falconusersandgroups.csv", "falconexport.csv", "active_users.csv")