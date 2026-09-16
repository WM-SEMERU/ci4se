def updatedJobWorker(self):
    resultsFiles = set()
    resultsFileHandles = []
    try:
        while self.running:
            newResultsFiles = set(os.listdir(self.parasolResultsDir)
                ).difference(resultsFiles)
            for newFile in newResultsFiles:
                newFilePath = os.path.join(self.parasolResultsDir, newFile)
                resultsFileHandles.append(open(newFilePath, 'r'))
                resultsFiles.add(newFile)
            for fileHandle in resultsFileHandles:
                while self.running:
                    line = fileHandle.readline()
                    if not line:
                        break
                    assert line[-1] == '\n'
                    (status, host, jobId, exe, usrTicks, sysTicks,
                        submitTime, startTime, endTime, user, errFile, command
                        ) = line[:-1].split(None, 11)
                    status = int(status)
                    jobId = int(jobId)
                    if os.WIFEXITED(status):
                        status = os.WEXITSTATUS(status)
                    else:
                        status = -status
                    self.cpuUsageQueue.put(jobId)
                    startTime = int(startTime)
                    endTime = int(endTime)
                    if endTime == startTime:
                        usrTicks = int(usrTicks)
                        sysTicks = int(sysTicks)
                        wallTime = float(max(1, usrTicks + sysTicks)) * 0.01
                    else:
                        wallTime = float(endTime - startTime)
                    self.updatedJobsQueue.put((jobId, status, wallTime))
            time.sleep(1)
    except:
        logger.warn('Error occurred while parsing parasol results files.')
        raise
    finally:
        for fileHandle in resultsFileHandles:
            fileHandle.close()