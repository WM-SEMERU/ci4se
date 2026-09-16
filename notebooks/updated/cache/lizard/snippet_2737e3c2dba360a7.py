def plural_fmt(name, cnt):
    if cnt == 1:
        return '{} {}'.format(cnt, name)
    else:
        return '{} {}s'.format(cnt, name)