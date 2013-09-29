from pyramid_layout.layout import layout_config


@layout_config(name='layout_sign', template='z1:layouts/layout_sign.pt')
class layout_sign(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

@layout_config(name='layout_main', template='z1:layouts/layout_main.pt')
class layout_main(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request