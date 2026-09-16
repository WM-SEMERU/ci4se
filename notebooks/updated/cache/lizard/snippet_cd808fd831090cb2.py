def multchoicebox(message='Pick as many items as you like.', title='',
    choices=['program logic error - no choices specified']):
    return psidialogs.multi_choice(message=message, title=title, choices=
        choices)