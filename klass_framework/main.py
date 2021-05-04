class NotFoundView:
    def __call__(self, request):
        return '404 Not found', [b'bad request']


class Application:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts
    def __call__(self, environ, start_response):
        # print(type(environ))
        # print(environ)

        path = environ['PATH_INFO']
        print(path)
        print(self.routes)
        print(self.fronts)
        if not path.endswith('/'):
            path = path + '/'

        # page controller
        if path in self.routes:
            view = self.routes[path]
        else:
            view = NotFoundView()
        request = {}
        # front controllers
        for front in self.fronts:
            front(request)
        code, body = view(request)
        if not isinstance(body, list):
            body = [body.encode('utf-8')]
        print(request)
        print(code)
        print(body)
        start_response(code, [('Content-type', 'text/html')])
        return body
