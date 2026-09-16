def execute_session(self, session_data):
    pipe = self.client.pipeline()
    for sm in session_data:
        meta = sm.meta
        if sm.structures:
            self.flush_structure(sm, pipe)
        delquery = None
        if sm.deletes is not None:
            delquery = sm.deletes.backend_query(pipe=pipe)
        self.accumulate_delete(pipe, delquery)
        if sm.dirty:
            meta_info = json.dumps(self.meta(meta))
            lua_data = [len(sm.dirty)]
            processed = []
            for instance in sm.dirty:
                state = instance.get_state()
                if not meta.is_valid(instance):
                    raise FieldValueError(json.dumps(instance._dbdata[
                        'errors']))
                score = MIN_FLOAT
                if meta.ordering:
                    if meta.ordering.auto:
                        score = meta.ordering.name.incrby
                    else:
                        v = getattr(instance, meta.ordering.name, None)
                        if v is not None:
                            score = meta.ordering.field.scorefun(v)
                data = instance._dbdata['cleaned_data']
                action = state.action
                prev_id = state.iid if state.persistent else ''
                id = instance.pkvalue() or ''
                data = flat_mapping(data)
                lua_data.extend((action, prev_id, id, score, len(data)))
                lua_data.extend(data)
                processed.append(state.iid)
            self.odmrun(pipe, 'commit', meta, (), meta_info, *lua_data,
                iids=processed)
    return pipe.execute()