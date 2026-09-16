def profile(event_type, extra_data=None):
    worker = ray.worker.global_worker
    return RayLogSpanRaylet(worker.profiler, event_type, extra_data=extra_data)