
# esse kra faz a ligação entre o apache e o python


def application(environ, start_response):
    import sys
    path = '/var/www/webroot/ROOT'
    if path not in sys.path:
        sys.path.append(path)

    # from pyinfo import pyinfo
    # from testemain import retorno
    from flask_simples.hello import app as application

    # output = pyinfo()
    # retorno = retorno()

    start_response('200 OK', [('Content-type', 'text/html')])

    # yield output.encode('utf-8')
    # yield retorno.encode('utf-8')
