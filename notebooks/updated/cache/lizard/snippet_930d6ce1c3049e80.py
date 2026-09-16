def parse_results_gen(search_term, field='title', max_results=100,
    sleep_time=0.1):
    if max_results * sleep_time > 30:
        warnings.warn(
            'Because of API limitations, this function        will take at least '
             + str(max_results * sleep_time) +
            ' seconds to return results.        If you need greater speed, try modifying the optional argument sleep_time=.1, (although         this may cause the search to time out)'
            )
    all_data_raw = find_results_gen(search_term, field=field)
    all_data = list()
    while len(all_data) < max_results:
        all_data.append(all_data_raw.send(None))
        time.sleep(sleep_time)
    return all_data