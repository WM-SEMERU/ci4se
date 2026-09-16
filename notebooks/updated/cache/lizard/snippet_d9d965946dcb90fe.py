def get_orchestrator_build_logs(self, build_id, follow=False,
    wait_if_missing=False):
    logs = self.get_build_logs(build_id=build_id, follow=follow,
        wait_if_missing=wait_if_missing, decode=True)
    if logs is None:
        return
    if isinstance(logs, GeneratorType):
        for entries in logs:
            for entry in entries.splitlines():
                yield LogEntry(*self._parse_build_log_entry(entry))
    else:
        for entry in logs.splitlines():
            yield LogEntry(*self._parse_build_log_entry(entry))