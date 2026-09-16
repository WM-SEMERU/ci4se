async def upload_artifacts(context, files):

    def to_upload_future(target_path):
        path = os.path.join(context.config['artifact_dir'], target_path)
        content_type, content_encoding = compress_artifact_if_supported(path)
        return asyncio.ensure_future(retry_create_artifact(context, path,
            target_path=target_path, content_type=content_type,
            content_encoding=content_encoding))
    tasks = list(map(to_upload_future, files))
    await raise_future_exceptions(tasks)