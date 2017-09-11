# Tool 	        	: DirTraversal_Detector
# Author		: Mayendran Govender
# Date Created          : 13 November 2015
# Description		: This tool scans through your webserver log to detect directory Traversal attempts  
# Usage                 : python DirTraversal_Detector.py

###########Important Notice - Please test this Tool in a test platorm and understand how this tool works before using in a production platform. 
###########
#Directory Traversal 
# What is Directory Traversal - Directory traversal is an HTTP exploit which allows attackers to access restricted directories and execute commands outside of the web server's root directory. 

###########Modules Loaded
import platform		                # Loading the list of  Modules
import os
import subprocess
import sys
import datetime
import time

#########Core Detection Module
with open("DirTraversal_Attacks.log","a+") as stdout: # The DirTraversal_Attacks.log file is the output file that will contain directory traversal attempts if there any detected.
   subprocess.Popen('cat access.log | grep "/../../"' ,  shell=True, stdout=stdout, stderr=stdout) # change access.log to your web server log file name (e.g. access_log or httpd.log)

########Date Timestamp
import datetime 
f=open("DirTraversal_Attacks.log",'a')
f.write ("Directory Traversal Attacks detected on"+'\t') # Appending in DirTraversal_Attacks.log  "Directory traversal attacks detected with current date and time stamp
f.write ('\n')
f.write(datetime.datetime.now().ctime())

