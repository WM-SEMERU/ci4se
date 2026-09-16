def filtersBM(dataset, host=biomart_host):
    stdout_ = sys.stdout
    stream = StringIO()
    sys.stdout = stream
    server = BiomartServer(host)
    d = server.datasets[dataset]
    d.show_filters()
    sys.stdout = stdout_
    variable = stream.getvalue()
    v = variable.replace('{', ' ')
    v = v.replace('}', ' ')
    v = v.replace(': ', '\t')
    print(v)