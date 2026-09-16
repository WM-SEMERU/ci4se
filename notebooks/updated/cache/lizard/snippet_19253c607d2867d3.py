def lastProgress(self):
    lastProgress = self._jsq.lastProgress()
    if lastProgress:
        return json.loads(lastProgress.json())
    else:
        return None