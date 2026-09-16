def _make_notice_date(self, response):
    today = date.today()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    week = today + timedelta(days=2)
    next_week = today + timedelta(weeks=1)
    future = today + timedelta(weeks=3)
    future_end = today + timedelta(weeks=5)
    json_data = json.loads(response.data)
    for notice in json_data['Notices']:
        if notice['NoticeAttributes'] and len(notice['NoticeAttributes']) > 0:
            for attr in notice['NoticeAttributes']:
                if attr['DataType'] == 'date':
                    if attr['Value'] == 'yesterday':
                        attr['Value'] = yesterday.strftime('%Y%m%d')
                    elif attr['Value'] == 'today':
                        attr['Value'] = today.strftime('%Y%m%d')
                    elif attr['Value'] == 'tomorrow':
                        attr['Value'] = tomorrow.strftime('%Y%m%d')
                    elif attr['Value'] == 'future':
                        attr['Value'] = future.strftime('%Y%m%d')
                    elif attr['Value'] == 'future_end':
                        attr['Value'] = future_end.strftime('%Y%m%d')
                    elif attr['Value'] == 'next_week':
                        attr['Value'] = next_week.strftime('%Y%m%d')
                    elif attr['Value'] == 'week':
                        attr['Value'] = week.strftime('%Y%m%d')
                    else:
                        pass
    response.data = json.dumps(json_data)