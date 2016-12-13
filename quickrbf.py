#!/usr/bin/env python
# writen by Rosdyana Kusuma - rosdyana.kusuma@gmail.com

import sys
import os
from subprocess import *

#clear page
def clear_page():
    is_win32 = (sys.platform == 'win32')
    if(is_win32):
        os.system('cls')
    else:
        os.system('clear')
clear_page()

#banner
def banner(x):
    if(x=='quickrbf'):
        print '''
                          +-+-+-+-+-+-+-+-+
                          |Q|u|i|c|k|R|B|F|
                          +-+-+-+-+-+-+-+-+                                                  
        '''
    if(x=='datatrans'):
        print '''
                         +-+-+-+-+-+-+-+-+-+
                         |D|a|t|a|T|r|a|n|s|
                         +-+-+-+-+-+-+-+-+-+
        '''
    if(x=='centerselect'):
        print '''
                      +-+-+-+-+-+-+-+-+-+-+-+-+
                      |C|e|n|t|e|r|S|e|l|e|c|t|
                      +-+-+-+-+-+-+-+-+-+-+-+-+                                                          
       '''
    if(x=='datascale'):
        print '''
                         +-+-+-+-+-+-+-+-+-+
                         |D|a|t|a|S|c|a|l|e|
                         +-+-+-+-+-+-+-+-+-+
        '''
banner('quickrbf')

#data trans
def rmx_datatrans():
    clear_page()
    banner('datatrans')
    datatrans_exe = r"datatrans.exe"
    assert os.path.exists(datatrans_exe), "data trans executable is not found"
    print '''
    Datatrans in QuickRBF package to help you to convert the data file to the our format. 
    You can use "Microsoft Excel" or other software to edit your data file,
    then save the data file to *.csv file, which use the "," to separate the feature values. 
    In addition, the last value is the class feature value. 
    '''
    datatrans_file = raw_input("Input data file : ")
    if os.path.isfile(datatrans_file) and os.access(datatrans_file, os.R_OK):
        #logic for datatrans method
        cmd = '{0} "{1}"'.format(datatrans_exe,datatrans_file)
        Popen(cmd, shell = True, stdout = PIPE).communicate()
        print('Output from datatrans: {0}.out'.format(datatrans_file))
    else:
        print "file not found"
    sys.exit()

#data scale
def rmx_datascale():
    clear_page()
    banner('datascale')
    datascale_exe = r"datascale.exe"
    assert os.path.exists(datascale_exe), "data scale executable is not found"
    print ''' 
    Scaling your data properly is very important in data classification experiments. 
    So we also offer datascale program in our package to help you to scale your data. 
    The default range is from -1 to 1, and you may edit the source file to change the setting.
    '''
    datascale_file = raw_input("Input data file : ")
    if os.path.isfile(datascale_file) and os.access(datascale_file, os.R_OK):
        #logic for datascale method
        cmd = '{0} "{1}"'.format(datascale_exe, datascale_file)
        Popen(cmd, shell = True, stdout = PIPE).communicate()
        print('Output for data scale: {0}.scale'.format(datascale_file))
    else:
        print "file not found"
    sys.exit()

#center select
def rmx_centerselect():
    clear_page()
    banner('centerselect')
    centerselect_exe = r"centerselect.exe"
    assert os.path.exists(centerselect_exe), "center select executable is not found"
    print '''
    How to select good centers for RBFN is still a hot research issue. 
    In this package, we only offer a simple tool, centerselect, to select the centers from training instances randomly. 
    We will try to find a better approach in the future. However, if your training data is not large (less than 10,000), you may consider to use the all training instances as centers.
    '''
    centerselect_file = raw_input("Input training data file : ")
    num_of_center = raw_input("Number of center : ")
    if os.path.isfile(centerselect_file) and os.access(centerselect_file, os.R_OK):
        f =  open(centerselect_file, "r")
        #logic for center select
        cmd = '{0} "{1}" {2}'.format(centerselect_exe, centerselect_file, num_of_center)
        Popen(cmd, shell = True, stdout = PIPE).communicate()
        print('output for center select: {0}.{1}'.format(centerselect_file,num_of_center))
    else:
        print "file not found"
    sys.exit()

#quicrbf
def rmx_quickrbf():
    clear_page()
    banner('quickrbf')
    quickrbf_exe = r"quickrbf.exe"
    assert os.path.exists(quickrbf_exe), "quickrbf executable is not found"
    print '''
    The QuickRBF package is a simple, easy-to-use, and efficient software package for Radial Basis Function Networks (RBFN). 
    Also, the QuickRBF package use an efficient least mean square error method for constructing RBFN classifier based on the Cholesky decomposition.
    '''
    file_center = raw_input("Input center file : ")
    file_train = raw_input("Input training file : ") 
    file_test = raw_input("Input test file : ")
    output = raw_input("input name for result :")
    if os.path.isfile(file_train) and os.access(file_train, os.R_OK) and \
    os.path.isfile(file_center) and os.access(file_center, os.R_OK) and \
    os.path.isfile(file_test) and os.access(file_test, os.R_OK) :
        #logic for quickrbf method
        cmd = 'quickrbf "{0}" "{1}" "{2}" > "{3}"_result.txt'.format(file_center, file_train, file_test, output)
        Popen(cmd, shell = True, stdout = PIPE).communicate()
        print('QuickRBF result in "{0}"_result.txt'.format(output))
    else:
        print "file not found"
    sys.exit()

#Menu
def Menu():
    print " QUICK RBF with python "
    print " [1] QuickRBF \n [2] Data Trans \n [3] Data Scale \n [4] Center Select"
    while True:
        try:
            choice = int(raw_input("Select method : "))
        except ValueError:
            print "only accept number"
        else:
            if (choice == 1):
                rmx_quickrbf()
            if (choice == 2):
                rmx_datatrans()
            if (choice == 3):
                rmx_datascale()
            if  (choice == 4):
                rmx_centerselect()
            else:
                clear_page()
                banner('quickrbf')
                Menu()            
    sys.exit()
Menu()


        
