# in the 'users' file we have the IP address and whenever we want to block a
# website we have to redirect the site to the IP address

import time
from datetime import datetime as dt

fhand = 'C:/Windows/System32/drivers/etc/hosts'
fhand_temp = r'./hosts' #passing a real string
redirect = '127.0.0.1' #IP address

websites = ['www.facebook.com','facebook.com']

#Infinit Loop
while True:
    file = open(fhand, 'r+')
    content = file.read()
    file.seek(0)
    content_ = file.readlines()
    hr = dt.now().hour
    if 8 <= hr and hr <= 16 :   #blocking between 8AM to 4PM
        for item in websites :
            if item in content :
                continue
            else :
                file.write('{}       {}\n'.format(redirect, item))
        print("working hours ...........")
    else :
        file.seek(0)
        for line in content_ :
            for website in websites :
                if website not in line:
                    condition = True
                else :
                    condition = False
            if condition == True :
                file.write(line)
        file.truncate()
        print('Relax time ............')
    time.sleep(5)
