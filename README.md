# delosNmap


Menu Options

                Default Scan Types 
        1-) Default Scan
        2-) Host Discovery
        3-) Port(SYN) Scan
        4-) Port(TCP) Scan
        5-) Port(UDP) Scan
        6-) Null scan (-sN)
        7-) FIN scan (-sF)
        8-) OS Analysis and Version Discovery
        9-) Nmap Script Engineering (default)
        
                Firewall Bypass
        10-) Script Bypass (--script=firewall-bypass)
        11-) Data Length (--data-length <number> )
        12-) Smash (-ff)
        
                Vulnerability Scanning
        13-) Default Vuln Scan (--script vuln)
        14-) FTP Vuln Scan
        15-) SMB Vuln Scan
        16-) HTTP Vuln Scan
        17-) SQL Injection Vuln Scan
        18-) Stored XSS Vuln Scan
        19-) Dom Based XSS vuln Scan
                Subdomain Scanning
        20-) DNS Brute-force Hostnames
        21-) Subdomain/hostmap-crtsh
                Other
        22-) Whois

        00-) Contact
        0-) Exit
       
## New Features on 06.10.2022
        *Subdomain
        *Whois
        
## Usage
        sudo python3 delosNmap.py
        
## Libraries
        import sys
        import os
        import time
        import signal
        from time import sleep
        from sys import argv
        from platform import system

## Example Usage
[![asciicast](https://asciinema.org/a/TvecD1aJyaY1zdWwPUwlsOOQO.svg)](https://asciinema.org/a/TvecD1aJyaY1zdWwPUwlsOOQO)

## Image

![image](https://raw.githubusercontent.com/delosemre/resimler/master/delosNmap%20Resimler/delosnmapv2.5.PNG)

## Notice

Run it with Python3 and don't forget to be root! <br>
Communicate for suggestions!

## Contact
delosemre@outlook.com <br>
emre@emreylmz.com <br>
https://emreylmz.com <br>
https://t.me/delosemre <br> 
https://twitter.com/delosemre
