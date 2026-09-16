def waitOrTerminate(self, timeoutSeconds, pollInterval=
    DEFAULT_POLL_INTERVAL, terminateToKillSeconds=
    SUBPROCESS2_DEFAULT_TERMINATE_TO_KILL_SECONDS):
    returnCode = self.waitUpTo(timeoutSeconds, pollInterval)
    actionTaken = SUBPROCESS2_PROCESS_COMPLETED
    if returnCode is None:
        if terminateToKillSeconds is None:
            self.terminate()
            actionTaken |= SUBPROCESS2_PROCESS_TERMINATED
            time.sleep(pollInterval)
            returnCode = self.poll()
        elif terminateToKillSeconds == 0:
            self.kill()
            actionTaken |= SUBPROCESS2_PROCESS_KILLED
            time.sleep(0.01)
            self.poll()
            returnCode = None
        else:
            self.terminate()
            actionTaken |= SUBPROCESS2_PROCESS_TERMINATED
            returnCode = self.waitUpTo(terminateToKillSeconds, pollInterval)
            if returnCode is None:
                actionTaken |= SUBPROCESS2_PROCESS_KILLED
                self.kill()
                time.sleep(0.01)
                self.poll()
    return {'returnCode': returnCode, 'actionTaken': actionTaken}