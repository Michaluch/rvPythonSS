from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


# 'hello_world' is the function that's called when we open up
# http://localhost:8080/hello/bar in the browser.
# We call the 'hello_world' function a 'view'.  Views accept 'Request'
# objects and return 'Response' objects.
def hello_world(request):
    # The request.matchdict is a dictionary that has a 'name' entry,
    # which corresponds to the '{name}' part in our '/hello/{name}'
    # route below.
    some_string = """
    <html>{}<body>{}{}</body></html>
    """.format(
        Head('Python Rocks!', 'header.css', 'footer.css', 'main.js'),
        Div(divclass='myclass', divbody='<h1>Hello Py</h1>'),
        myfunc(generate_block(6, 'main_box_style'))
    )
    return Response(some_string)


def myfunc(func):
    """function to create string
    from result of generate_block() function
    which is a generator object with Div class
    instances inside"""
    result = ''
    for i in func:
        result += i
    return result


def generate_block(count, divclass):
    """function that generates instances
    of Div class, count must be int of how many
    instances you need
    return generator object
    """
    text = 'Lorem Ipsum Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse tincidunt ultrices leo, eu aliquam mauris placerat ac. Praesent quis lacus quis arcu aliquet ornare euismod ac nibh.'
    for i in range(count):
        divid = '{}-{}'.format(divclass, i)
        yield Div(divclass=divclass, divid=divid, divbody=text).__str__()


class Div(object):
    """class that creates html divs
    divbody is optional
    """

    def __init__(self, divclass='empty', divid='', divbody=''):
        if len(divid) >= 1:
            self.div_open = '<div class={} id={}>'.format(divclass, divid)
        else:
            self.div_open = '<div class={}>'.format(divclass)
        self.div_body = '{}'.format(divbody)
        self.div_close = '</div>'

    def return_div(self):
        return '{open}{body}{close}'.format(open=self.div_open, body=self.div_body, close=self.div_close)

    def __str__(self):
        return self.return_div()


class Head(object):
    """class that creates html header
    with:
        title it must be string
        and a list of string arguments
        that will be used as css stylesheet
        or link to js file based on file extension"""

    def __init__(self, title, *args):
        self.head_open = '<head>'
        self.head_close = '</head>'
        self.title = '<title>{}</title>'.format(title)
        self.css = ''
        self.js = ''
        for each in args:
            if each[-3:] == 'css':
                self.css += '<link rel="stylesheet" href="{}" type="text/css">'.format(each)
            elif each[-2:] == 'js':
                self.js += '<script src="{}" type="text/javascript"></script>'.format(each)
            else:
                pass

    def get_css(self):
        return '{}{}{}{}{}'.format(self.head_open, self.css, self.js, self.title, self.head_close)

    def __str__(self):
        return self.get_css()


# Views may also return dictionaries:
def hello_json(request):
    return request.matchdict


if __name__ == '__main__':
    # Instantiate a Pyramid 'Configurator' object.  This one is used
    # to configure our views, and we'll use it ultimately to create
    # our WSGI application:
    config = Configurator()

    # This is the route configuration for our 'hello_world' view.
    # Note that the pattern has a variable part '{name}'.  Once our
    # view function is called, we can access the 'name' as
    # 'request.matchdict["name"]'.
    config.add_route(name='hello', pattern='/hello/{namesss}')

    # Next, we need to register our function as a view using the
    # 'hello' route we just defined:
    config.add_view(hello_world, route_name='hello')

    # Let's register another, slightly different route and associate
    # it with our second view: 'hello_json'.
    config.add_route(name='hello_json', pattern='/json/{name}')

    # Note that this time, we pass an additional 'renderer' argument
    # to 'config.add_view'.  This tells Pyramid to take the dictionary
    # that we return in our 'hello_json' function and turn it into a
    # JSON response.
    config.add_view(hello_json, route_name='hello_json', renderer='json')

    # We can now create our WSGI app and serve it using the standard
    # library 'wsgiref' server:
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    print("Server started at http://localhost:8080")
    server.serve_forever()