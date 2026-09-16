def index():
    crawler_list = []
    for crawler in manager:
        is_due = 'yes' if crawler.check_due() else 'no'
        if crawler.disabled:
            is_due = 'off'
        crawler_list.append([crawler.name, crawler.description, crawler.
            schedule, is_due, Queue.size(crawler)])
    headers = ['Name', 'Description', 'Schedule', 'Due', 'Pending']
    print(tabulate(crawler_list, headers=headers))