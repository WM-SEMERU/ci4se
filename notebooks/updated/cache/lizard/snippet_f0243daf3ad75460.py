def parse_response(fields, records):
    data = [i['values']['data'] for i in records]
    return [{fields[idx]: row for idx, row in enumerate(d)} for d in data]