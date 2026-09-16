def get_rule_by_id(self, rule_id):
    url = 'rule/get_by_id/' + str(rule_id)
    code, xml = self.submit(None, 'GET', url)
    return self.response(code, xml, ['rule_contents', 'rule_blocks'])