def _import_LOV(baseuri=
    'http://lov.okfn.org/dataset/lov/api/v2/vocabulary/list', keyword=''):
    printDebug('----------\nReading source... <%s>' % baseuri)
    query = requests.get(baseuri, params={})
    all_options = query.json()
    options = []
    if keyword:
        for x in all_options:
            if keyword in x['uri'].lower() or keyword in x['titles'][0]['value'
                ].lower() or keyword in x['nsp'].lower():
                options.append(x)
    else:
        options = all_options
    printDebug('----------\n%d results found.\n----------' % len(options))
    if options:
        counter = 1
        for x in options:
            uri, title, ns = x['uri'], x['titles'][0]['value'], x['nsp']
            click.echo(click.style('[%d]' % counter, fg='blue') + click.
                style(uri + ' ==> ', fg='black') + click.style(title, fg='red')
                )
            counter += 1
        while True:
            var = input(Style.BRIGHT +
                '=====\nSelect ID to import: (q=quit)\n' + Style.RESET_ALL)
            if var == 'q':
                break
            else:
                try:
                    _id = int(var)
                    ontouri = options[_id - 1]['uri']
                    print(Fore.RED + '\n---------\n' + ontouri +
                        '\n---------' + Style.RESET_ALL)
                    action_analyze([ontouri])
                    if click.confirm(
                        '=====\nDo you want to save to your local library?'):
                        action_import(ontouri)
                    return
                except:
                    print('Error retrieving file. Import failed.')
                    continue