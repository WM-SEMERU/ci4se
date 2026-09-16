def pathExists(self, path):

    def commandComplete(cmd):
        return not cmd.didFail()
    return self.runRemoteCommand('stat', {'file': path, 'logEnviron': self.
        logEnviron}, abandonOnFailure=False, evaluateCommand=commandComplete)