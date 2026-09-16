def print_dict(d, show_missing=True):
    for k, v in sorted(d.items()):
        if not v and show_missing:
            print('{} -'.format(k))
        elif isinstance(v, list):
            print(k)
            for item in v:
                print('   {}'.format(item))
        elif isinstance(v, dict):
            print(k)
            for kk, vv in sorted(v.items()):
                print('   {:<20} {}'.format(kk, vv))