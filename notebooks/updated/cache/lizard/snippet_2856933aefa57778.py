def get_email(self):
    api_url = self.api_url + '/events/public'
    api_content = GithubRawApi(api_url, get_api_content_now=True).api_content
    for event in api_content:
        if event['type'] == 'PushEvent':
            return event['payload']['commits'][0]['author']['email']