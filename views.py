from klass_framework.temlator import render


class IndexView:
    def __call__(self, request):
        return '200 OK', render('templates/index.html', date=request.get('date', None))

class AboutView:
    def __call__(self, request):
        return '200 OK', render('templates/about.html')
