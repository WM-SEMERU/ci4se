def splunk(cmd, user='admin', passwd='changeme'):
    return sudo('/opt/splunkforwarder/bin/splunk {c} -auth {u}:{p}'.format(
        c=cmd, u=user, p=passwd))