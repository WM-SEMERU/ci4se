def aggregate_url(aggregate, url, err_exit_code=2):
    get_url_from = checker.get_url_from
    url = checker.guess_url(url)
    url_data = get_url_from(url, 0, aggregate, extern=(0, 0))
    aggregate.urlqueue.put(url_data)