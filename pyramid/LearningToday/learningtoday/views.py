from pyramid.response import Response
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
    check_login
    )

menu_links_in = [{'link': '#', 'text': 'About Us'},
                 {'link': '#', 'text': 'Courses'},
                 {'link': '/logout', 'text': 'Logout'},
]
menu_links_out = [{'link': '#', 'text': 'About Us'},
                  {'link': '#', 'text': 'Courses'},
                  {'link': '#', 'text': 'Sign In'},
                  {'link': '/signup', 'text': 'Sign Up'},
]

footer_links = ('About Us', 'Courses', 'Terms')


@view_config(renderer='templates/layout.jinja2', route_name='jinja')
def index(request):
    return {'hello': 'world'}


@view_config(renderer='templates/login.pt',
             request_method="GET",
             context='pyramid.httpexceptions.HTTPForbidden')
def login_view(request):
    return {'app_url': request.application_url,
            'message': 'Please Login!',
            'menu_links': menu_links_out,
            'footer_links': footer_links}


@view_config(renderer='templates/login.pt',
             request_method="POST",
             context='pyramid.httpexceptions.HTTPForbidden')
def login_post(request):
    login = request.params.get("login")
    password = request.params.get("hash")

    if check_login(login, password):
        headers = remember(request, login)
        return HTTPFound(location='/', headers=headers)

    message = 'Failed login'
    return {'app_url': request.application_url,
            'message': message,
            'menu_links': menu_links_out,
            'footer_links': footer_links}


@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location='/', headers=headers)


@view_config(route_name='home',
             renderer='templates/home.pt',
             permission='view')
def home(request):
    userid = authenticated_userid(request)
    num_boxes = 6
    if 'num_boxes' in request.params:
        if request.params['num_boxes']:
            num_boxes = request.params['num_boxes']
    return {'app_url': request.application_url,
            'menu_links': menu_links_in,
            'footer_links': footer_links,
            'boxes': generate_box(num_boxes),
            'user': userid}


@view_config(route_name='signup',
             renderer='templates/signup.pt',
             request_method='POST')
def signup(request):
    session = DBSession()

    login = request.params.get('login')

    # print '####################################'
    # for each in request.params:
    #     print each
    # print '####################################'

    login_db = session.query(Users).filter_by(login=login).first()

    # password = request.params.get('password1')
    # passwordCheck = request.params.get('password2')
    hashed_password = request.params.get('hash')
    # print '####################################'
    # print password
    # print passwordCheck
    # print hashed_password
    # print '####################################'

    if login_db:
        return {'app_url': request.application_url,
                'message': 'User with login: {}, already exists.'.format(login),
                'login': login,
                'menu_links': menu_links_out,
                'footer_links': footer_links}
        # if password != confirm:
    #     return {'app_url': request.application_url,
    #             'message': 'Passwords doesnt match',
    #             'login': login}

    user = Users(login, hashed_password, 1)
    session.add(user)
    headers = remember(request, login)
    return HTTPFound(location='/', headers=headers)


@view_config(route_name='signup',
             renderer='templates/signup.pt',
             request_method='GET')
def signup_form(request):
    return {'app_url': request.application_url,
            'message': 'Please SignUp and join the Party!',
            'login': '',
            'menu_links': menu_links_out,
            'footer_links': footer_links}


def generate_box(count):
    """function that generates instances
    of Div class, count must be int of how many
    instances you need
    return generator object
    """
    count = int(count)
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
        result.append({'div_id': div_id, 'link': link})
    return result