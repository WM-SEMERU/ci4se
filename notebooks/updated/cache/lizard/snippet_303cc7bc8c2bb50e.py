def create(self, client_id, subject, name, from_name, from_email, reply_to,
    html_url, text_url, list_ids, segment_ids):
    body = {'Subject': subject, 'Name': name, 'FromName': from_name,
        'FromEmail': from_email, 'ReplyTo': reply_to, 'HtmlUrl': html_url,
        'TextUrl': text_url, 'ListIDs': list_ids, 'SegmentIDs': segment_ids}
    response = self._post('/campaigns/%s.json' % client_id, json.dumps(body))
    self.campaign_id = json_to_py(response)
    return self.campaign_id