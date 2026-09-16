def __fix_field_date(self, item, attribute):
    field_date = str_to_datetime(item[attribute])
    try:
        _ = int(field_date.strftime('%z')[0:3])
    except ValueError:
        logger.warning('%s in commit %s has a wrong format', attribute,
            item['commit'])
        item[attribute] = field_date.replace(tzinfo=None).isoformat()