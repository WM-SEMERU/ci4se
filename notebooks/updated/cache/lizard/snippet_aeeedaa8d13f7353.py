def _get_jmx_data(self, instance, jmx_address, tags):
    response = self._rest_request_to_json(instance, jmx_address, self.
        JMX_PATH, {'qry': self.HDFS_DATANODE_BEAN_NAME}, tags=tags)
    beans = response.get('beans', [])
    return beans