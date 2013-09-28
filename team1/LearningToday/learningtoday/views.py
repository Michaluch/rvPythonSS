from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import (
    authenticated_userid,
    remember,
    forget
)

from .models import (
    DBSession,
    Users,
    check_login,
    get_courses,
)

menu_links_in = [
    {'link': '#', 'text': 'About Us'},
    {'link': '#', 'text': 'Courses'},
    {'link': '/logout', 'text': 'Logout'}
]
menu_links_out = [
    {'link': '#', 'text': 'About Us'},
    {'link': '#', 'text': 'Courses'},
    {'link': '#', 'text': 'Sign In'},
    {'link': '/signup', 'text': 'Sign Up'}
]

footer_links = ('About Us', 'Courses', 'Terms')


@view_config(renderer='templates/layout.jinja2', route_name='jinja')
def index(request):
    return {'hello': 'world'}


class LoginSignUpLogoutViews(object):
    def __init__(self, request):
        self.request = request

    @view_config(renderer='templates/login.pt',
                 request_method="GET",
                 context='pyramid.httpexceptions.HTTPForbidden')
    def login_view(self):
        return {
            'app_url': self.request.application_url,
            'message': 'Please Login!',
            'menu_links': menu_links_out,
            'footer_links': footer_links
        }

    @view_config(renderer='templates/login.pt',
                 request_method="POST",
                 context='pyramid.httpexceptions.HTTPForbidden')
    def login_post(self):
        login = self.request.params.get("login")
        password = self.request.params.get("hash")

        if len(password) != 0 and check_login(login, password):
            headers = remember(self.request, login)
            return HTTPFound(location='/', headers=headers)

        message = 'Failed login'
        return {
            'app_url': self.request.application_url,
            'message': message,
            'menu_links': menu_links_out,
            'footer_links': footer_links
        }

    @view_config(route_name='logout')
    def logout(self):
        headers = forget(self.request)
        return HTTPFound(location='/', headers=headers)

    @view_config(route_name='signup',
                 renderer='templates/signup.pt',
                 request_method='POST')
    def signup(self):
        login = self.request.params.get('login')
        login_db = DBSession().query(Users).filter_by(login=login).first()
        hashed_password = self.request.params.get('hash')

        if login_db:
            return {
                'app_url': self.request.application_url,
                'message': 'User with login: {}, already exists.'.format(login),
                'login': login,
                'menu_links': menu_links_out,
                'footer_links': footer_links
            }

        user = Users(login, hashed_password, 1)
        DBSession().add(user)
        headers = remember(self.request, login)
        return HTTPFound(location='/', headers=headers)

    @view_config(route_name='signup',
                 renderer='templates/signup.pt',
                 request_method='GET')
    def signup_form(self):
        return {
            'app_url': self.request.application_url,
            'message': 'Please SignUp and join the Party!',
            'login': '',
            'menu_links': menu_links_out,
            'footer_links': footer_links
        }


class HomeView(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home',
                 renderer='templates/home.pt',
                 permission='view')
    def home(self):
        userid = authenticated_userid(self.request)
        num_boxes = 6
        if 'num_boxes' in self.request.params:
            if self.request.params['num_boxes']:
                num_boxes = self.request.params['num_boxes']
        return {
            'app_url': self.request.application_url,
            'menu_links': menu_links_in,
            'footer_links': footer_links,
            'boxes': generate_box(num_boxes),
            'user': userid,
        }


def generate_box(count):
    """receives: int(count)
    returns: list with dictionaries
    each dictionary will have unique keys id and link
    """
    courses = get_courses()
    count = int(count)

    if count > len(courses):
        count = len(courses)

    if count <= 1:
        count = 3
    elif count % 3 == 1:
        count -= 1
    elif count % 3 == 2:
        count += 1

    result = []
    for i in range(count):
        div_id = 'box-{}'.format(i)
        link = 'Link {}'.format(i + 1)
        course_name = courses[i][0]
        course_description = courses[i][1][:160].strip() + '...'
        result.append({'div_id': div_id,
                       'link': link,
                       'course_name': course_name,
                       'course_description': course_description})
    return result