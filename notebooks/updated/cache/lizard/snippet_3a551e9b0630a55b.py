def get_project_totals(entries, date_headers, hour_type=None, overtime=
    False, total_column=False, by='user'):
    totals = [(0) for date in date_headers]
    rows = []
    for thing, thing_entries in groupby(entries, lambda x: x[by]):
        name, thing_id, date_dict = date_totals(thing_entries, by)
        dates = []
        for index, day in enumerate(date_headers):
            if isinstance(day, datetime.datetime):
                day = day.date()
            if hour_type:
                total = date_dict.get(day, {}).get(hour_type, 0)
                dates.append(total)
            else:
                billable = date_dict.get(day, {}).get('billable', 0)
                nonbillable = date_dict.get(day, {}).get('non_billable', 0)
                total = billable + nonbillable
                dates.append({'day': day, 'billable': billable,
                    'nonbillable': nonbillable, 'total': total})
            totals[index] += total
        if total_column:
            dates.append(sum(dates))
        if overtime:
            dates.append(find_overtime(dates))
        dates = [(date or '') for date in dates]
        rows.append((name, thing_id, dates))
    if total_column:
        totals.append(sum(totals))
    totals = [(t or '') for t in totals]
    yield rows, totals