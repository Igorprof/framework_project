import datetime
from views import IndexView, AboutView, ContactsView


# front controllers
def date_front(request):
    request['date'] = datetime.date.today()


fronts = [date_front]

routes = {
    '/': IndexView(),
    '/about/': AboutView(),
    '/contacts/': ContactsView(),
}
