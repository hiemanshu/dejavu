import bottle
from bottle import route, get, request, post, run
import dejavu
import simplejson

bottle.debug(True)

load=simplejson.loads
dump=simplejson.dumps

@get('/')
def introduce():
    return dump({"servers": dejavu.servers, "version": dejavu.version})

@get('/server')
def addserver():
    serverinfo = request.GET.get('data')
    result = dejavu.addserver(load(serverinfo))

    return dump({'result': result})

run(host='localhost', port=2012, reloader=True)
