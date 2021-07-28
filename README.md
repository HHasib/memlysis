# Automatic memory dump analysis using LiME and Volatility2
A python program to remotely extract RAM into a local computer within the same network and run volatility commands on it.
This is a program written in python3. Upon running this program it will automatically create a memory dump from a remote computer (currently set as 192.168.0.102 using port 4444). The memory dump is in lime format (currently set to be saved as dummy.lime). Then, the volatility commands are run on the memory dump (currently the command is set as ‘imageinfo’ if no argument is passed when run). 

To run the program simply type the following in the terminal:

***python3 memlysis.py***

To run a particular volatility command pass the name after the program name.For example:

***python3 memlysis.py linux_threads***
