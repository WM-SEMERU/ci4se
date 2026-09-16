def getTableColumns(table, columns, namespace='default', network='current',
    host=cytoscape_host, port=cytoscape_port, verbose=False):
    if type(network) != int:
        network = cytoscape('network', 'get attribute', {'network': network,
            'namespace': namespace, 'columnList': 'SUID'}, host=host, port=port
            )
        network = network[0]['SUID']
    df = pd.DataFrame()

    def target(column):
        URL = 'http://' + str(host) + ':' + str(port) + '/v1/networks/' + str(
            network) + '/tables/' + namespace + table + '/columns/' + column
        if verbose:
            print("'" + URL + "'")
            sys.stdout.flush()
        response = urllib2.urlopen(URL)
        response = response.read()
        colA = json.loads(response)
        col = pd.DataFrame()
        colHeader = colA['name']
        colValues = colA['values']
        col[colHeader] = colValues
        return col
    ncols = ['name']
    for c in columns:
        ncols.append(c.replace(' ', '%20'))
    for c in ncols:
        try:
            col = target(c)
            df = pd.concat([df, col], axis=1)
        except:
            print('Could not find ' + c)
            sys.stdout.flush()
    df.index = df['name'].tolist()
    df = df.drop(['name'], axis=1)
    return df