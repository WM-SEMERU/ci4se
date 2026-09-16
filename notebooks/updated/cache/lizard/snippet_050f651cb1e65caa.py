def log_assist_request_without_audio(assist_request):
    if logging.getLogger().isEnabledFor(logging.DEBUG):
        resp_copy = embedded_assistant_pb2.AssistRequest()
        resp_copy.CopyFrom(assist_request)
        if len(resp_copy.audio_in) > 0:
            size = len(resp_copy.audio_in)
            resp_copy.ClearField('audio_in')
            logging.debug('AssistRequest: audio_in (%d bytes)', size)
            return
        logging.debug('AssistRequest: %s', resp_copy)