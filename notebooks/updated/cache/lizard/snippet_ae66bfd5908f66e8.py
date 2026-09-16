async def send_ssh_job_info(self, job_id: BackendJobId, host: str, port:
    int, key: str):
    if job_id not in self.__running_job:
        raise JobNotRunningException()
    if self.__running_job[job_id]:
        raise TooManyCallsException()
    self.__running_job[job_id] = True
    await ZMQUtils.send(self.__backend_socket, AgentJobSSHDebug(job_id,
        host, port, key))