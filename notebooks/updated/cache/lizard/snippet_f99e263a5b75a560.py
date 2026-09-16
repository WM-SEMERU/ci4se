def run(self):
    with self.input().open() as handle:
        body = json.loads(handle.read())
    es = elasticsearch.Elasticsearch()
    id = body.get('_id')
    es.index(index='frontpage', doc_type='html', id=id, body=body)