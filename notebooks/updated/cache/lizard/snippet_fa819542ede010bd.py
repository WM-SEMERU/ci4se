def get_file(file_id, **kwargs):
    params = dict(file_id=file_id)
    return TelegramBotRPCRequest('getFile', params=params, on_result=File.
        from_result, **kwargs)