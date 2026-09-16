def element_by_href_as_json(href, params=None):
    if href:
        element = fetch_json_by_href(href, params=params)
        if element:
            return element.json