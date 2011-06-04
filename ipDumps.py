from discovery import discover
from time import sleep

def dumps():
    while True:
        print discover('192.168.2.0/24', '80')
        print 'Sleeping for 60 secs'
        sleep(60)

dumps()
