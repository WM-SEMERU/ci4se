def get_stats(self):
    try:
        query = {'size': 0, 'aggs': {'num_packages': {'value_count': {
            'field': 'id'}}, 'num_records': {'sum': {'field':
            'package.count_of_rows'}}, 'num_countries': {'cardinality': {
            'field': 'package.countryCode.keyword'}}}}
        aggregations = self.es.search(index=self.index_name, body=query)[
            'aggregations']
        return {key: int(value['value']) for key, value in aggregations.items()
            }
    except NotFoundError:
        return {}