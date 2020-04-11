#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 14:46:54 2020

@author: deba10106
"""

import os, glob,PyPDF2
import shutil
path1=os.getcwd()
print("by default it will work on "+ path1+". Press ENTER for default path.")
path2=input("Put a directory path (relative to the default) for anything else: ")
path=path1+"/"+path2

my_dir=glob.glob(path+"/*")
if os.path.isdir(path):
    
#print(my_dir)
#for elem in my_dir:
#    e=elem.strip().split(".",-1)
#    print(elem)
#    if e[len(e)-1]=="pdf":
#        shutil.move(elem, "/home/omaxxx/Downloads/PDFs/")
    for elem in my_dir:
        if os.path.isdir(elem):
            print("it's a folder! Cannot be moved")
        else:
            e=elem.strip().split(".",-1)
            
            if e[len(e)-1]=="pdf":
                
                with open(elem,"rb") as f:
                    try:
                        pdfReader = PyPDF2.PdfFileReader(f)
                        #print(pdfReader.numPages)
                        pageObj = pdfReader.getPage(0)
                        if pageObj.extractText().strip().split(":",-1)[0]=='arXiv':
                            try:
                                os.mkdir(path+"/arXiv/")
                            except:  
                                print("Folder arXiv already exists")   
                            shutil.move(elem,path+"/arXiv/")
                            print(elem.split("/",-1)[-1] + " is being moved to" + path+"arXiv/")
                            
                        else:
                            try:
                                os.mkdir(path+"/PDFs/")
                            except:  
                                print("Folder PDFs already exists!")   
                            shutil.move(elem,path+"/PDFs/")
                            print(elem.split("/",-1)[-1] + " is being moved to" + path+"PDFs/")
                    except:
                        print(elem.strip().split("/",-1)[-1]+" can not be opened or is password protected")
            else:
                try:
                    try:
                        os.mkdir(path+"/Documents/")
                    except:
                        print("Folder Documents already exists!")
                        if elem.split("/",-1)[-1]!="myapp.py":
                            shutil.move(elem,path+"/Documents/")
                            print(elem.split("/",-1)[-1] + " is being moved to" + path+"Documents/")
                except:
                    print("File already exist!")
                    #os.remove(elem)
else:
    print("Path does not exist!")
                    

    
    