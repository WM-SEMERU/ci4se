def parse_oembed_data(oembed_data, data):
    data.update({'oembed': oembed_data})
    _type = oembed_data.get('type')
    provider_name = oembed_data.get('provider_name')
    if not _type:
        return data
    if oembed_data.get('title'):
        data.update({'title': oembed_data.get('title')})
    if _type == 'video':
        try:
            item = {'width': convert_to_int(oembed_data.get('width')),
                'height': convert_to_int(oembed_data.get('height'))}
            if provider_name in ['YouTube']:
                item['src'] = HYPERLINK_PATTERN.search(oembed_data.get('html')
                    ).group(0)
            data['videos'].append(item)
        except Exception:
            pass
        if oembed_data.get('thumbnail_url'):
            item = {'width': convert_to_int(oembed_data.get(
                'thumbnail_width')), 'height': convert_to_int(oembed_data.
                get('thumbnail_height')), 'src': oembed_data.get(
                'thumbnail_url')}
            data['images'].append(item)
    return data