def createissue(accountable, options):
    issue = accountable.issue_create(options)
    headers = sorted(['id', 'key', 'self'])
    rows = [headers, [itemgetter(header)(issue) for header in headers]]
    print_table(SingleTable(rows))