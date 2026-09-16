def index(request, page):
    days = []
    days_found = set()
    query = Entry.query.order_by(Entry.pub_date.desc())
    pagination = Pagination(query, PER_PAGE, page, 'index')
    for entry in pagination.entries:
        day = date(*entry.pub_date.timetuple()[:3])
        if day not in days_found:
            days_found.add(day)
            days.append({'date': day, 'entries': []})
        days[-1]['entries'].append(entry)
    return render_template('index.html', days=days, pagination=pagination)