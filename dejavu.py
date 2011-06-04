import simplejson
import subprocess
import string
import sys

load=simplejson.loads
dump=simplejson.dumps

version = '0.1-alpha'
servers = []

def discover(ip, port):
    """Discover ips with the given port open with for the given ip range
       Example: discover('192.168.2.0/24', '80')"""
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

def addserver(server):
    try:
        myip       = server['yourip'] # client's ip as seen by the server
        serverhost = server['host']
        serverport = server['port']
    except:
        raise ValueError('Invalid data.')

    server = {'myip' : myip, 'host' : serverhost, 'port' : serverport }
    servers.append(server)

    return True
