async def download_cot_artifact(chain, task_id, path):
    link = chain.get_link(task_id)
    log.debug('Verifying {} is in {} cot artifacts...'.format(path, task_id))
    if not link.cot:
        log.warning(
            'Chain of Trust for "{}" in {} does not exist. See above log for more details. Skipping download of this artifact'
            .format(path, task_id))
        return
    if path not in link.cot['artifacts']:
        raise CoTError('path {} not in {} {} chain of trust artifacts!'.
            format(path, link.name, link.task_id))
    url = get_artifact_url(chain.context, task_id, path)
    loggable_url = get_loggable_url(url)
    log.info('Downloading Chain of Trust artifact:\n{}'.format(loggable_url))
    await download_artifacts(chain.context, [url], parent_dir=link.cot_dir,
        valid_artifact_task_ids=[task_id])
    full_path = link.get_artifact_full_path(path)
    for alg, expected_sha in link.cot['artifacts'][path].items():
        if alg not in chain.context.config['valid_hash_algorithms']:
            raise CoTError('BAD HASH ALGORITHM: {}: {} {}!'.format(link.
                name, alg, full_path))
        real_sha = get_hash(full_path, hash_alg=alg)
        if expected_sha != real_sha:
            raise CoTError('BAD HASH on file {}: {}: Expected {} {}; got {}!'
                .format(full_path, link.name, alg, expected_sha, real_sha))
        log.debug('{} matches the expected {} {}'.format(full_path, alg,
            expected_sha))
    return full_path