def save_codeobject(self, obj):
    if self.dump_code:
        print(obj.co_name)
        dis.dis(obj.co_code)
    self.save_reduce(types.CodeType, self._extract_code_args(obj), obj=obj)