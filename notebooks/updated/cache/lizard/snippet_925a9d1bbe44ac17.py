def str_name_value(name, value, tab=4, ljust=25):
    rep_name = name.startswith('_') and name[1:] or name
    try:
        return ' ' * tab + str(rep_name).ljust(ljust) + str(value).replace('\n'
            , '\n' + ' ' * (ljust + tab))
    except:
        rep_name = 'Exception in serializing %s value' % name
        return ' ' * tab + str(rep_name).ljust(ljust) + str(value).replace('\n'
            , '\n' + ' ' * (ljust + tab))