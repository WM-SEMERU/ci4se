def ncbi_geneid(self):
    values = self.get_attribute('Dbxref', as_list=True)
    if values is None:
        return None
    for value in values:
        if value.startswith('GeneID:'):
            key, geneid = value.split(':')
            return geneid
    return None