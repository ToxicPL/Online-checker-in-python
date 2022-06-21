import os
import pandas as pd
import openpyxl

# --- This version is checking IP from the txt file and save in txt file
with open("ip.txt", "r+") as ips_file:
    ips = [ip.strip() for ip in ips_file.readlines()]

with open("IPsCheck.txt", "w") as available_ips_file:
    for ip in ips:
        response = os.system('ping {} -n 2 -w 2'.format(ip))
        if response == 0:
            available_ips_file.write(ip + "\n")
            # TODO: It's for test delete this
            df = pd.DataFrame([ip], index=[None], columns=['IP Address'])
            df.to_excel('pandas_to_excel.xlsx', sheet_name='Online IP Address')
        else:
            with open("offline_ip.txt", "w") as offline_ip:
                offline_ip.write(ip + "\n")

# This version is checking IP from the excel file and save it to another sheet in this file


