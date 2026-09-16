def _with_retries(self, pool, fn):
    skip_nodes = []

    def _skip_bad_nodes(transport):
        return transport._node not in skip_nodes
    retry_count = self.retries - 1
    first_try = True
    current_try = 0
    while True:
        try:
            with pool.transaction(_filter=_skip_bad_nodes, yield_resource=True
                ) as resource:
                transport = resource.object
                try:
                    return fn(transport)
                except (IOError, HTTPException, ConnectionClosed) as e:
                    resource.errored = True
                    if _is_retryable(e):
                        transport._node.error_rate.incr(1)
                        skip_nodes.append(transport._node)
                        if first_try:
                            continue
                        else:
                            raise BadResource(e)
                    else:
                        raise
        except BadResource as e:
            if current_try < retry_count:
                resource.errored = True
                current_try += 1
                continue
            else:
                raise e.args[0]
        finally:
            first_try = False