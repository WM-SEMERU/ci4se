def build_response_card(title, subtitle, options):
    buttons = None
    if options is not None:
        buttons = []
        for i in range(min(5, len(options))):
            buttons.append(options[i])
    return {'contentType': 'application/vnd.amazonaws.card.generic',
        'version': 1, 'genericAttachments': [{'title': title, 'subTitle':
        subtitle, 'buttons': buttons}]}