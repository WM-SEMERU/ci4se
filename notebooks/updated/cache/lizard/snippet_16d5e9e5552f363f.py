def create_new(mapreduce_id=None, gettime=datetime.datetime.now):
    if not mapreduce_id:
        mapreduce_id = MapreduceState.new_mapreduce_id()
    state = MapreduceState(key_name=mapreduce_id, last_poll_time=gettime())
    state.set_processed_counts([], [])
    return state