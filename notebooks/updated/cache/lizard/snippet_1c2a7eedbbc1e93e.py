async def update(self, _id=None, **new_data):
    if not _id or not new_data:
        return {'error': 400, 'reason': 'Missed required fields'}
    document = await self.collection.find_one({'id': _id})
    if not document:
        return {'error': 404, 'reason': 'Not found'}
    for key in new_data:
        await self.collection.find_one_and_update({'id': _id}, {'$set': {
            key: new_data[key]}})
    updated = await self.collection.find_one({'id': _id})
    return {'success': 200, 'reason': 'Updated', **updated}