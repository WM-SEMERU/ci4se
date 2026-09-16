def template_to_dict_debug(name, item, debug):
    if debug == 1:
        print('\n%s = ' % name)
    elif debug > 1:
        print('\n%s' % name)
        print('=' * 64)
        print(lxml.etree.tostring(item))
        print()