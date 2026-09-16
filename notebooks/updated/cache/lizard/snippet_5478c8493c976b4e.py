def exclude_range(self, field, start='*', stop='*', inclusive=True,
    new_group=False):
    if start is None:
        start = '*'
    if stop is None:
        stop = '*'
    if start == '*' and stop == '*':
        return self.match_not_exists(field, new_group=new_group)
    if inclusive:
        value = '[' + str(start) + ' TO ' + str(stop) + ']'
    else:
        value = '{' + str(start) + ' TO ' + str(stop) + '}'
    return self.exclude_field(field, value, new_group=new_group)