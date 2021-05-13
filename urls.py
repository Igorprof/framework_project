import datetime
from views import IndexView, AboutView, ContactsView, CoursesList, CreateCourse, CreateCategory, CategoryList, CopyCourse


# front controllers
def date_front(request):
    request['date'] = datetime.date.today()


fronts = [date_front]

routes = {
    '/': IndexView(),
    '/about/': AboutView(),
    '/contacts/': ContactsView(),
    '/courses-list/': CoursesList(),
    '/create-course/': CreateCourse(),
    '/create-category/': CreateCategory(),
    '/category-list/': CategoryList(),
    '/copy-course/': CopyCourse()
}
