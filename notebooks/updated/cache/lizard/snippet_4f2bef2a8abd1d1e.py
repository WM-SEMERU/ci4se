def listar_healtchcheck_expect_distinct(self):
    url = 'healthcheckexpect/distinct/busca/'
    code, xml = self.submit(None, 'GET', url)
    return self.response(code, xml)