# -*- coding: utf-8 -*-

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.renderers import get_renderer

from sqlalchemy.exc import DBAPIError
import transaction

from .models import (
    DBSession,
    ModelUsers,
    )




@view_config(name="front", renderer="templates/front_page.pt", layout="layout_main")
def front_page_view(request):
    session = request.session
    if not ("ss" in session):
        if "op_type" in request.POST and request.POST["op_type"] == "sign_in":
            if ("login" in request.POST and "hesh" in request.POST):
                print "hesh = %s" % (request.POST["hesh"])
                print "password = %s" % (request.POST["password"])
                try:
                    user = DBSession.query(ModelUsers).filter(ModelUsers.login == request.POST["login"], \
                                                       ModelUsers.password == request.POST["hesh"]).first()
                except DBAPIError:
                    return Response(conn_err_msg, content_type='text/plain', status_int=500)
            else:
                msg = "login and/or password not send"
                return Response(msg, content_type='text/plain')
            if user == None:
                msg = "no such user in database"
                return Response(msg, content_type='text/plain')
            else:
                session["ss"] = "insession"
                print request.POST["login"], request.POST["hesh"]
                return {"plates": plates}
        elif "op_type" in request.POST and request.POST["op_type"] == "sign_up":
            post = request.POST
            user = ModelUsers(3, post["f_name"], post["l_name"], post["login"], post["hesh"], post["email"], 1)
            try:
                DBSession.add(user)
                transaction.commit()
            except DBAPIError:
                transaction.rollback()
                return Response("adding user error %s" % DBAPIError, content_type='text/plain', status_int=500)
            return {"plates": plates}
        else:
            return Response("wrong parameters %s" % request.POST, content_type='text/plain')
    return{"plates": plates}

@view_config(name="register", renderer="templates/sign_up.pt", layout="layout_sign")
def register_view(request):
    session = request.session
    if ("ss" in session):
        return Response("you are registered %s" % request.POST, content_type='text/plain')
    return {}

@view_config(name="login", renderer="z1:templates/sign_in.pt", layout="layout_sign")
def login_view(request):
    session = request.session
    if "logout" in request.POST and request.POST["logout"] == "true":
        print "invalidate"
        session.invalidate()
    return {"page_title": "Home"}
            
@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    """try:
        one = DBSession.query(ModelUsers).filter(ModelUsers.f_name == 'Администратор')
        for i in one:
            print i.login
            
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)"""
    return {'one': "one", 'project': 'z1'}

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_z1_db" script
    to initialize your database tables.  Check your virtual 
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, \
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."
        
plates = [{"color": "plate-green", "text": lorem_ipsum, "advert_text": "START RUBY COURSE NOW!",
           "advert_href": "#"},
           {"color": "plate-orange", "text": lorem_ipsum, "advert_text": "",
           "advert_href": ""},
           {"color": "plate-skyblue", "text": lorem_ipsum, "advert_text": "START RUBY COURSE NOW!",
           "advert_href": "#"},
           {"color": "plate-red", "text": lorem_ipsum, "advert_text": "",
           "advert_href": ""},
           {"color": "plate-salat", "text": lorem_ipsum, "advert_text": "START RUBY COURSE NOW!",
           "advert_href": "#"},
           {"color": "plate-skyblue", "text": lorem_ipsum, "advert_text": "",
           "advert_href": ""}]
