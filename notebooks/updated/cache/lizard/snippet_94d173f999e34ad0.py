def AnsiText(text, command_list=None, reset=True):
    command_list = command_list or ['reset']
    if reset:
        return '%s%s%s' % (_AnsiCmd(command_list), text, _AnsiCmd(['reset']))
    else:
        return '%s%s' % (_AnsiCmd(command_list), text)