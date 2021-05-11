from klass_framework.temlator import render


class IndexView:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None))


class AboutView:
    def __call__(self, request):
        return '200 OK', render('about.html')


class ContactsView:
    def __call__(self, request):
        return '200 OK', render('contacts.html')
