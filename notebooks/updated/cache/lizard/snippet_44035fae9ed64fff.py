def get_by_id(self, schema_id):
    if schema_id in self.id_to_schema:
        return self.id_to_schema[schema_id]
    url = '/'.join([self.url, 'schemas', 'ids', str(schema_id)])
    result, code = self._send_request(url)
    if code == 404:
        log.error('Schema not found:' + str(code))
        return None
    elif not (code >= 200 and code <= 299):
        log.error('Unable to get schema for the specific ID:' + str(code))
        return None
    else:
        schema_str = result.get('schema')
        try:
            result = loads(schema_str)
            self._cache_schema(result, schema_id)
            return result
        except ClientError as e:
            raise ClientError(
                'Received bad schema (id %s) from registry: %s' % (
                schema_id, e))