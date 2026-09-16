def open_file(cls, filename: str, response: BaseResponse, mode='wb+'):
    _logger.debug('Saving file to {0}, mode={1}.', filename, mode)
    dir_path = os.path.dirname(filename)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)
    response.body = Body(open(filename, mode))