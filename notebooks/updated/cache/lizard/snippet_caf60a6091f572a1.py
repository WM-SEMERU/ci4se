def update_status(table_name='swdata', date_column='date'):
    status_text = 'Latest entry: {}'.format(_get_most_recent_record(
        table_name, date_column))
    L.info(status_text)
    scraperwiki.status('ok', status_text)