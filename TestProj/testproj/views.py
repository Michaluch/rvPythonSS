from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'TestProj'}

@view_config(route_name='ajax_contact_handler', renderer='json')
def ajax_contact_handler(request):
    jsText = request.POST.get('contact_id', None)
    print jsText
    paragraph_id = "inputMessage"
    print paragraph_id

    paragraph = "<p id='{}'></p>".format(paragraph_id)
    print paragraph

    letter = "Hello Dima. I hope, that you accepted my message. I'm fine. Paragraph was sent for you. Hope you enjoy it. My friend JQuery will render it for you."
    print letter

    return {'paragraph_id': paragraph_id,
    		'paragraph': paragraph,
    		'letter': letter,
    		}