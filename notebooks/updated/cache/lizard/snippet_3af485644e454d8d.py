def facts():
    ret = {}
    try:
        ret['facts'] = __proxy__['junos.get_serialized_facts']()
        ret['out'] = True
    except Exception as exception:
        ret['message'] = 'Could not display facts due to "{0}"'.format(
            exception)
        ret['out'] = False
    return ret