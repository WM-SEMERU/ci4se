def exists(self):
    return self.rpc_model.search_count(self.domain, context=self.context) > 0