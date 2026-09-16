def local_async(self, *args, **kwargs):
    local = salt.client.get_local_client(mopts=self.opts)
    ret = local.run_job(*args, **kwargs)
    return ret