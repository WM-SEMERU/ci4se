def delete(self, id):
    run = self.backend_store.get_run(id)
    if not run:
        return abort(http_client.NOT_FOUND, message="Run {} doesn't exist".
            format(id))
    if not self.manager.delete_run(run):
        return abort(http_client.BAD_REQUEST, message=
            'Failed to find the task queue manager of run {}.'.format(id))
    return '', http_client.NO_CONTENT