def copy_artifact(src_path: str, artifact_hash: str, conf: Config):
    cache_dir = conf.get_artifacts_cache_dir()
    if not isdir(cache_dir):
        makedirs(cache_dir)
    cached_artifact_path = join(cache_dir, artifact_hash)
    if isfile(cached_artifact_path) or isdir(cached_artifact_path):
        logger.debug('Skipping copy of existing cached artifact {} -> {}',
            src_path, cached_artifact_path)
        return
    abs_src_path = join(conf.project_root, src_path)
    logger.debug('Caching artifact {} under {}', abs_src_path,
        cached_artifact_path)
    shutil.copy(abs_src_path, cached_artifact_path)