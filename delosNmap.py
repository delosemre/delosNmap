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
  Emre Yılmaz (delosemre) - KernelBlog.org |_| v1.5
\033[1;m """)


def menu():
    logo()
    print("""
        1-) Default Scan
        2-) Host Discovery
        3-) Port(SYN) Scan
        4-) Port(TCP) Scan
        5-) Port(UDP) Scan
        6-) Port Definition (-sS -F)
        7-) Service and Version Discovery
        8-) OS Analysis and Version Discovery
        9-) Nmap Script Engineering
        \033[1;91m Firewall and IDS bypass \033[1;m
        10-) Spoof Mac (-spoof-mac 'cisco')
        11-) MTU
        \033[1;91m Mixed \033[1;m
        12-) together (-sS -sV -Pn -p-)
        0-) Exit
        """)
    

def baslangic():
    menu()
    print("   Enter one of the options.")

    secim = input("root""\033[1;91m@KernelBlog:~$\033[1;m ")

    if secim == "1":
        print(" Starting Default Scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        birhedef = input("     Enter Your Destination: ")
        os.system("nmap "+birhedef+" -oN "+birhedef)
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimbir = input("root""\033[1;91m@KernelBlog:~$\033[1;m ")
        if secimbir == "1":
            baslangic()
        if secimbir == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    if secim =="2":
        print(" Starting Host Discovery...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        ikihedef = input("     Enter Your Destination: ")
        os.system("nmap -Pn "+ikihedef+" -oN "+ikihedef)
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimiki = input("root""\033[1;91m@KernelBlog:~$\033[1;m ")
        if secimiki == "1":
            baslangic()
        if secimiki == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()
    
    if secim== "3":
        print(" Starting Port(SYN) Scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        uchedef = input("     Enter Your Destination: ")
        os.system("nmap -sS "+uchedef+" -oN "+uchedef)
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimuc = input("root""\033[1;91m@KernelBlog:~$\033[1;m ")
        if secimuc == "1":
            baslangic()
        if secimuc == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()
    
    if secim== "4":
        print(" Starting Port(TCP) Scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        dorthedef = input("     Enter Your Destination: ")
        os.system("nmap –sT "+dorthedef+" -oN "+dorthedef)
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimdort = input("root""\033[1;91m@KernelBlog:~$\033[1;m ")
        if secimdort == "1":
            baslangic()
        if secimdort == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()
    
    if secim== "5":
        print(" Starting Port(UDP) Scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        beshedef = input("     Enter Your Destination: ")
        os.system("nmap –sU "+beshedef+" -oN "+beshedef+".txt")
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimbes = input("root""\033[1;91m@KernelBlog:~$\033[1;m ")
        if secimbes == "1":
            baslangic()
        if secimbes == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()


    if secim=="6":
        print(" Starting Port Definition (-sS -F)...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        altihedef = input("     Enter Your Destination: ")
        os.system("nmap -sS -F "+altihedef+" -oN "+altihedef+".txt")
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimalti = input("root""\033[1;91m@KernelBlog:~$\033[1;m ")
        if secimalti == "1":
            baslangic()
        if secimalti == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()


    
    if secim=="7":
        print(" Starting Service and Version Discovery...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        yedihedef = input("     Enter Your Destination: ")
        os.system("nmap –sS -F "+yedihedef+" -oN "+yedihedef+".txt")
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimyedi = input("root""\033[1;91m@KernelBlog:~$\033[1;m ")
        if secimyedi == "1":
            baslangic()
        if secimyedi == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()



    if secim=="8":
        print(" Starting OS Analysis and Version Discovery...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        sekizhedef = input("     Enter Your Destination: ")
        os.system("nmap –sS -O "+sekizhedef+" -oN "+sekizhedef+".txt")
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimsekiz = input("root""\033[1;91m@KernelBlog:~$\033[1;m ")
        if secimsekiz == "1":
            baslangic()
        if secimsekiz == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()


    if secim=="9":
        print(" Starting Nmap Script Engineering...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        dokuzhedef = input("     Enter Your Destination: ")
        os.system("nmap –sC "+dokuzhedef+" -oN "+dokuzhedef+".txt")
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimdokuz = input("root""\033[1;91m@KernelBlog:~$\033[1;m ")
        if secimdokuz == "1":
            baslangic()
        if secimdokuz == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    if secim=="10":
        print("Starting -spoof-mac 'cisco' ")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        onhedef = input("     Enter Your Destination: ")
        os.system("nmap -spoof-mac 'cisco' "+onhedef+" -oN "+onhedef+".txt")
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimon = input("root""\033[1;91m@KernelBlog:~$\033[1;m ")
        if secimon == "1":
            baslangic()
        if secimon == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    if secim=="11":
        print("Starting MTU ")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        onbirhedef = input("     Enter Your Destination: ")
        print("Enter the MTU value. Data payload MTU must be >0 and multiple of 8")
        mtudeger=input("MTU Value:")
        os.system("nmap --mtu "+mtudeger+" "+onbirhedef+" -oN "+onbirhedef+".txt")
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimonbir= input("root""\033[1;91m@KernelBlog:~$\033[1;m ")
        if secimonbir == "1":
            baslangic()
        if secimonbir == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    if secim=="12":
        print("Starting together (-sS -sV -Pn -p-) ")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        onikihedef = input("     Enter Your Destination: ")
        os.system("nmap -sS -sV -Pn -p- "+onikihedef+" -oN "+onikihedef+".txt")
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimoniki = input("root""\033[1;91m@KernelBlog:~$\033[1;m ")
        if secimoniki == "1":
            baslangic()
        if secimoniki == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()


    if secim=="0":
        print(" \033[1;91m@Good bye\033[1;m")
        sys.exit()

    else:
        print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
        time.sleep(2)
        baslangic()




def rootkontrol():
    if os.geteuid()==0:
        baslangic()
    else:
        print ("Please run it with root access.")
        sys.exit()

rootkontrol()