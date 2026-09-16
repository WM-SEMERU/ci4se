def list_relations(self):
    _ = self._execute('select * from relations').fetchall()
    for i in _:
        src, name, dst = i
        src = self.deserialize(next(self._execute(
            'select code from objects where id=?', (src,)))[0])
        dst = self.deserialize(next(self._execute(
            'select code from objects where id=?', (dst,)))[0])
        yield src, name, dst