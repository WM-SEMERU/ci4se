def url_to_destination_params(url):
    if url.startswith('pulsar://'):
        url = url[len('pulsar://'):]
    if not url.endswith('/'):
        url += '/'
    private_token_format = 'https?://(.*)@.*/?'
    private_token_match = match(private_token_format, url)
    private_token = None
    if private_token_match:
        private_token = private_token_match.group(1)
        url = url.replace('%s@' % private_token, '', 1)
    destination_args = {'url': url, 'private_token': private_token}
    return destination_args