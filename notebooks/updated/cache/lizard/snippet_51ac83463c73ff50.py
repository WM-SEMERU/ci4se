def _is_pod_host_networked(self, pod_uid):
    for pod in self.pod_list['items']:
        if pod.get('metadata', {}).get('uid', '') == pod_uid:
            return pod.get('spec', {}).get('hostNetwork', False)
    return False