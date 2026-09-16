def indexbox(msg='Shall I continue?', title=' ', choices=('Yes', 'No'),
    image=None, default_choice='Yes', cancel_choice='No'):
    reply = bb.buttonbox(msg=msg, title=title, choices=choices, image=image,
        default_choice=default_choice, cancel_choice=cancel_choice)
    if reply is None:
        return None
    for i, choice in enumerate(choices):
        if reply == choice:
            return i
    msg = (
        """There is a program logic error in the EasyGui code for indexbox.
reply={0}, choices={1}"""
        .format(reply, choices))
    raise AssertionError(msg)