def mutate(self, mutation=None, set_obj=None, del_obj=None, set_nquads=None,
    del_nquads=None, commit_now=None, ignore_index_conflict=None, timeout=
    None, metadata=None, credentials=None):
    mutation = self._common_mutate(mutation=mutation, set_obj=set_obj,
        del_obj=del_obj, set_nquads=set_nquads, del_nquads=del_nquads,
        commit_now=commit_now, ignore_index_conflict=ignore_index_conflict)
    new_metadata = self._dg.add_login_metadata(metadata)
    mutate_error = None
    try:
        assigned = self._dc.mutate(mutation, timeout=timeout, metadata=
            new_metadata, credentials=credentials)
    except Exception as error:
        if util.is_jwt_expired(error):
            self._dg.retry_login()
            new_metadata = self._dg.add_login_metadata(metadata)
            try:
                assigned = self._dc.mutate(mutation, timeout=timeout,
                    metadata=new_metadata, credentials=credentials)
            except Exception as error:
                mutate_error = error
        else:
            mutate_error = error
    if mutate_error is not None:
        try:
            self.discard(timeout=timeout, metadata=metadata, credentials=
                credentials)
        except:
            pass
        self._common_except_mutate(mutate_error)
    if mutation.commit_now:
        self._finished = True
    self.merge_context(assigned.context)
    return assigned