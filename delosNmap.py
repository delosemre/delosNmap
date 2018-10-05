#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################
#                        #
#Emre Yılmaz (delosemre) #
# 	  kernelblog.org     #
##########################

import sys
import os
import time
import signal
from time import sleep
from sys import argv
from platform import system


def sigint_handler(signum, frame):
    os.system("clear")
    print ("CTRL+C detected!")
    print(" \033[1;91m@Good bye\033[1;m")
    sys.exit() 
 
signal.signal(signal.SIGINT, sigint_handler)

def logo():
    print ("""\033[1;91m

                           )
  (         (           ( /(
  )\ )   (  )\          )\())    )       )
 (()/(  ))\((_) (   (  ((_)\    (     ( /(  `  )
  ((_))/((_)_   )\  )\  _((_)   )\  ' )(_)) /(/(
  _| |(_)) | | ((_)((_)| \| | _((_)) ((_)_ ((_)_)
/ _` |/ -_)| |/ _ \(_-<| .` || '  \()/ _` || '_ \)
\__,_|\___||_|\___//__/|_|\_||_|_|_| \__,_|| .__/
  Emre Yılmaz (delosemre) - KernelBlog.org |_| v1
\033[1;m
    """)


def menu():
    logo()
    print("""
        Menu
        1-) Default Scan
        2-) Host Discovery
        3-) Port(SYN) Scan
        4-) Port(TCP) Scan
        5-) Port(UDP) Scan
        """)
    

def baslangic():
    logo()
    menu()
    print("   Enter one of the options.")

    secim = raw_input("root""\033[1;91m@KernelBlog:~$\033[1;m ")

    if secim == "1":
        print(" Starting Default Scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        birhedef = raw_input("     Enter Your Destination: ")
        os.system("nmap "+birhedef+" -oN "+birhedef)
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimbir = raw_input("root""\033[1;91m@KernelBlog:~$\033[1;m ")
        if secimbir == "1":
            baslangic()
        if secimbir == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    if secim == "2":
        print(" Starting Host Discovery...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        ikihedef = raw_input("     Enter Your Destination: ")
        os.system("nmap -Pn "+ikihedef+" -oN "+ikihedef)
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimiki = raw_input("root""\033[1;91m@KernelBlog:~$\033[1;m ")
        if secimiki == "1":
            baslangic()
        if secimiki == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()
    
    if secim=="3":
        print(" Starting Port(SYN) Scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        uchedef = raw_input("     Enter Your Destination: ")
        os.system("nmap -sS "+uchedef+" -oN "+uchedef)
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimuc = raw_input("root""\033[1;91m@KernelBlog:~$\033[1;m ")
        if secimuc == "1":
            baslangic()
        if secimuc == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()
    
    if secim=="4":
        print(" Starting Port(TCP) Scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        dorthedef = raw_input("     Enter Your Destination: ")
        os.system("nmap –sT "+dorthedef+" -oN "+dorthedef)
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimdort = raw_input("root""\033[1;91m@KernelBlog:~$\033[1;m ")
        if secimdort == "1":
            baslangic()
        if secimdort == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()
    
    if secim=="5":
        print(" Starting Port(UDP) Scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        beshedef = raw_input("     Enter Your Destination: ")
        os.system("nmap –sU "+beshedef+" -oN "+beshedef)
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        besdort = raw_input("root""\033[1;91m@KernelBlog:~$\033[1;m ")
        if secimbes == "1":
            baslangic()
        if secimbes == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    else:
        print(" Please enter one of the options in the menu.")
        time.sleep(1)
        baslangic()
    

baslangic()