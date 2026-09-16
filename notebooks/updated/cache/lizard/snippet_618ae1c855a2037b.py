def prepare_connection():
    elasticsearch_host = getattr(settings, 'ELASTICSEARCH_HOST', 'localhost')
    elasticsearch_port = getattr(settings, 'ELASTICSEARCH_PORT', 9200)
    connections.create_connection(hosts=['{}:{}'.format(elasticsearch_host,
        elasticsearch_port)])