from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')

    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

    authentication_policy = AuthTktAuthenticationPolicy('learn2day', hashalg='sha512', max_age=1200)
    authorization_policy = ACLAuthorizationPolicy()

    config = Configurator(root_factory='learningtoday.models.RootFactory',
                          authentication_policy=authentication_policy,
                          authorization_policy=authorization_policy,
                          settings=settings)

    config.add_jinja2_search_path("learningtoday:templates")

    config.add_static_view(
        name='css',
        path='learningtoday:static/css'
    )
    config.add_static_view(
        name='img',
        path='learningtoday:static/img',
    )
    config.add_static_view(
        name='js',
        path='learningtoday:static/js',
    )
    config.add_route('home', '/')
    config.add_route('logout', '/logout')
    config.add_route('signup', '/signup')
    config.add_route('jinja', '/jinja')

    config.scan()
    return config.make_wsgi_app()
