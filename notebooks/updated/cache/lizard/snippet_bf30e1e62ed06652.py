def multiprocessing_apply_infer(object_id):
    global inference_objects, inference_args, inference_kwargs
    return inference_objects[object_id]._infer_raw(*inference_args, **
        inference_kwargs)