def get_gpu_ids():
    if _mode() == LOCAL_MODE:
        raise Exception(
            'ray.get_gpu_ids() currently does not work in PYTHON MODE.')
    all_resource_ids = global_worker.raylet_client.resource_ids()
    assigned_ids = [resource_id for resource_id, _ in all_resource_ids.get(
        'GPU', [])]
    if global_worker.original_gpu_ids is not None:
        assigned_ids = [global_worker.original_gpu_ids[gpu_id] for gpu_id in
            assigned_ids]
    return assigned_ids