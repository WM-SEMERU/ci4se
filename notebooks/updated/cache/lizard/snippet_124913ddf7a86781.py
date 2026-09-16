def register(coordinator):
    if FLAGS.phantomjs_script:
        utils.verify_binary('phantomjs_binary', ['--version'])
        assert os.path.exists(FLAGS.phantomjs_script)
    else:
        utils.verify_binary('capture_binary', ['--version'])
        assert FLAGS.capture_script
        assert os.path.exists(FLAGS.capture_script)
    assert FLAGS.capture_threads > 0
    assert FLAGS.queue_server_prefix
    item = queue_worker.RemoteQueueWorkflow(constants.CAPTURE_QUEUE_NAME,
        DoCaptureQueueWorkflow, max_tasks=FLAGS.capture_threads,
        wait_seconds=FLAGS.capture_wait_seconds)
    item.root = True
    coordinator.input_queue.put(item)