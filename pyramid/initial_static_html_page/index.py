from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import ConfigParser
import argparse
import pkg_resources


####################
## Tag Decorators - BEGIN
####################
def div(div_class='', div_id=''):
    def tag(func):
        def wrapper(*args):
            if div_class and div_id:
                return "<div class='{div_class}' id='{div_id}'>{foo}</div>".format(
                    div_class=div_class,
                    div_id=div_id,
                    foo=func(*args))
            if div_class:
                return "<div class='{div_class}'>{foo}</div>".format(
                    div_class=div_class,
                    foo=func(*args))
            if div_id:
                return "<div id='{div_id}'>{foo}</div>".format(
                    div_id=div_id,
                    foo=func(*args))

        return wrapper

    return tag


def tag(targ='', tclass=''):
    def tag(func):
        def wrapper(*args):
            if tclass:
                return "<{tag} class='{tclass}'>{foo}</{tag}>".format(
                    tag=targ,
                    tclass=tclass,
                    foo=func(*args))
            else:
                return "<{tag}>{foo}</{tag}>".format(tag=targ, foo=func(*args))

        return wrapper

    return tag


def link(func):
    def wrapper(*args):
        return "<a href='#'>{foo}</a>".format(foo=func(*args))

    return wrapper

####################
## Tag Decorators - END
####################


def get_config_and_args(section, config, args):
    Config = ConfigParser.ConfigParser()
    Config.read(config)
    pyramid_version = ''
    if args.version:
        # print('Version turned on')
        pyramid_version = pkg_resources.get_distribution("pyramid").version
    if pyramid_version:
        return """<div class="config_parser">
        <p>Config Parser Result: {}</p>
        <p>Pyramid version: {}</p>
        </div>""".format(Config.get(section, Config.options(section)[0]), pyramid_version)
    else:
        return """<div class="config_parser">
        <p>Config Parser Result: {}</p>
        </div>""".format(Config.get(section, Config.options(section)[0]))


class Block(object):
    """class that creates html divs
    divbody is optional
    """

    def __init__(
            self,
            divclass='empty',
            divid='',
            divbody='',
            onclick='',
    ):
        if divid and onclick:
            self.div_open = '<div class="{}" id="{}" onclick="{}">'.format(divclass, divid, onclick)
        else:
            self.div_open = '<div class="{}">'.format(divclass)
        self.div_body = '{}'.format(divbody)
        self.div_close = '</div>'

    def return_div(self):
        return '{open}{body}{close}'.format(open=self.div_open, body=self.div_body, close=self.div_close)

    def __str__(self):
        return self.return_div()


def generate_block(count, divclass, onclick):
    """function that generates instances
    of Block class, count must be int of how many
    instances you need
    return generator object
    """
    text = """\n<p>Lorem Ipsum Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse tincidunt ultrices leo, eu aliquam mauris placerat ac. Praesent quis lacus quis arcu aliquet ornare euismod ac nibh.</p>\n"""
    for i in range(count):
        divid = '{}-{}'.format(divclass, i)
        yield Block(
            divclass=divclass,
            divid=divid,
            onclick=onclick,
            divbody=text
        ).__str__()


class Head(object):
    """class that creates html header
    with:
        title it must be string
        and a list of string arguments
        that will be used as css stylesheet
        or link to js file based on file extension"""

    def __init__(self, *args, **kwargs):
        self.title = '<title>{}</title>'.format(kwargs.get('title'))
        self.css = ''
        self.js = ''
        for each in args:
            if each[-3:] == 'css':
                self.css += '<link rel="stylesheet" href="{}" type="text/css">'.format(each)
            elif each[-2:] == 'js':
                self.js += '<script src="{}" type="text/javascript"></script>'.format(each)
            else:
                pass

    def get_head(self):
        return '{css}{js}{title}'.format(
            css=self.css,
            js=self.js,
            title=self.title)

    def __str__(self):
        return self.get_head()


####################
## Decorating header div's
####################
@tag('li')
@link
def menu_item(name):
    return name


@div(div_id='header_menu')
@tag(targ='ul', tclass='nav_top')
def header_menu(*menu_items):
    return ''.join(menu_items)


@div(div_id='header_logo')
def header_logo():
    return ''


@div(div_class='header')
@div(div_class='header_container')
@div(div_class='header_content')
def header():
    result = ''
    result += header_logo()
    result += header_menu(
        menu_item('About Us'),
        menu_item('Courses'),
        menu_item('Sign In'),
        menu_item('Sign Up'),
    )
    return result


####################
## Decorating main div's
####################
@div(div_class='main_top')
def main_top():
    result = """<form method="post" action="#">
                <input type="text" id="main_search_form" 
                name="search courses" placeholder="Search courses" 
                onfocus="hide_text();" onblur="show_text();">
                </form>
                """
    return result


@div(div_class='main_box_wrapper')
def generator_to_str(func):
    """function to create string
    from result of generate_block() function
    which is a generator object with Div class
    instances inside"""
    result = ''
    for i in func:
        result += i
    return result


@div(div_class='main')
def main():
    result = ''
    result += main_top()
    result += generator_to_str(generate_block(6, 'main_box_style', 'changeBoxOne(this);'))
    return result


####################
## Decorating footer elements
####################
@div(div_class='footer_content_right_icons')
def footer_icons():
    return ''


@tag(targ='p')
def footer_follow():
    return 'Follow us:'


@div(div_class='footer_content_right')
def content_right():
    result = ''
    result += footer_follow()
    result += footer_icons()
    return result


@div(div_class='footer')
@div(div_class='footer_content')
def footer():
    result = ''
    result += content_right()
    return result


####################
## Creating Response Object
####################
def index(request):
    response = """<html>
    {head}
    <body onload='changeBoxAll();'>
    <div class="wrapper">
    {header}
    {config_parser}
    {main}
    <div class="push"></div>
    </div>
    {footer}
    </body>
    </html>""".format(
        head=Head('/css/header.css', '/css/main.css', '/css/footer.css', 'js/main.js', title='Learning 0day'),
        header=header(),
        main=main(),
        config_parser=get_config_and_args('SectionOne', 'myconfig.ini', args),
        footer=footer(),
    )
    return Response(response)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', help='return verison of pyramid', action='store_true')
    args = parser.parse_args()

    config = Configurator()

    config.add_static_view(
        name='css',
        path='static/css',
        cache_max_age=3600
    )
    config.add_static_view(
        name='js',
        path='static/js',
        cache_max_age=3600
    )
    config.add_static_view(
        name='img',
        path='static/img',
        cache_max_age=3600
    )

    config.add_route(name='index', pattern='/')

    config.add_view(index, route_name='index')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    print("Server started at http://localhost:8080")
    server.serve_forever()