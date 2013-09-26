#!/usr/bin/env python

import optparse
import sys
import textwrap

from pyramid.paster import bootstrap

def settings_show():
    description = """\
    Print the deployment settings for a Pyramid application.  Example:
    'psettings deployment.ini'
    """
    usage = "usage: %prog config_uri"
    parser = optparse.OptionParser(
        usage=usage,
        description=textwrap.dedent(description),
        version='version 1.0'
        )
    parser.add_option(
        '-o', '--omit',
        dest='omit',
        metavar='PREFIX',
        type='string',
        action='append',
        help=("Omit settings which start with PREFIX (you can use this "
              "option multiple times)")
        )
    
    options, args = parser.parse_args(sys.argv[1:])
    if not len(args) >= 1:
        print('You must provide at least one argument')
        return 2
    config_uri = args[0]
    omit = options.omit
    if omit is None:
        omit = []
    env = bootstrap(config_uri)
    settings, closer = env['registry'].settings, env['closer']
    try:
        for k, v in settings.items():
            if any([k.startswith(x) for x in omit]):
                continue
            print('%-40s     %-20s' % (k, v))
    finally:
        closer()