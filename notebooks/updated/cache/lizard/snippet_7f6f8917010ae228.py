def get_object(self, ObjectClass, id):
    print('dynamo.get(%s, %s)' % (ObjectClass, str(id)))
    resp = self.db.engine.get(ObjectClass, [id])
    if resp:
        return resp[0]
    else:
        return None