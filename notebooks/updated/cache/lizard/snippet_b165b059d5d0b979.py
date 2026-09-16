def send_many(kwargs_list):
    emails = []
    for kwargs in kwargs_list:
        emails.append(send(commit=False, **kwargs))
    Email.objects.bulk_create(emails)