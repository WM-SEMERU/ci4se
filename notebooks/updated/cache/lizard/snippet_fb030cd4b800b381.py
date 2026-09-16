def _execute_sql_query(self):
    self.log.info('starting the ``_execute_sql_query`` method')
    params = urllib.urlencode({'cmd': self.sqlQuery, 'format': 'json'})
    results = urllib.urlopen(self.sdssUrl + '?%s' % params)
    ofp = sys.stdout
    results = results.read()
    if results.startswith('ERROR'):
        ofp = sys.stderr
        ofp.write(string.rstrip(line) + os.linesep)
    results = results.replace(': ,', ': "NULL",')
    regex = re.compile('"photoz_err"\\:\\s*(\\n\\s*})')
    newString = regex.sub('"photoz_err": "NULL"\\g<1>', results)
    results = newString
    results = json.loads(results)[0]
    self.results = results['Rows']
    self.log.info('completed the ``_execute_sql_query`` method')
    return