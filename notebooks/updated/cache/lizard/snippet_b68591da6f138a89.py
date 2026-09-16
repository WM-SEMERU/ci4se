def get(self, stype, flags, filters, options=None):
    if not isinstance(flags, str):
        if isinstance(flags, list):
            finflags = ','.join(flags)
        else:
            raise SyntaxError(
                'Flags should be a list or comma separated string')
    else:
        finflags = flags
    if not isinstance(filters, str):
        raise SyntaxError(
            'Filters needs to be a string in the format Filter<op>Value. The simplest form is search="<Term>".'
            )
    if stype not in self.stypes:
        raise SyntaxError('{} not a valid Search type.'.format(stype))
    if '"' not in filters or "'" not in filters:
        newfilters = self.helperpat.split(filters)
        newfilters = [x.strip() for x in newfilters]
        newfilters[1] = '"' + newfilters[1] + '"'
        op = self.helperpat.search(filters)
        newfilters = op.group(0).join(newfilters)
        command = '{} {} ({}){}'.format(stype, finflags, newfilters, ' ' +
            ujson.dumps(options) if options is not None else '')
    else:
        command = '{} {} ({}){}'.format(stype, finflags, filters, ' ' +
            ujson.dumps(options) if options is not None else '')
    data = self.connection.send_command('get', command)
    if 'id' in data:
        raise ServerError(data['msg'], data['id'])
    else:
        return {'pages': data.get('more', default=False), 'data': data['items']
            }