def list(self, deployment_sid=values.unset, limit=None, page_size=None):
    return list(self.stream(deployment_sid=deployment_sid, limit=limit,
        page_size=page_size))