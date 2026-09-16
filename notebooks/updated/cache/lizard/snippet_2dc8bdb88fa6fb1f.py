def execute(self, call):
    method = self.get_method(call)
    deferred = maybeDeferred(self.authorize, method, call)
    deferred.addCallback(lambda _: method.invoke(call))
    return deferred.addCallback(self.dump_result)