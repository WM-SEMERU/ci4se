def get_customer_transitions(self, issue_id_or_key):
    url = 'rest/servicedeskapi/request/{}/transition'.format(issue_id_or_key)
    return self.get(url, headers=self.experimental_headers)