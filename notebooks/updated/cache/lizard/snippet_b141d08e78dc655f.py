def infra_nodes(info, meta, max_pod_cluster, label, key):
    nodes = meta.get(label, []) or []
    infos = info[info['machine_id'].isin(nodes)]
    if infos.empty:
        return
    return make_response(key, max_pod_cluster=max_pod_cluster, infos=infos,
        GREEN=Fore.GREEN, RED=Fore.RED, YELLOW=Fore.YELLOW, NC=Style.RESET_ALL)