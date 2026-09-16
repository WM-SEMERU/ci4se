def query_bulk(names):
    answers = [__threaded_query(name) for name in names]
    while True:
        if all([a.done() for a in answers]):
            break
        sleep(1)
    return [answer.result() for answer in answers]