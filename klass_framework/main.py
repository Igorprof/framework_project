import quopri
from .myrequests import PostRequests, GetRequests

class NotFoundView:
    def __call__(self, request):
        return '404 Not found', [b'bad request']


class Application:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts
    def __call__(self, environ, start_response):

        path = environ['PATH_INFO']

        request = {}
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests.get_request_params(environ)
            request['data'] = data
            print(f'POST: {Application.decode_data(data)}')
        elif method == 'GET':
            params = GetRequests.get_request_params(environ)
            request['request_params'] = params
            print(f'GET: {params}')

        if not path.endswith('/'):
            path = path + '/'

        # page controller
        if path in self.routes:
            view = self.routes[path]
        else:
            view = NotFoundView()
        
        # front controllers
        for front in self.fronts:
            front(request)
        code, body = view(request)
        if not isinstance(body, list):
            body = [body.encode('utf-8')]

        start_response(code, [('Content-type', 'text/html')])
        return body

    @staticmethod
    def decode_data(data):
        new_data = {}

        for key, value in data.items():
            val = bytes(value.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[key] = val_decode_str

        return new_data


class DebugApplication(Application):
    def __init__(self, routes, fronts):
        self.application = Application(routes, fronts)
        super().__init__(routes, fronts)

    def __call__(self, env, start_response):
        print('DEBUG MODE')
        print(env)
        return self.application(env, start_response)


class FakeApplication(Application):
    def __init__(self, routes, fronts):
        self.application = Application(routes, fronts)
        super().__init__(routes, fronts)

    def __call__(self, env, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Hello from Fake']