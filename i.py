#!/home/alex/www/pyramid/VENV/bin/python

import os
import ConfigParser
import argparse

from collections import OrderedDict
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


#PageGeneralParts
class PGParts:
    @staticmethod
    def make_doc_header(title, scripts, styles):
        title = title or ""
        output = "<!DOCTYPE html><html><head><title>%s</title>" % title
        for script in scripts:
            output = "".join([output, "<script src='http://localhost/pyramid/project/js/%s.js' \
            type='text/javascript'></script>" % script])
        for style in styles:
            output = "".join([output, "<link rel='stylesheet' \
            href='http://localhost/pyramid/project/css/%s.css' />" % style])
        output = "".join([output, "</head>"])
        return output

    @staticmethod
    def make_doc_footer():
        output = "</body></html>"
        return output

    @staticmethod
    def make_page_header(menu_items):
        output = "<div class='header-background'></div>\
        <div class='header'>\
        <div class='main-logo' id='logo-button'> \
        </div><div class='main-menu'><ul>"
        for item in menu_items:
            if item == "divider":
                output = "".join([output, "<li class='main-menu-divider'>|</li>"])
                continue
            output = "".join([output, "<li><a href='%s'>%s</a></li>" % (menu_items[item], item)])
        output = "".join([output, "</ul></div></div>"])
        return output


    @staticmethod
    def make_page_footer(bottom_menu_items, follow_us_items):
        output = "<div class='footer-background'></div>\
        <div class='footer'><div class='bottom-menu'><ul>"
        for item in bottom_menu_items:
            if item == "divider":
                pass
                #here will be bottom menu divider
                #output = "".join([output])
            output = "".join([output, "<li><a href='%s'>%s</a></li>" % (bottom_menu_items[item], item)])
        output = "".join([output, "</ul></div><div class='followus-bottom clearfix'> \
        <div class='followus-label'>Follow us:</div>"])
        for item in follow_us_items:
            output = "".join([output, "<a href='%s'><img class='follow-logo' \
            src='http://localhost/pyramid/project/img/%s' /></a>" % (follow_us_items[item], item)])
        output = "".join([output, "</div></div>"])
        return output


class BuildPage:
    
    config = {}
    
    @staticmethod
    def build(route):
        if route["name1"] == "index":
            return BuildPage.build_front_page()
        else:
            return "%s" % route

    @staticmethod
    def build_front_page():
        scripts = OrderedDict([("test", "")])
        styles = OrderedDict([("reset", ""),
                              ("common", ""),
                              ("header", ""),
                              ("front-page", ""),
                              ("footer", "")])

        top_menu_items = OrderedDict([("About us", "#"),
                                      ("Courses", "#"),
                                      ("divider", " "),
                                      ("Sign in", "#"),
                                      ("Sign up", "#")])

        bottom_menu_items = OrderedDict([("About us", "#"),
                                         ("Courses", "#"),
                                         ("Terms", "#")])

        follow_us_items = OrderedDict([("facebook-large.png", "#"),
                                       ("twitter-large.png", "#"),
                                       ("googlep-large.png", "#")])

        lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, \
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."

        plates = OrderedDict([("plate1", OrderedDict([("colour", "plate-green"),
                                                     ("text", lorem_ipsum),
                                                     ("advert", OrderedDict([("text", "START RUBY COURSE NOW!"),
                                                                             ("href", "#")])
                                                     )])),

                              ("plate2", OrderedDict([("colour", "plate-orange"),
                                                     ("text", lorem_ipsum),
                                                     ("advert", OrderedDict([("text", "START RUBY COURSE NOW!"),
                                                                             ("href", "#")])
                                                     )])),

                              ("plate3", OrderedDict([("colour", "plate-skyblue"),
                                                     ("text", lorem_ipsum),
                                                     ("advert", OrderedDict([("text", ""),
                                                                             ("href", "")])
                                                     )])),

                              ("plate4", OrderedDict([("colour", "plate-red"),
                                                     ("text", lorem_ipsum),
                                                     ("advert", OrderedDict([("text", "START RUBY COURSE NOW!"),
                                                                             ("href", "#")])
                                                     )])),

                              ("plate5", OrderedDict([("colour", "plate-salat"),
                                                     ("text", lorem_ipsum),
                                                     ("advert", OrderedDict([("text", ""),
                                                                             ("href", "")])
                                                     )])),

                              ("plate6", OrderedDict([("colour", "plate-skyblue"),
                                                     ("text", lorem_ipsum),
                                                     ("advert", OrderedDict([("text", "START RUBY COURSE NOW!"),
                                                                             ("href", "#")])
                                                     )]))
                                ])

        page = ""
        page = "".join([page, PGParts.make_doc_header("Front page", scripts, styles)])
        page = "".join([page, PGParts.make_page_header(top_menu_items)])
        page = "".join([page, "<body>"])

        page = "".join([page, "<div class='front-page-wrapper clearfix'>\
        <div class='main-banner'> \
        <div class='frontpage-search'>\
        <form name='frontpage-search-form'> \
        <input class='search-input-large' id='search-frontpage' type='text' name='search-field' \
        placeholder='Search courses' />\
        </form></div></div>\
        <div class='courses-grid'>"])
        for plate in plates:
            page = "".join([page, "<div class='course-plate %s' \
            tabindex='0'>%s" % (plates[plate]["colour"], plates[plate]["text"])])
            if plates[plate]["advert"]["text"] != "" and plates[plate]["advert"]["href"] != "":
                page = "".join([page, "<div class='course-plate-advert'><a href='%s'>%s</a></div> \
                " % (plates[plate]["advert"]["href"], plates[plate]["advert"]["text"])])
            page = "".join([page, "</div>"])
        page = "".join([page, "</div></div>"])

        page = "".join([page, PGParts.make_page_footer(bottom_menu_items, follow_us_items)])
        page = "".join([page, PGParts.make_doc_footer()])
        return page


class StartConfigServer:
    
    @staticmethod
    def root_view(request):
        output = BuildPage.build(request.matchdict)
        return Response(output)

    @staticmethod
    def start_server():
        config = Configurator()
        config.add_route("route", "/{name1}")
        config.add_view(StartConfigServer.root_view, route_name="route")
        app = config.make_wsgi_app()
        server = make_server("0.0.0.0", 2000, app)
        server.serve_forever()


if __name__ == "__main__":
    if not os.path.isfile("config.ini"):
        f = open("config.ini", "w+")
        config_pars = ConfigParser.ConfigParser()
        config_pars.add_section("user")
        config_pars.set("user", "name", "ThisUser")
        config_pars.set("user", "age", "90")
        config_pars.add_section("corp_server")
        config_pars.set("corp_server", "url", "server.com")
        config_pars.set("corp_server", "corp", "Mega Inc")
        config_pars.write(f)
        f.close()
    else:
        f = open("config.ini", "r")
        config_pars = ConfigParser.ConfigParser()
        config_pars.readfp(f)
        for section in config_pars.sections():
            BuildPage.config[section] = {}
            for key, value in config_pars.items(section):
                BuildPage.config[section][key] = value
        f.close()
        print "Config: %s" % (BuildPage.config)
        # i can add BuildPage.config to the page with no problem, but don't want to break design
        # it outputs in console
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", help="enter version of program here")
    args = parser.parse_args() 
    print "Script version: %s" % (args.version)
    # output verison in console

    
    StartConfigServer.start_server()
