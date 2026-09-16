def run(self, queue):
    time.sleep(random.random())
    obj = self.get_object()
    obj.fullname.hset('%s %s' % tuple(obj.hmget('firstname', 'lastname')))
    result = 'Created fullname for Person %s: %s' % (obj.pk.get(), obj.
        fullname.hget())
    self.result.set(result)
    return result