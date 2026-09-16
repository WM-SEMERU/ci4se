def get_es(url, **kwargs):
    urls = [url] if isinstance(url, str) else url
    kwargs.setdefault('serializer', ElasticJSONSerializer())
    es = elasticsearch.Elasticsearch(urls, **kwargs)
    return es