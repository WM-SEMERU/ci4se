def __get_total_response_time(meta_datas_expanded):
    try:
        response_time = 0
        for meta_data in meta_datas_expanded:
            response_time += meta_data['stat']['response_time_ms']
        return '{:.2f}'.format(response_time)
    except TypeError:
        return 'N/A'