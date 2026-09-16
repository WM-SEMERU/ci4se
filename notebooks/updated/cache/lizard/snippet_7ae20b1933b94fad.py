def getHostsFromPBS():
    with open(os.environ['PBS_NODEFILE'], 'r') as hosts:
        hostlist = groupTogether(hosts.read().split())
        retVal = []
        for key, group in groupby(hostlist):
            retVal.append((key, len(list(group))))
        return retVal