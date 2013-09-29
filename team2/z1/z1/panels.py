from pyramid_layout.panel import panel_config

@panel_config(name='header', renderer='z1:panels/header.pt')
def header_panel(context, request):
    return {}

@panel_config(name='footer', renderer='z1:panels/footer.pt')
def footer_panel(context, request):
    return {}

@panel_config(name='main_banner', renderer='z1:panels/main_banner.pt')
def main_banner_panel(context, request):
    return {}