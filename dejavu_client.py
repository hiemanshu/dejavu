from bottle import route, get, post, run
import dejavu
import json

@get('/')
def introduce():
    print json.dump({"servers": dejavu.servers, "version": dejavu.version})

@post('/server')
def addserver():
    print request.body
    dejavu.servers.append(request.body)

run(host='localhost', port=2012)
