# esse kra faz a ligação entre o apache e o python

import sys

sys.path.insert(0, "/var/www/webroot/ROOT")

# from flask_simples import app as application
from flask_restplus_teste import app as application


#def application(environ, start_response):
#    import sys
#    path = '/var/www/webroot/ROOT'
#    if path not in sys.path:
#        sys.path.append(path)

    # from pyinfo import pyinfo
    # from testemain import retorno
    # from flask_simples import app as application

    # output = pyinfo()
    # retorno = retorno()

    #start_response('200 OK', [('Content-type', 'text/html')])

    # yield output.encode('utf-8')
    # yield retorno.encode('utf-8')
    # yield 'churros ok'.encode('utf-8')