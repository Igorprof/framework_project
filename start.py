from wsgiref.simple_server import make_server

from klass_framework.main import Application
from urls import fronts
from views import routes

application = Application(routes, fronts)

with make_server('', 8000, application) as httpd:
    print('Start server on 8000...')
    httpd.serve_forever()