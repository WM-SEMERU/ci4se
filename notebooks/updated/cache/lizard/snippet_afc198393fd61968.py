def create_html(api_key, attrs):
    gif = get_gif(api_key, attrs['gif_id'])
    if 'alt' not in attrs.keys():
        attrs['alt'] = 'source: {}'.format(gif['data']['source'])
    html_out = '<a href="{}">'.format(gif['data']['url'])
    html_out += '<img src="{}" alt="{}">'.format(gif['data']['images'][
        'original']['url'], attrs['alt'])
    html_out += '</a>'
    return html_out