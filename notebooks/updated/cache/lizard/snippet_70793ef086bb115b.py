def _tail_profile(self, db, interval):
    latest_doc = None
    while latest_doc is None:
        time.sleep(interval)
        latest_doc = db['system.profile'].find_one()
    current_time = latest_doc['ts']
    while True:
        time.sleep(interval)
        cursor = db['system.profile'].find({'ts': {'$gte': current_time}}
            ).sort('ts', pymongo.ASCENDING)
        for doc in cursor:
            current_time = doc['ts']
            yield doc