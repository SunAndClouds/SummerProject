#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:51:29 2023

@author: robertgc
"""

from multiprocessing import Pool
import os 
import subprocess
from glob import glob

#Tu exe
tu_exe = '/opt/Transuranus/21.1.1/Release/bin/Transuranus'
tuplot_exe = '/opt/Transuranus/21.1.1/Release/bin/TuPlot'

#To run one case
def run_case(inp):
    
    #Get the directory
    directory = os.path.dirname(inp)
    
    #Print directory
    print(directory)
    
    #Stout and stderr
    stdout_name = os.path.sep.join((directory,'std_out'))
    stderr_name = os.path.sep.join((directory,'std_err'))
    
    #Open stdout and stderr
    with (
            open(stdout_name,'w') as stdout, 
            open(stderr_name,'w') as stderr
            ):
        
        #Run transuranus 
        subprocess.call(
            tu_exe,cwd=directory,
            stderr=stderr,
            stdout=stdout
            )

    subprocess.call(
        tuplot_exe,
        cwd=directory
        )
        
        #Note here that no cleaning occurs
        
#Main script 
if __name__ == '__main__':
   
    
    #Input files
    inps = glob('*/input')
    

        
    with Pool() as pool:
        
        pool.map(run_case,inps[:10])
