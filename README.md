# memlysis
A python program to remotely extract RAM into a local computer within the same network and run volatility commands on it.
This is a program written in python3. Upon running this program it will automatically create a memory dump from a remote computer (currently set as 192.168.0.102 using port 4444). The memory dump is in lime format (currently set to be saved as dummy.lime). Then, the volatility commands are run on the memory dump (currently the command is set as ‘imageinfo’).

To run the program simply type the following in the terminal:

python3 auto_mem_analysis.py

