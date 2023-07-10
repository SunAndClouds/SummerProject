#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 22:34:22 2023

@author: robertgc
"""

import os
import shutil

#Input folder
inp_folder = '../input'

#output folder
out_folder = '../TU_output'

#input header
head_file = '../templates/PWR_head_new'

#tuplot file
tuplot_file = '../templates/TuPlot.inp'

#Walk the input tree
for r,_,fs in os.walk(inp_folder):
    
    #Go through files
    for f in fs:
        
        #If we have a txt file
        if f.endswith('txt'):
            
            #Ph path
            ph_path = os.sep.join((r,f))
            
            #get the run path from the ph path
            run_path = os.sep.join(
                out_folder.split(os.sep) + 
                ph_path.replace('.txt','')
                .split(os.sep)[len(inp_folder.split(os.sep)):]
                )


            print(ph_path)
            
            #Make run path
            os.makedirs(run_path,exist_ok=True)
            
            #Input file name
            input_file = os.sep.join((run_path,'input'))
            
            #Tuplot file 
            tuplot_file_dst = os.sep.join((run_path,'TuPlot.inp'))
            
            #Copy tuplot file if exists
            if os.path.exists(tuplot_file):
                shutil.copy(
                    tuplot_file,
                    tuplot_file_dst
                    )
            
            #Open head, ph_file and input file
            with (
                    #Head file
                    open(head_file,'r') as head,
                    #ph file
                    open(ph_path,'r') as ph,
                    #input file
                    open(input_file,'w') as inp
                    ):
                
                #Write header lines 
                for l in head: 
                    inp.write(l)
                    
                #Write ph_lines
                for l in ph:
                    inp.write(l)
                
                print(f)
