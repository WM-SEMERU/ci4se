def server_inspect_exception(self, req_event, rep_event, task_ctx, exc_info):
    if self._hide_zerorpc_frames:
        traceback = exc_info[2]
        while traceback:
            zerorpc_frame = traceback.tb_frame
            zerorpc_frame.f_locals['__traceback_hide__'] = True
            frame_info = inspect.getframeinfo(zerorpc_frame)
            if (frame_info.function == '__call__' or frame_info.function ==
                '_receiver'):
                break
            traceback = traceback.tb_next
    self._elasticapm_client.capture_exception(exc_info, extra=task_ctx,
        handled=False)