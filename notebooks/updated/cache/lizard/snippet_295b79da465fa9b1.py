def convert_item_to_flask_url(self, ctx, item, filepath=None):
    if ctx.environment._app.config.get('FLASK_ASSETS_USE_S3'):
        try:
            from flask_s3 import url_for
        except ImportError as e:
            print('You must have Flask S3 to use FLASK_ASSETS_USE_S3 option')
            raise e
    elif ctx.environment._app.config.get('FLASK_ASSETS_USE_CDN'):
        try:
            from flask_cdn import url_for
        except ImportError as e:
            print('You must have Flask CDN to use FLASK_ASSETS_USE_CDN option')
            raise e
    elif ctx.environment._app.config.get('FLASK_ASSETS_USE_AZURE'):
        try:
            from flask_azure_storage import url_for
        except ImportError as e:
            print(
                'You must have Flask Azure Storage to use FLASK_ASSETS_USE_AZURE option'
                )
            raise e
    else:
        from flask import url_for
    directory, rel_path, endpoint = self.split_prefix(ctx, item)
    if filepath is not None:
        filename = filepath[len(directory) + 1:]
    else:
        filename = rel_path
    flask_ctx = None
    if not _request_ctx_stack.top:
        flask_ctx = ctx.environment._app.test_request_context()
        flask_ctx.push()
    try:
        url = url_for(endpoint, filename=filename)
        if url and url.startswith('http:'):
            url = url[5:]
        return url
    finally:
        if flask_ctx:
            flask_ctx.pop()