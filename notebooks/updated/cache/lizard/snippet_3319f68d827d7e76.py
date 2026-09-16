def doUpdate(self, timeout=1):
    namespace = Fritz.getServiceType('doUpdate')
    uri = self.getControlURL(namespace)
    results = self.execute(uri, namespace, 'X_AVM-DE_DoUpdate', timeout=timeout
        )
    return results['NewUpgradeAvailable'], results['NewX_AVM-DE_UpdateState']