def get_html_source_with_base_href(driver, page_source):
    last_page = get_last_page(driver)
    if '://' in last_page:
        base_href_html = get_base_href_html(last_page)
        return '%s\n%s' % (base_href_html, page_source)
    return ''