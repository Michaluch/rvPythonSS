from pyramid.view import view_config
import ConfigParser


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    conf = ConfigParser.ConfigParser()
    conf.read('setup.cfg')
    user = conf.get('newsection', 'username').__str__()
    return {'project': 'NewProject', 'username': user}
