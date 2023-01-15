#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################
#                        #
#Emre Yılmaz (delosemre) #
# 	   emreylmz.com      #
# 	  kernelblog.org     #
##########################

import sys
import os
import time
import signal
from time import sleep
from sys import argv
from platform import system

defaultportscan="50";

def anamenu():
        print("\n \033[1;91m your output file is in your current directory \033[1;m")
        os.system("pwd")
        print(" \033[1;91m Your current directory \033[1;m")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        secimdonus = input("root""\033[1;91m@KernelBlog:~$\033[1;m ")
        if secimdonus == "1":
            baslangic()
        if secimdonus == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

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
  Emre Yılmaz (delosemre) - emreylmz.com |_| v2.5
\033[1;m """)


def menu():
    logo()
    print("""
        \033[1;91m Default Scan Types \033[1;m
        1-) Default Scan
        2-) Host Discovery
        3-) Port(SYN) Scan
        4-) Port(TCP) Scan
        5-) Port(UDP) Scan
        6-) Null scan (-sN)
        7-) FIN scan (-sF)
        8-) OS Analysis and Version Discovery
        9-) Nmap Script Engineering (default)
        \033[1;91m Firewall Bypass \033[1;m
        10-) Script Bypass (--script=firewall-bypass)
        11-) Data Length (--data-length <number> )
        12-) Smash (-ff)
        \033[1;91m Vulnerability Scanning \033[1;m
        13-) Default Vuln Scan (--script vuln)
        14-) FTP Vuln Scan
        15-) SMB Vuln Scan
        16-) HTTP Vuln Scan
        17-) SQL Injection Vuln Scan
        18-) Stored XSS Vuln Scan
        19-) Dom Based XSS vuln Scan
        \033[1;91m Subdomain Scanning \033[1;m
        20-) DNS Brute-force Hostnames
        21-) Subdomain/hostmap-crtsh
        \033[1;91m Other \033[1;m
        22-) Whois

        00-) Contact
        0-) Exit
        """)
    

def baslangic():
    menu()
    print("   Enter one of the options.")

    secim = input("root""\033[1;91m@emreylmzcom:~$\033[1;m ")

    if secim == "1":
        print(" Starting Default Scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        birhedef = input("     Enter Your Destination: ")
        if not birhedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport1=input("Top Port? Example: 10 or 50, Default 50:  ")
            if not topport1:
                os.system("nmap -vv --top-ports="+defaultportscan+" "+birhedef+" -oN "+birhedef)
            else:
                os.system("nmap -vv --top-ports="+topport1+" "+birhedef+" -oN "+birhedef)
            
        anamenu()

    if secim =="2":
        print(" Starting Host Discovery...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        ikihedef = input("     Enter Your Destination: ")
        if not ikihedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport2=input("Top Port? Example: 10 or 50, Default 50:  ")
            if not topport2:
                os.system("nmap -vv -Pn --top-ports="+defaultportscan+" "+ikihedef+" -oN HostD-"+ikihedef+"-output")
            else:
                os.system("nmap -vv -Pn --top-ports="+topport2+" "+ikihedef+" -oN HostD-"+ikihedef+"-output")
            
        anamenu()
    
    if secim== "3":
        print(" Starting Port(SYN) Scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        uchedef = input("     Enter Your Destination: ")
        if not uchedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport3=input("Top Port? Example: 10 or 50, Default 50:  ")
            if not topport3:
                os.system("nmap -vv -sS --top-ports="+defaultportscan+" "+uchedef+" -oN "+uchedef+"-output")
            else:
                os.system("nmap -vv -sS --top-ports="+topport3+" "+uchedef+" -oN "+uchedef+"-output")

        anamenu()
    
    if secim== "4":
        print(" Starting Port(TCP) Scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        dorthedef = input("     Enter Your Destination: ")
        if not dorthedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport4=input("Top Port? Example: 10 or 50, Default 50:  ")
            if not topport4:
                os.system("nmap -vv –sT --top-ports="+defaultportscan+" "+dorthedef+" -oN TcpScan-"+dorthedef+"-output")
            else:
                os.system("nmap -vv –sT --top-ports="+topport4+" "+dorthedef+" -oN TcpScan-"+dorthedef+"-output")

        anamenu()
    
    if secim== "5":
        print(" Starting Port(UDP) Scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        beshedef = input("     Enter Your Destination: ")
        if not beshedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport5=input("Top Port? Example: 10 or 50, Default 50:  ")
            if not topport5:
                os.system("nmap -vv –sU --top-ports="+defaultportscan+" "+beshedef+" -oN UdpScan-"+beshedef+"-output")
            else:
                os.system("nmap -vv –sU --top-ports="+topport5+" "+beshedef+" -oN UdpScan-"+beshedef+"-output")
            
        anamenu()


    if secim=="6":
        print(" Null scan (-sN)")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        altihedef = input("     Enter Your Destination: ")
        if not altihedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport6=input("Top Port? Example: 10 or 50, Default 50:  ")
            if not topport6:
                os.system("nmap -vv -sN --top-ports="+defaultportscan+" "+altihedef+" -oN NullScan-"+altihedef+"-output")
            else:
                os.system("nmap -vv -sN --top-ports="+topport6+" "+altihedef+" -oN NullScan-"+altihedef+"-output")

        anamenu()


    
    if secim=="7":
        print(" FIN scan (-sF)")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        yedihedef = input("     Enter Your Destination: ")
        if not yedihedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport7=input("Top Port? Example: 10 or 50, Default 50:  ")
            if not topport7:
                os.system("nmap -vv -sF --top-ports="+defaultportscan+" "+yedihedef+" -oN FinScan-"+yedihedef+"-output")
            else:
                os.system("nmap -vv -sF --top-ports="+topport7+" "+yedihedef+" -oN FinScan-"+yedihedef+"-output")

        anamenu()



    if secim=="8":
        print(" Starting OS Analysis and Version Discovery...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        sekizhedef = input("     Enter Your Destination: ")
        if not sekizhedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport8=input("Top Port? Example: 10 or 50, Default 50:  ")
            if not topport8:
                os.system("nmap –sS -sV -O --top-ports="+defaultportscan+" "+sekizhedef+" -oN Os-Version-"+sekizhedef+"output")
            else:
                os.system("nmap –sS -sV -O --top-ports="+topport8+" "+sekizhedef+" -oN Os-Version-"+sekizhedef+"output")
        
        anamenu()


    if secim=="9":
        print(" Starting Nmap Script Engineering...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        dokuzhedef = input("     Enter Your Destination: ")
        if not dokuzhedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport9= input("Top Port? Example: 10 or 50, Default 50:  ")
            if not topport9:
                os.system("nmap -vv --script=default --top-ports="+defaultportscan+" " +dokuzhedef+" -oN ScScan-"+dokuzhedef+"-output")
            else:
                os.system("nmap -vv --script=default --top-ports="+topport9+" " +dokuzhedef+" -oN ScScan-"+dokuzhedef+"-output")
            
        anamenu()

#firewall bypass
    if secim=="10":
        print("Starting Nmap Scripting Firewall Bypass ")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        onhedef = input("     Enter Your Destination: ")
        if not onhedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport10= input("Top Port? Example: 10 or 50, Default 50:  ")
            if not topport10:
                os.system("nmap -vv --script=firewall-bypass --top-ports="+defaultportscan+" " +onhedef+" -oN "+"firewallbaypass-"+onhedef+"-output")
            else :
                os.system("nmap -vv --script=firewall-bypass --top-ports="+topport10+" " +onhedef+" -oN "+"firewallbaypass-"+onhedef+"-output")

        anamenu()

    if secim=="11":
        print("Starting Data Length ")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        onbirhedef = input("     Enter Your Destination: ")
        if not onbirhedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport11= input("Top Port? Example 10 or 50, Default 50:  ")
            print("Append random data to sent packets")
            datalength=input("Number:")
            if not topport11:
                os.system("nmap --data-string "+datalength+" --top-ports="+defaultportscan+" "+onbirhedef+" -oN datalength-"+onbirhedef+"-output")
            else:
                os.system("nmap ---data-string +"+datalength+" --top-ports="+topport11+" "+onbirhedef+" -oN datalength-"+onbirhedef+"output")
            
        anamenu()

    if secim=="12":
        print("Smash (-ff) ")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        onikihedef = input("     Enter Your Destination: ")
        if not onikihedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport12= input("Top Port? Example 10 or 50, Default 50:  ")
            if not topport12:
                os.system("nmap -vv -ff --top-ports="+defaultportscan+" " +onikihedef+" -oN "+"ff-"+onikihedef+"-output" )
            else:
                os.system("nmap -vv -ff --top-ports="+topport12+" " +onikihedef+" -oN "+"ff-"+onikihedef+"-output" )

        anamenu()

#Zafiyet Tarama 'biraz ayar çekilmesi lazım'

    if secim=="13":
        print("Default Vuln Scan ")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        onuchedef = input("     Enter Your Destination: ")
        if not onuchedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport13=input("\033[92mTop Port? Example 10 or 50, Default 50:\033[0m;  ")
            if not topport13:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+defaultportscan+" --script vuln " +onuchedef+" -oN "+"VulnScanDef-"+onuchedef+"-output" )
            else:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+topport13+" --script vuln " +onuchedef+" -oN "+"VulnScanDef-"+onuchedef+"-output" )
        
        anamenu()


    if secim=="14":
        print("FTP Vuln Scan ")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        ondorthedef = input("     Enter Your Destination: ")
        if not ondorthedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport14=input("\033[92mTop Port? Example 10 or 50, Default 50:\033[0m;  ")
            if not topport14:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+defaultportscan+" --script ftp* " +ondorthedef+" -oN "+"FTPvuln-"+ondorthedef+"-output" )
            else:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+topport14+" --script ftp* " +ondorthedef+" -oN "+"FTPvuln-"+ondorthedef+"-output" )
        
        anamenu()

    if secim=="15":
        print("SMB Vuln Scan ")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        onbeshedef = input("     Enter Your Destination: ")
        if not onbeshedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport15=input("\033[92mTop Port? Example 10 or 50, Default 50:\033[0m;  ")
            if not topport15:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+defaultportscan+" --script smb* " +onbeshedef+" -oN "+"SMBvuln-"+onbeshedef+"-output" )
            else:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+topport15+" --script smb* " +onbeshedef+" -oN "+"SMBvuln-"+onbeshedef+"-output" )
        
        anamenu()


    if secim=="16":
        print("HTTP Vuln Scan ")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        onaltihedef = input("     Enter Your Destination: ")
        if not onaltihedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport16=input("\033[92mTop Port? Example 10 or 50, Default 50:\033[0m;  ")
            if not topport16:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+defaultportscan+" --script smb* " +onaltihedef+" -oN "+"HTTPvuln-"+onaltihedef+"-output" )
            else:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+topport16+" --script smb* " +onaltihedef+" -oN "+"HTTPvuln-"+onaltihedef+"-output" )
        
        anamenu()   

    if secim=="17":
        print("SQL Injection Vuln Scan ")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        onyedihedef = input("     Enter Your Destination: ")
        if not onyedihedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport17=input("\033[92mTop Port? Example 10 or 50, Default 50:\033[0m;  ")
            if not topport17:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+defaultportscan+" --script=http-sql-injection " +onyedihedef+" -oN "+"SQLvuln-"+onyedihedef+"-output" )
            else:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+topport17+" --script=http-sql-injection " +onyedihedef+" -oN "+"SQLvuln-"+onyedihedef+"-output" )
        
        anamenu() 

    if secim=="18":
        print("Stored XSS Vuln Scan ")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        onsekizhedef = input("     Enter Your Destination: ")
        if not onsekizhedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport18=input("\033[92mTop Port? Example 10 or 50, Default 50:\033[0m;  ")
            if not topport18:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+defaultportscan+" --script=http-stored-xss.nse " +onsekizhedef+" -oN "+"StoredXSSvuln-"+onsekizhedef+"-output" )
            else:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+topport18+" --script=http-stored-xss.nse " +onsekizhedef+" -oN "+"StoredXSSvuln-"+onsekizhedef+"-output" )
        
        anamenu() 


    if secim=="19":
        print("DOM Based XSS Vuln Scan ")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        ondokuzhedef = input("     Enter Your Destination: ")
        if not ondokuzhedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport19=input("\033[92mTop Port? Example 10 or 50, Default 50:\033[0m;  ")
            if not topport19:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+defaultportscan+" --script=http-dombased-xss.nse " +ondokuzhedef+" -oN "+"DomBasedXSSvuln-"+ondokuzhedef+"-output" )
            else:
                os.system("nmap -vv -sV -ff -Pn --top-ports="+topport19+" --script=http-dombased-xss.nse " +ondokuzhedef+" -oN "+"DomBasedXSSvuln-"+ondokuzhedef+"-output" )
        
        anamenu() 
    
    
    if secim=="20":
        print("DNS Brute-force Hostnames ")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        yirmihedef = input("     Enter Your Destination: ")
        if not yirmihedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport20=input("\033[92mTop Port? Example 10 or 50, Default 50:\033[0m;  ")
            if not topport20:
                os.system("nmap --top-ports="+defaultportscan+" --script dns-brute " +yirmihedef+" -oN "+"subdomain_DnsBruteForce-"+yirmihedef+"-output" )
            else:
                os.system("nmap --top-ports="+topport20+" --script dns-brute " +yirmihedef+" -oN "+"subdomain_DnsBruteForce-"+yirmihedef+"-output" )
        
        anamenu()

    if secim=="21":
        print("Subdomain/hostmap-crtsh ")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        yirmibirhedef = input("     Enter Your Destination: ")
        if not yirmibirhedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport21=input("\033[92mTop Port? Example 10 or 50, Default 50:\033[0m;  ")
            if not topport21:
                os.system("nmap --top-ports="+defaultportscan+" --script hostmap-crtsh " +yirmibirhedef+" -oN "+"Subdomain_crtsh-"+yirmibirhedef+"-output" )
            else:
                os.system("nmap --top-ports="+topport21+" --script hostmap-crtsh " +yirmibirhedef+" -oN "+"Subdomain_crtsh-"+yirmibirhedef+"-output" )
        
        anamenu() 

    if secim=="22":
        print("Whois ")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        yirmiikihedef = input("     Enter Your Destination: ")
        if not yirmiikihedef:
            print("Pls Enter Target")
            print("\033[1;91mYou are grounded! You go to the main menu...\033[1;m")
            time.sleep(2)
            os.system("clear")
            baslangic()
        else:
            topport22=input("\033[92mTop Port? Example 10 or 50, Default 50:\033[0m;  ")
            if not topport22:
                os.system("nmap --top-ports="+defaultportscan+" --script whois-domain.nse " +yirmiikihedef+" -oN "+"whois-"+yirmiikihedef+"-output" )
            else:
                os.system("nmap --top-ports="+topport22+" --script whois-domain.nse " +yirmiikihedef+" -oN "+"whois-"+yirmiikihedef+"-output" )
        
        anamenu() 

    if secim=="00":
        print("\n             \033[1;91mContact\033[1;m")
        print("Mail: emre@emreylmz.com\nWeb Site: http://www.emreylmz.com\nGithub: https://github.com/delosemre\nTelegram: \033[1;91m@delosemre\033[1;m\n\n")
        secimdonus = input("root""\033[1;91m@KernelBlog:~$\033[1;m ")
        if secimdonus == "1":
            baslangic()
        if secimdonus == "2":
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
