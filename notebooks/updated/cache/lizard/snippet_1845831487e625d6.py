def listen_error_messages_raylet(worker, task_error_queue, threads_stopped):
    worker.error_message_pubsub_client = worker.redis_client.pubsub(
        ignore_subscribe_messages=True)
    error_pubsub_channel = str(ray.gcs_utils.TablePubsub.ERROR_INFO).encode(
        'ascii')
    worker.error_message_pubsub_client.subscribe(error_pubsub_channel)
    try:
        error_messages = global_state.error_messages(worker.task_driver_id)
        for error_message in error_messages:
            logger.error(error_message)
        while True:
            if threads_stopped.is_set():
                return
            msg = worker.error_message_pubsub_client.get_message()
            if msg is None:
                threads_stopped.wait(timeout=0.01)
                continue
            gcs_entry = ray.gcs_utils.GcsTableEntry.GetRootAsGcsTableEntry(msg
                ['data'], 0)
            assert gcs_entry.EntriesLength() == 1
            error_data = ray.gcs_utils.ErrorTableData.GetRootAsErrorTableData(
                gcs_entry.Entries(0), 0)
            driver_id = error_data.DriverId()
            if driver_id not in [worker.task_driver_id.binary(), DriverID.
                nil().binary()]:
                continue
            error_message = ray.utils.decode(error_data.ErrorMessage())
            if ray.utils.decode(error_data.Type()
                ) == ray_constants.TASK_PUSH_ERROR:
                task_error_queue.put((error_message, time.time()))
            else:
                logger.error(error_message)
    finally:
        worker.error_message_pubsub_client.close()