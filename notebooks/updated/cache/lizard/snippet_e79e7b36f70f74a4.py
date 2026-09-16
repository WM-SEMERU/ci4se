def subscribe(self):
    try:
        LOG.debug('Creating Kinesis subscription')
        if self.starting_position_ts:
            self._lambda_client.create_event_source_mapping(EventSourceArn=
                self.stream_name, FunctionName=self.function_name,
                BatchSize=self.batch_size, StartingPosition=self.
                starting_position, StartingPositionTimestamp=self.
                starting_position_ts)
        else:
            self._lambda_client.create_event_source_mapping(EventSourceArn=
                self.stream_name, FunctionName=self.function_name,
                BatchSize=self.batch_size, StartingPosition=self.
                starting_position)
        LOG.debug('Subscription created')
    except botocore.exceptions.ClientError as ex:
        response_code = ex.response['Error']['Code']
        if response_code == 'ResourceConflictException':
            LOG.debug('Subscription exists. Updating ...')
            resp = self._lambda_client.list_event_source_mappings(FunctionName
                =self.function_name, EventSourceArn=self.stream_name)
            uuid = resp['EventSourceMappings'][0]['UUID']
            self._lambda_client.update_event_source_mapping(UUID=uuid,
                FunctionName=self.function_name, Enabled=True, BatchSize=
                self.batch_size)
        else:
            LOG.error('Subscription failed, error=%s' % str(ex))
            raise ex