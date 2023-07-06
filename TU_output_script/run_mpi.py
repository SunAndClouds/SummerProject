#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:51:29 2023

@author: robertgc
"""

from multiprocessing import Pool
import os 
import subprocess

#Tu exe
tu_exe = '/opt/Transuranus/21.1.1/Release/bin/Transuranus'
tuplot_exe = '/opt/Transuranus/21.1.1/Release/bin/TuPlot'

#Files to clean 
clean_file_list = """
generic_case.mic
generic_case.mac
standard.out 
overview.out
""".split()

#To run one case
def run_case(inp):
    
    #Get the directory
    directory = os.path.dirname(inp)
    
    #Print directory
    print(directory)
    
    #Stout and stderr
    stdout_name = os.path.sep.join((directory,'std_out'))
    stderr_name = os.path.sep.join((directory,'std_err'))

    #Error file 
    error_name = os.path.sep.join((directory,'error.log'))

    #If error file dosent exist
    if not os.path.exists(error_name):
    
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
    
        #Just run tuplot 
        subprocess.call(
            tuplot_exe,
            cwd=directory
            )
    
    #Iterate files to clean 
    for clean_file in clean_file_list:
        
        #Concatenate name and dir for full path 
        path = os.sep.join((directory,clean_file))
        
        #If exists
        if os.path.exists(path):
            
            #Remove 
            os.remove(path)
           
#Function that just iterate folders
def iterate_folder(folder):
    
    #Walk the folder 
    for r,_,fs in os.walk(folder):
        
        #Check files, if input exists 
        if 'input' in fs: 
            
            #Then concatenate the full path 
            path = os.sep.join((r,'input´'))
            
            #Yield back the path
            yield path
        
#Main script 
if __name__ == '__main__':
        
    #Get the inputs
    inps = [inp for inp in iterate_folder('../TU_output')]
     
    #Start a pool
    with Pool() as pool:
        
       #Run the cases
       pool.map(run_case,inps[:10])