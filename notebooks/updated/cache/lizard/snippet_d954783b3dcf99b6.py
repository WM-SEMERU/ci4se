def _dispatch(self, input_batch: List[SingleQuery]):
    method = getattr(self, self.serve_method)
    if hasattr(method, 'ray_serve_batched_input'):
        batch = [inp.data for inp in input_batch]
        result = _execute_and_seal_error(method, batch, self.serve_method)
        for res, inp in zip(result, input_batch):
            ray.worker.global_worker.put_object(inp.result_object_id, res)
    else:
        for inp in input_batch:
            result = _execute_and_seal_error(method, inp.data, self.
                serve_method)
            ray.worker.global_worker.put_object(inp.result_object_id, result)