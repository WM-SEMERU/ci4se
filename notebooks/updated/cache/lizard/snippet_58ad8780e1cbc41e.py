def get(self, master_id):
    collection_name = self.request.headers.get('collection')
    self.client = BaseAsyncMotorDocument('%s_revisions' % collection_name)
    limit = self.get_query_argument('limit', 2)
    add_current_revision = self.get_arg_value_as_type('addCurrent', 'false')
    show_history = self.get_arg_value_as_type('showHistory', 'false')
    objects_processed = []
    if isinstance(limit, unicode):
        limit = int(limit)
    objects = yield self.client.find({'master_id': master_id, 'processed':
        False}, orderby='toa', order_by_direction=1, page=0, limit=20)
    if len(objects) == 0:
        new_revision = yield self.__lazy_migration(master_id)
        if not new_revision:
            return
    if show_history:
        objects_processed = yield self.client.find({'master_id': master_id,
            'processed': True}, orderby='toa', order_by_direction=-1, page=
            0, limit=limit)
    elif add_current_revision:
        objects_processed = yield self.client.find({'master_id': master_id,
            'processed': True}, orderby='toa', order_by_direction=-1, page=
            0, limit=1)
    if len(objects_processed) > 0:
        objects_processed = objects_processed[::-1]
        objects_processed[-1]['current'] = True
        objects = objects_processed + objects
    self.write({'count': len(objects), 'results': objects})