def _get_file_size(path, get_retriever):
    integration, config = get_retriever.integration_and_config(path)
    if integration:
        return integration.file_size(path, config)
    elif os.path.exists(path):
        return os.path.getsize(path) / (1024.0 * 1024.0)