#take a filename as input argument and save it as that in a particular directory
#also take volatility commands as arguments which is optional
#e.g. python3 automation_1.py test(name of lime file: test.lime) locationof vol.py 

import time
import os
import multiprocessing
import paramiko
import sys

filename = 'dummy'
vol_command = 'imageinfo'
if (len(sys.argv)>2):
    filename = sys.argv[1]
    vol_command = sys.arg[2]
else if (len(sys.argv)>1):
    filename = sys.argv[1]   
else:
    pass
    
    
        
def save_file():
##    print('listening to save...')
    command = 'nc 192.168.0.102 4444 > %s.lime' %(filename)
    os.system(command)
##    print('Saved')

def remote_commands(command):
##    print("Connecting...")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('192.168.0.102',username='root',password='root') #change it to whatever the ip and usernam and password is
    stdin, stdout, stderr = client.exec_command(command)
    client.close()
##    print("Connection finished.")

def connect(): #this creates the lime file ready to be sent through port 4444
    remote_commands('insmod ./lime.ko \"path=tcp:4444 format=lime\"') #lime is installed in the root directory in this case
    
def remove_lime_mod(): # this removes the lime module from system kernel
    remote_commands('rmmod lime')
    
def volatility_commands(): #this runs memory analysis using volatility on the memo
    location_to_volatility = '/Users/DummyUser/Programs/volatility/'      #change the variable to wherever vol.py is installed
    command = 'python %svol.py -f %s.lime %s'%(location_to_volatility, filename, vol_command) 
    os.system(command)
    

p1 = multiprocessing.Process(target=connect)
p2 = multiprocessing.Process(target=save_file)

if __name__ == "__main__":
    print('Program started..')
    p1.start()
    time.sleep(10)
    p2.start()
    p1.join()
    p2.join()
    print('Memory dump successfully downloaded.')
    remove_lime_mod() #removes the lime module from kernel
    print('Executing volatility commands on memory dump..')
    volatility_commands()

finish =time.perf_counter()
print('\nProgram Finished.\nTotal Time for completion:'+str(finish))
