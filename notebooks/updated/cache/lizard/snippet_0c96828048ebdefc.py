def look_for_hdl_urls(citation_elements):
    for el in citation_elements:
        if el['type'] == 'URL':
            match = re_hdl.match(el['url_string'])
            if match:
                el['type'] = 'HDL'
                el['hdl_id'] = match.group('hdl_id')
                del el['url_desc']
                del el['url_string']