def parse_json(self, data, encoding='utf-8'):
    if isinstance(data, bytes):
        data = data.decode(encoding)
    data = json.loads(data, parse_float=Decimal)
    if 'remark' in data:
        self._handle_remark_msg(msg=data.get('remark'))
    return Result.from_json(data, api=self)