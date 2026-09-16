def _cleanup_orphaned_versions(self, dry_run):
    lib = self
    versions_coll = lib._collection.versions
    snapshots_coll = lib._collection.snapshots
    logger.info('ORPHANED SNAPSHOT CHECK: %s' % self._arctic_lib.get_name())
    gen_time = dt.now() - timedelta(days=1)
    parent_id_constraint = {'$lt': bson.ObjectId.from_datetime(gen_time)}
    snapshots = set(snapshots_coll.distinct('_id'))
    snapshots |= set(lib._audit.distinct('_id'))
    parents = versions_coll.aggregate([{'$project': {'parent': True}}, {
        '$unwind': '$parent'}, {'$match': {'parent': parent_id_constraint}},
        {'$group': {'_id': '$parent'}}])
    parent_ids = set([x['_id'] for x in parents])
    leaked_snaps = sorted(parent_ids - snapshots)
    if len(leaked_snaps):
        logger.info('leaked %d snapshots' % len(leaked_snaps))
    for x in leaked_snaps:
        ver_count = mongo_count(versions_coll, filter={'parent': x})
        logger.info("Missing Snapshot %s (%s) ; %s versions ref'd" % (x.
            generation_time, x, ver_count))
        if snapshots_coll.find_one({'_id': x}) is not None:
            raise Exception(
                "Error: snapshot (%s) is found, but shouldn't be!" % x)
        if not dry_run:
            versions_coll.update_many({'parent': x}, {'$pull': {'parent': x}})