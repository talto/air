#!/usr/bin/python
import os
from time import sleep

##def status_of_O2 (O2_in):

status_now= "_"
i=0
j=2 # 
O2_max=20000 #
O2_now=0 # 
O2_rit=10 #
O2_man=1 # 
num_of_people = 1
status_list = ['fresh air', 'habitable', 'stuffy', 'stagnant', 'difficult to breathe', 'presistent smell of death', 'incompabilite whit life', 'no oxygen in the room']
limits_list = [15000, 12000, 8000, 6000, 4000, 100, 10, 0]
n_limits= 7 # 
status_now = str(status_list[0])
while j>1:
        pass
        Number_of_people = open("Number_of_people.txt") # 
        num_of_people=int(Number_of_people.read());
        K= 10 #ritual cost
        O2 = open("O2.txt") #.
        ritual = open("ritual.txt") #
        status = open("status.txt","w") # 
        #status_now =status.read()
        O2_now = int(O2.read())
        print(status_now,O2_now, j , i)#
        O2.close
        rit_I=ritual.readline() 
        while  rit_I!="": #
                if rit_I=="F" :
                        O2_now = O2_max
                else:
                        O2_now = O2_now-int(rit_I)*O2_man*K
                rit_I=ritual.readline()
        O2_now=O2_now-num_of_people*O2_man #
        status_now=status_list[0]
        ritual.close
        
        for i in range(0,n_limits):
                pass
                if O2_now<limits_list[i]:
                        pass
                        status_now=status_list[i+1]
        print(status_now,O2_now, j , i)
        status_to_write= status_now+" "+str(O2_now)
        status = open("status.txt","w")
        status.write(status_to_write)
        status.close
        
        
        Number_of_people.close
        
        O2 = open("O2.txt","w")
        O2.write(str(O2_now))
        O2.close
        
        ritual = open("ritual.txt","w")
        ritual.write("")
        ritual.close
        

        j=(j-1)
	#sleep(3)
