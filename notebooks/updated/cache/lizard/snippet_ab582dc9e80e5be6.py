def stop_recording():
    global _recording
    if not _recording:
        raise ValueError('Must call "start_recording" before.')
    recorded_events_queue, hooked = _recording
    unhook(hooked)
    return list(recorded_events_queue.queue)