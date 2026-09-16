def parse_entry_media_attributes(self, soup):
    row_info = {}
    try:
        start = utilities.parse_profile_date(soup.find('series_start').text)
    except ValueError:
        start = None
    except:
        if not self.session.suppress_parse_exceptions:
            raise
    if start is not None:
        try:
            row_info['aired'] = start, utilities.parse_profile_date(soup.
                find('series_end').text)
        except ValueError:
            row_info['aired'] = start, None
        except:
            if not self.session.suppress_parse_exceptions:
                raise
    status_terms = getattr(self.session, self.type)(1)._status_terms
    try:
        row_info['id'] = int(soup.find('series_' + self.type + 'db_id').text)
    except:
        if not self.session.suppress_parse_exceptions:
            raise
    try:
        row_info['title'] = soup.find('series_title').text
    except:
        if not self.session.suppress_parse_exceptions:
            raise
    try:
        row_info['status'] = status_terms[int(soup.find('series_status').text)]
    except:
        if not self.session.suppress_parse_exceptions:
            raise
    try:
        row_info['picture'] = soup.find('series_image').text
    except:
        if not self.session.suppress_parse_exceptions:
            raise
    return row_info