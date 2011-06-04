r"""Discovers computer with a specfic port open on the given IP Range.
Usage:
    >>> from discovery import discover
    >>> discover(192.168.2.0/24, 80)
    ['192.168.2.125', '192.168.2.116', '192.168.1.140']
"""
import subprocess
import string
import sys

def discover(ip, port):
    ip2 = ip
    for i in string.split(ip, sep='.'):
        if '/' in i:
            ip = string.split(i, sep='/')[0]
            if int(ip) > 255:
                print 'Invalid IP range'
                sys.exit(0)
        else:
            if int(i) > 255:
                print 'Invalid IP range'
                sys.exit(0)
    cmd1 = '/usr/bin/nmap -v %s -p %s' %(ip2, port)
    cmd = string.split(cmd1)
    output =  subprocess.check_output(cmd)
    outputS = string.split(output, '\n')
    ipR = []
    
    for line in outputS:
        if 'Discovered open' in line:
            ipR.append(line.split()[-1])

    return ipR

