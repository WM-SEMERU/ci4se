def _drop_gracefully(self):
    mr_id = self.request.headers[util._MR_ID_TASK_HEADER]
    state = model.MapreduceState.get_by_job_id(mr_id)
    if not state or not state.active:
        return
    state.active = False
    state.result_status = model.MapreduceState.RESULT_FAILED
    config = util.create_datastore_write_config(state.mapreduce_spec)
    puts = []
    for ss in model.ShardState.find_all_by_mapreduce_state(state):
        if ss.active:
            ss.set_for_failure()
            puts.append(ss)
            if len(puts) > model.ShardState._MAX_STATES_IN_MEMORY:
                db.put(puts, config=config)
                puts = []
    db.put(puts, config=config)
    db.put(state, config=config)