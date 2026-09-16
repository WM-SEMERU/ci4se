def get_trend_graph_url(start, end):
    filename = get_trend_graph_filename(start, end)
    urls = {'graph_url': urlparse.urljoin(GRAPH_URL, filename + '.png'),
        'data_url': urlparse.urljoin(GRAPH_URL, filename + '.csv')}
    return urls