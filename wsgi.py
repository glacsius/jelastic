def application(environ, start_response):
    import sys
    path = '/var/www/webroot/ROOT'
    if path not in sys.path:
        sys.path.append(path)
    from pyinfo import pyinfo
    output = pyinfo()
    start_response('200 OK', [('Content-type', 'text/html')])
    yield output.encode('utf-8')
