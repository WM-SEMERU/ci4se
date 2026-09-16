def csv(self, jql, limit=1000):
    url = (
        'sr/jira.issueviews:searchrequest-csv-all-fields/temp/SearchRequest.csv?tempMax={limit}&jqlQuery={jql}'
        .format(limit=limit, jql=jql))
    return self.get(url, not_json_response=True, headers={'Accept':
        'application/csv'})