from bottle import route, run
import dejavu
import json

@get '/'
def introduce():
    print json.dump({"servers": dejavu.servers, "version": dejavu.version})

@post '/server'
def addserver():
    
