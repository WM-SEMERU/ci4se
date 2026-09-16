def delete(self, dash_id):
    removed_info = dict(time_modified=r_db.zscore(config.DASH_ID_KEY,
        dash_id), meta=r_db.hget(config.DASH_META_KEY, dash_id), content=
        r_db.hget(config.DASH_CONTENT_KEY, dash_id))
    r_db.zrem(config.DASH_ID_KEY, dash_id)
    r_db.hdel(config.DASH_META_KEY, dash_id)
    r_db.hdel(config.DASH_CONTENT_KEY, dash_id)
    return {'removed_info': removed_info}