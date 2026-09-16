def all_issues(issues):
    logging.info('finding issues...')
    seen = set()
    for issue in issues:
        if issue['title'] not in seen:
            seen.add(issue['title'])
            yield issue